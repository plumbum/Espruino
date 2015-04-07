#!/bin/false
# This file is part of Espruino, a JavaScript interpreter for Microcontrollers
#
# Copyright (C) 2013 Gordon Williams <gw@pur3.co.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# ----------------------------------------------------------------------------------------
# This file contains information for a specific board - the available pins, and where LEDs,
# Buttons, and other in-built peripherals are. It is used to build documentation as well
# as various source and header files for Espruino.
# ----------------------------------------------------------------------------------------

import pinutils;
import json;
info = {
 'name' : "Home power control",
 'link' :  [ "https://github.com/plumbum/home-power-control" ],
 'variables' : 715,
 'binary_name' : 'espruino_%v_homepowerctrl_stm32.bin',
};
chip = {
  'part' : "STM32F103CBT6",
  'family' : "STM32F1",
  'package' : "LQFP48",
  'ram' : 20,
  'flash' : 128,
  'speed' : 72,
  'usart' : 3,
  'spi' : 2,
  'i2c' : 2,
  'adc' : 3,
  'dac' : 0,
};
# left-right, or top-bottom order
board = {
  'ext' : [ '3V3', 'GND', 'A9', 'A10', 'B10', 'B11', 'B14', 'B15', 'B13', 'B12' ]

  # '_pinmap' : { 'A0':'D15', 'A1':'D16', 'A2':'D17', 'A3':'D18', 'A4':'D19', 'A5':'D20' }
};
#board["left"].reverse()
#board["left2"].reverse()
#board["right"].reverse()
#board["right2"].reverse()

devices = {
  'OSC' : { 'pin_1' :  'D0',
            'pin_2' : 'D1' },
  'OSC_RTC' : { 'pin_1' :  'C14',
                'pin_2' : 'C15' },
  'LED1' : { 'pin' : 'B3' },
  'LED2' : { 'pin' : 'A15' },
  'LED3' : { 'pin' : 'B1' },
  'LED4' : { 'pin' : 'B0' },
  'BTN1' : { 'pin' : 'B8',
             'inverted' : True, # 1 when unpressed, 0 when pressed! (Espruino board is 1 when pressed)
             'pinstate': 'IN_PULLUP', # to specify INPUT, OUPUT PULL_UP PULL_DOWN..
         },
  'BTN2' : { 'pin' : 'B9',
             'inverted' : True, # 1 when unpressed, 0 when pressed! (Espruino board is 1 when pressed)
             'pinstate': 'IN_PULLUP', # to specify INPUT, OUPUT PULL_UP PULL_DOWN..
         },
  'USB' : { 'pin_disc' :  'A1',
            'pin_dm' : 'A11',
            'pin_dp' : 'A12'
          },
  #'SD' :  { 'pin_cs' :  'D25',#'D2',
  #          'pin_di' :  'D34',#'B15',
  #          'pin_do' :  'D33',#'B14',
  #          'pin_clk' :  'D32'}, #'B13'
};

board_css = """
#board {
  width: 540px;
  height: 418px;
  top: 300px;
  left: 200px;
  background-image: url(img/OLIMEXINO_STM32.jpg);
}
#boardcontainer {
  height: 850px;
}

#top {
  top: -20px;
  left: 140px;
}
#bottom  {
  top: 431px;
  left: 220px;
}

#left {
  top: 155px;
  right: 520px;
  
}
#left2  {
  top:155px;
  left: 20px;
}

#right {
  top: 155px;
  left: 520px;
}
#right2  {
  top: 155px;
  right: 20px;
}

""";



def get_pins():
  pins = pinutils.scan_pin_file([], 'stm32f103xb.csv', 6, 10, 11)
  return pinutils.only_from_package(pinutils.fill_gaps_in_pin_list(pins), chip["package"])

