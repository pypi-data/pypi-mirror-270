#!/usr/bin/env python3

# SPDX-License-Identifier: LGPL-2.1-or-later

# Copyright (C) 2021 Pengutronix, Chris Fiege <entwicklung@pengutronix.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import contextlib
import errno
import struct
from sys import stderr
from time import sleep

import usb.core

from .firmware import version


def path_from_usb_dev(dev):
    """Takes a pyUSB device as argument and returns a string.
    The string is a Path representation of the position of the USB device on the USB bus tree.

    This path is used to find a USB device on the bus or all devices connected to a HUB.
    The path is made up of the number of the USB controller followed be the ports of the HUB tree."""
    if dev.port_numbers:
        dev_path = ".".join(str(i) for i in dev.port_numbers)
        return f"{dev.bus}-{dev_path}"
    else:
        return ""


class UmuxNotFound(Exception):
    pass


class NoPrivileges(Exception):
    pass


class ProtocolVersionMismatch(Exception):
    pass


class Mux:
    """
    This class implements a driver for a USB-Mux device.
    """

    # USB-Commands
    _GET_STATUS = 0
    _SET_POWER = 1
    _SET_DATA = 2
    _SET_OTG = 3
    _DFU = 42
    _SW_VERSION = 254
    _PROTO_VERSION = 255

    _USB_IDs = [
        {
            # This is our actual Linux Automation GmbH Vendor ID and our actual Product ID.
            "VENDORID": 0x33F7,
            "PRODUCTID": 0x0001,
        },
        {
            # This is a _fake_ Vendor-ID and Product-ID that we have chosen by throwing dice during
            # development. This ID is only for the transition phase. There should be no USB-Muxes
            # in the wild using this ID!
            "VENDORID": 0x5824,
            "PRODUCTID": 0x27DD,
        },
    ]

    _USB_REQ_TYPE_DIR_HOST_TO_DEVICE = 0x80
    _USB_REQ_TYPE_TYPE_VENDOR = 0x40
    _USB_REQ_TYPE_RECIPIENT_DEVICE = 0x00

    _STATUS_FLAG_DUT_LOCK = 0x0100
    _STATUS_FLAG_OTG_OUT = 0x0200
    _STATUS_FLAG_OTG_IN = 0x0080

    # _ADC calibration data
    _ADC_RANGE = (1 << 16) - 1
    _ADC_SCALE = 3.3 * 3

    # Possible Links that can be set by the USB-Mux on power and data links
    # The values of this dict are used for the connect() method.
    _LINKS = {0: "None", 1: "Device-Host", 2: "DUT-Host", 3: "DUT-Host Device-Host", 4: "DUT-Device"}

    @staticmethod
    def find_devices():
        """
        Searches for a list of USB-Mux devices.

        Returns a list of all found devices:
        [{"serial": <SN>, "path": <UsbPath>}, ...]
        """
        found = []
        for ids in Mux._USB_IDs:
            devices = usb.core.find(find_all=True, idVendor=ids["VENDORID"], idProduct=ids["PRODUCTID"])
            for dev in devices:
                path = path_from_usb_dev(dev)
                found.append(
                    {
                        "serial": dev.serial_number,
                        "path": path,
                    }
                )
        return found

    def __init__(self, serial_number=None, path=None):
        """
        Create a new Mux instance.

        Selects the device by the given serial_numer or USB path.
        Both values can be obtained using Mux.find_devices().
        If both are given serial_number has priority over path.
        If neither is given the first found USB-Mux will be used.
        """

        def find_filter(dev):
            dev_path = path_from_usb_dev(dev)

            # Perform a dummy-acces on the device to make sure
            # we actually have permissions to access it, as
            # otherwise accessing dev.serial_number will result
            # in an exception being thrown from which the reason
            # of the error is not immediately obvious.
            try:
                dev.get_active_configuration()
            except usb.core.USBError as e:
                if e.errno == errno.EACCES:
                    print("Access denied while checking serial number for device:", dev_path, file=stderr)

                    return False

                raise e

            if serial_number is not None:
                return dev.serial_number == serial_number
            if path is not None:
                return dev_path == path
            return True

        for ids in Mux._USB_IDs:
            self._dev = usb.core.find(
                idVendor=ids["VENDORID"],
                idProduct=ids["PRODUCTID"],
                custom_match=find_filter,
            )
            if self._dev is not None:
                break

        if self._dev is None:
            raise UmuxNotFound()

        try:
            # check if we support the protocol version reported by the usbmux
            proto_version = self._send_cmd(self._PROTO_VERSION)
            if len(proto_version) != 8:
                raise ProtocolVersionMismatch(
                    "The protocol version reported by the USB-Mux is not supported by this control tool."
                )
            self._proto_version = "".join(str(x) for x in proto_version)
            if self._proto_version not in ["00000000"]:
                raise ProtocolVersionMismatch(
                    "The protocol version reported by the USB-Mux is not supported by this control tool."
                )
        except ValueError as e:
            raise NoPrivileges("Could not communicate with USB-device. Check privileges, maybe add udev-rule") from e

        # read sw version
        self.sw_version = str(self._send_cmd(self._SW_VERSION), "utf-8")
        self.sw_version_num = version.version_from_string(self.sw_version)

    def _send_cmd(self, cmd, arg=0):
        """
        Sends a low level USB control transfer to the device.
        """
        data = self._dev.ctrl_transfer(
            self._USB_REQ_TYPE_DIR_HOST_TO_DEVICE
            | self._USB_REQ_TYPE_TYPE_VENDOR
            | self._USB_REQ_TYPE_RECIPIENT_DEVICE,
            0xFF,
            cmd,
            arg,
            128,
        )
        return data

    def _parse_return(self, pkg):
        """
        Parses the status returned by most USB commands.

        Returns a dict with the available information on the hardware.
        """
        if len(pkg) != 8:
            raise Exception("Invalid Package length")

        (volt_host_raw, volt_device_raw, volt_dut_raw, flags) = struct.unpack("!HHHH", pkg)

        path = path_from_usb_dev(self._dev)
        state = {
            "voltage_host": volt_host_raw * self._ADC_SCALE / self._ADC_RANGE,
            "voltage_device": volt_device_raw * self._ADC_SCALE / self._ADC_RANGE,
            "voltage_dut": volt_dut_raw * self._ADC_SCALE / self._ADC_RANGE,
            "dut_power_lockout": (flags & self._STATUS_FLAG_DUT_LOCK) != 0,
            "dut_otg_output": (flags & self._STATUS_FLAG_OTG_OUT) != 0,
            "dut_otg_input": (flags & self._STATUS_FLAG_OTG_IN) != 0,
            "power_links": self._LINKS[(flags >> 10) & 0b111],
            "data_links": self._LINKS[(flags >> 13) & 0b111],
            "device": {
                "usb_path": path,
                "serial_number": self._dev.serial_number,
                "product_name": self._dev.product,
                "sw_version": self.sw_version,
                "sw_up_to_date": self.is_software_up_to_date(),
            },
        }
        return state

    def _connect_power(self, num):
        """
        Applies a connection for the power links on the USB-Mux.
        num must be one of Mux._LINKS.

        If the Host-DUT link is locked in hardware this command will
        still succeed, but this link will not be set. The state returned
        will reflect this.

        Return the parsed status received by the USB-Mux as a dict.
        """
        if 4 <= num <= 0:
            raise Exception(f"{num} is not a valid power connection id")
        data = self._send_cmd(self._SET_POWER, num)
        return self._parse_return(data)

    def _connect_data(self, num):
        """
        Applies a connection for the data links on the USB-Mux.
        num must be one of Mux._LINKS.

        If the Host-DUT link is locked in hardware this command will
        still succeed, but this link will not be set. The state returned
        will reflect this.

        Return the parsed status received by the USB-Mux as a dict.
        """
        if 4 <= num <= 0:
            raise Exception(f"{num} is not a valid data connection id")
        data = self._send_cmd(self._SET_DATA, num)
        return self._parse_return(data)

    def pull_otg_id_low(self, state):
        """
        Sets the state of the ID pin on the DUT port.

        If state is True: Pulls ID pin low
        If state is False: Leave ID pin floating, a 100k Pull Up is active

        Return the parsed status received by the USB-Mux as a dict.
        """
        data = self._send_cmd(self._SET_OTG, int(state))
        return self._parse_return(data)

    def get_status(self):
        """
        Queries the state of the USB-Mux.

        Return the parsed status received by the USB-Mux as a dict.
        """
        data = self._send_cmd(self._GET_STATUS)
        return self._parse_return(data)

    def enter_dfu(self):
        """
        Disconnects all Links and resets the CPU into the DFU-Mode.
        DFU-Mode is provided by the ROM Code.
        This mode is used to transfer firmware onto the device.

        To resume normal operation the USB-Mux must be either reset
        using the DFU-Mode or power cycled.
        """
        self._connect_power(0)
        self._connect_data(0)

        sleep(0.1)
        with contextlib.suppress(usb.core.USBError):
            self._send_cmd(self._DFU)

    def connect(self, links, id_pull_low=None):
        """
        Applies a connection between ports of the USB-Mux.

        Before switching to a new connection all current connections
        are being removed and this methods gives the USB-Mux about 0.5 s to settle.
        This will cycle the power to all connected USB devices.
        Afterwards the new links are being connected.

        links must be one of MUX._LINKS.

        id_pull_low affects the ID pin on the DUT port:
        if id_pull_low is None: The ID pin is not altered at all. Use
                                 pull_otg_low() to set the ID pin independent
                                 of the USB links.
        if id_pull_low is True: The ID pin is set floating when the previous connections
                                are being disconnected. The ID pin will be pulled low before
                                the new links are being connected.
        if id_pull_low is False: The ID pin is set floating when the previous connections
                                 are being disconnected. The ID pin will be left floating
                                 when the new links are being connected.
        """
        num = None
        for key, value in Mux._LINKS.items():
            if value == links:
                num = key
        if num is None:
            raise Exception(f"Invalid connection {links}")

        self._connect_power(0)
        self._connect_data(0)
        if id_pull_low is not None:
            self.pull_otg_id_low(False)

        sleep(0.5)  # Gives switches time to settle and devices to power off

        self._connect_power(num)
        self._connect_data(num)
        if id_pull_low is not None:
            self.pull_otg_id_low(id_pull_low)

        sleep(0.3)  # Wait a little moment for switches to settle

    def __str__(self):
        path = path_from_usb_dev(self._dev)
        path = f"Connected to:\n- ID:   {self._dev.serial_number}\n- Path: {path}\n- Name: {self._dev.product}"
        return path

    def is_software_up_to_date(self):
        return self.sw_version_num >= version.FIRMWARE_VERSION

    def update_software(self):
        """Updates the usbmux software"""

        from .update import (
            DFU,
            dfu_util_flash_firmware,
            dfu_util_version,
        )

        # We do not care about the actual version string but want this
        # to fail early (before we've entered DFU mode) if dfu-util is not installed.
        _ = dfu_util_version()
        self.enter_dfu()
        sleep(1)

        usb_path = path_from_usb_dev(self._dev)

        dfu = DFU(path=usb_path)

        dfu_util_flash_firmware(version.FIRMWARE_FILE, dfu.get_path())

        dfu.enter_user_code()
