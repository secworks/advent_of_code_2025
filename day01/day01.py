#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day01.py
# --------
# Solution to Advent of Code 2025, day 11.
# https://adventofcode.com/2025/day/1
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


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            stripl = line.strip()
            l.append((stripl[0], int(stripl[1:])))

    return l

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_password_problem_one(filename):
    print(f"Finding the problem one password for {filename}")

    my_input = get_input(filename)

    # Perform each move, If the result of a move is zero increase
    # The zero counter.
    curr_pos = 50
    num_zeros = 0
    for move in my_input:
 #       print(f"Current position {curr_pos}")
        (direction, move) = move

        if direction == 'L':
#            print(f"Moving left {move} steps")
            curr_pos = (curr_pos - move) % 100

        else:
#            print(f"Moving right {move} steps")
            curr_pos = (move + curr_pos) % 100
#        print("")

        if (curr_pos == 0):
            num_zeros += 1

    print(f"The number of zeros are {num_zeros}\n")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_password_problem_two(filename):
    print(f"Finding the problem two password for {filename}")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2025, day 01")
    print("===========================")

    get_password_problem_one("day01_example.txt")
    get_password_problem_one("day01_input.txt")

    get_password_problem_two("day01_example.txt")
    get_password_problem_two("day01_input.txt")

    sys.exit(0)

#=======================================================================
#=======================================================================
