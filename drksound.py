#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Daniel Nuß
# Created Date: 2022-04-10
# version ='0.20.3'
# ---------------------------------------------------------------------------
""" Details about the module and for what purpose it was built for"""  #
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import RPi.GPIO as GPIO#
from time import sleep

def OkBeep():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)

    GPIO.output(21, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(21, GPIO.LOW)
    return

def AlarmBeep():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)

    GPIO.output(21, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(21, GPIO.LOW)
    sleep(0.05)
    GPIO.output(21, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(21, GPIO.LOW)
    sleep(0.05)
    GPIO.output(21, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(21, GPIO.LOW)
    return