#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day03.py
# --------
# Solution to Advent of Code 2025, day 03.
# https://adventofcode.com/2025/day/3
#
#
# Author: Joachim Strombergson
# Copyright (c) 2025, Joachim Strömbergson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or
# without modification, are permitted provided that the following
# conditions are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#=======================================================================

import sys
import re

#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.rstrip("\n"))
    return l

#-------------------------------------------------------------------
# Find the max value in a string of digits, and the first position
# from left to right that value appears. Returns the max_value
# max_pos and the string with the max_value removed.
#-------------------------------------------------------------------
def find_max(s):
    max_val = -1
    max_pos = 0

    for i in range(len(s)):
        if int(s[i]) > max_val:
            max_val = int(s[i])
            max_pos = i
    return (max_val, max_pos)

#-------------------------------------------------------------------
# Find max joltage for a given string.
#-------------------------------------------------------------------
def max_joltage(s):
    print(s)

    # Get first max, but ignore last digit.
    (max_val1, max_pos1) = find_max(s[:-1])

    # Get seoond max, starting from the next
    # digit afteer where max_val1 was found
    (max_val2, max_pos2) = find_max(s[max_pos1 + 1:])

    joltage = max_val1 * 10 + max_val2
    print("max joltage for", s, ":", joltage)
    return joltage

#-------------------------------------------------------------------
# Get total joltage for all banks.
#-------------------------------------------------------------------
def total_joltage(filename):
    my_battery_banks = get_input(filename)
    print(my_battery_banks)

    total_joltage = 0
    for bank in my_battery_banks:
        total_joltage += max_joltage(bank)
    print("Total joltage for", filename, ":", total_joltage)
    return total_joltage


#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2025, day 03")
    print("===========================")

    total_joltage("day03_input.txt")
#    total_joltage("day03_example.txt")

#=======================================================================
