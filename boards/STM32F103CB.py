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
 'name' : "STM32F103CB",
 'link' :  [ "" ],
 'variables' : 715,
 'binary_name' : 'espruino_%v_stm32f103cb.bin',
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
  'ext' : [ 'D14', 'GND', 'D13', 'D12', 'D11','D10', 'D9', 'D8', '', 'D7', 'D6', 'D5', 'D4', 'D3', 'D2', 'D1', 'D0']
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
  #'LED1' : { 'pin' : 'D13' },
  #'LED2' : { 'pin' : 'D3' },
  # 'BTN1' : { 'pin' : 'D38' }, # 'C9'
  'USB' : { 'pin_disc' :  'A3',
            'pin_dm' : 'A11',
            'pin_dp' : 'A12'
          },
  'SD' :  { 'pin_cs' :  'A4',
            'pin_di' :  'A7',
            'pin_do' :  'A6',
            'pin_clk' :  'A5'},
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

