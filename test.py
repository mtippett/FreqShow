#!/usr/bin/python3

'''
Watch the buttons on the PiTFT case

Created on Dec 29, 2015

'''

import time, os
import uinput 
import RPi.GPIO as GPIO



def watch_the_switches():
    os.system( 'modprobe uinput' )
    GPIO.setmode( GPIO.BCM )

    # 4 buttons as marked on 2.2" TFT case
    GPIO.setup( 17, GPIO.IN, pull_up_down = GPIO.PUD_UP )  # Triangle Button for GPIO17
    GPIO.setup( 22, GPIO.IN, pull_up_down = GPIO.PUD_UP )  # Triangle Button for GPIO22
    GPIO.setup( 23, GPIO.IN, pull_up_down = GPIO.PUD_UP )  # Triangle Button for GPIO23
    GPIO.setup( 27, GPIO.IN, pull_up_down = GPIO.PUD_UP )  # Triangle Button for GPIO27

    # Map keys to these inputs
    events = ( uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_UP, uinput.KEY_DOWN )

    # register events for submission
    device = uinput.Device( events )

    # initial state
    btn_1 = False
    btn_2 = False
    btn_3 = False
    btn_4 = False

    old_status_str = ( btn_1, btn_2, btn_3, btn_4 )
    while True:
        changes_made = False

        if ( not btn_1) and ( not GPIO.input( 17 ) ):  # button 1
            btn_1 = True
            changes_made = True
            device.emit( uinput.KEY_LEFT, 1 )  # press left

        if btn_1 and GPIO.input( 17 ):  # button 1
            btn_1 = False
            changes_made = True
            device.emit( uinput.KEY_LEFT, 0 )  # release left

        if ( not btn_2 ) and ( not GPIO.input( 22 ) ):  # button 2
            btn_2 = True
            changes_made = True
            device.emit( uinput.KEY_RIGHT, 1 )  # Press right

        if btn_2 and GPIO.input( 22 ):  # button 2
            btn_2 = False
            changes_made = True
            device.emit( uinput.KEY_RIGHT, 0 )  # Release right

        if ( not btn_3 ) and ( not GPIO.input( 23 ) ):  # button 3
            btn_3 = True
            changes_made = True
            device.emit( uinput.KEY_UP, 1 )  # Press up

        if btn_3 and GPIO.input( 23 ):  # button 3
            btn_3 = False
            changes_made = True
            device.emit( uinput.KEY_UP, 0 )  # release up

        if ( not btn_4 ) and ( not GPIO.input( 27 ) ):  # button 4
            btn_4 = True
            changes_made = True
            device.emit( uinput.KEY_DOWN, 1 )  # press down

        if btn_4 and GPIO.input( 27 ):  # button 4
            btn_4 = False
            changes_made = True
            device.emit( uinput.KEY_DOWN, 0 )  # release down

        if changes_made:
            changes_made = False
            # debounce button
            time.sleep( .1 )

        time.sleep( .04 )
        status_str =  ( btn_1, btn_2, btn_3, btn_4 )
        if old_status_str != status_str:
            old_status_str = status_str
            print( status_str )

# --------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    watch_the_switches()

