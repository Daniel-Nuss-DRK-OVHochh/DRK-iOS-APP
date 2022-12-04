#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Daniel Nuß
# Created Date: 2022-04-16
# ---------------------------------------------------------------------------
""" Allgemeine DRK Funktionen"""                                            #
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from adafruit_platformdetect import Detector
from getmac import get_mac_address as gma
from sys import platform
import psutil
import os
from datetime import datetime


def local_date():
    now = datetime.now()
    return now.strftime('%d.%m.%Y')


def local_time():
    now = datetime.now()
    return now.strftime('%H:%M:%S')


def get_gu_id():
    # return str(uuid.getnode())
    return str(gma())


def get_process_id():
    return str(os.getpid())


def get_boottime():
    return datetime.fromtimestamp(psutil.boot_time()).strftime("%d.%m.%y %H:%M:%S")


def is_rpi():
    detector = Detector()
    # loading Libraries which only can be used on RaspberryPI
    rpi_on = detector.board.any_raspberry_pi
    return rpi_on


def get_osrunning():
    if platform == "linux" or platform == "linux2":
        os_run = "Linux"
    elif platform == "darwin":
        os_run = "Mac OS X"
    elif platform == "win32":
        os_run = "Windows"
    else:
        os_run = "unknown"
    return os_run


def reconnect_networks():
    if get_osrunning() == "Linux":
        os.system("/usr/bin/sudo /usr/sbin/ip link set dev eth0 down")
        os.system("/usr/bin/sudo /usr/sbin/ip link set dev tun0 down")
        os.system("/usr/bin/sudo /usr/sbin/ip link set dev wlan0 down")

        os.system("/usr/bin/sudo /usr/sbin/ip link set dev eth0 up")
        os.system("/usr/bin/sudo /usr/sbin/ip link set dev tun0 up")
        os.system("/usr/bin/sudo /usr/sbin/ip link set dev wlan0 up")

    if get_osrunning() == "Windows":
        os.system("netsh interface set interface name=\"Ethernet\" admin=disabled")
        os.system("netsh interface set interface name=\"WLAN\" admin=disabled")
        os.system("netsh interface set interface name=\"Ethernet\" admin=enabled")
        os.system("netsh interface set interface name=\"WLAN\" admin=enabled")


def restart_system():
    if get_osrunning() == "Linux":
        os.system("/usr/bin/sudo /usr/lib/molly-guard/reboot")
    if get_osrunning() == "Windows":
        os.system("shutdown /r /t 0")


def get_timestamp():
    now = datetime.now()
    local_datetime = now.strftime('%Y-%m-%d') + " " + now.strftime('%H:%M:%S')
    return local_datetime
