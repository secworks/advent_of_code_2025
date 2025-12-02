#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# day02.py
# --------
# Solution to Advent of Code 2025, day 02.
# https://adventofcode.com/2025/day/2
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
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            for part in line.split(','):
                a, b = map(int, part.split('-'))
                l.append((a, b))
    return l

#-------------------------------------------------------------------
# add_invalid_ids_problem_one
#
# Find accumulate values that are invalid in a set of given ranges.
# Stragy
# 1. step through the sequence
#
# 2. check each number if the lengt of the numger is even. If is
# it may be an invalid id.
#
# 2. Split the number in half and compare the halves.
# If they match it is an invalid id.
#-------------------------------------------------------------------
def add_invalid_ids_problem_one(filename):
    print(f"Finding the sum of invalid IDs, the problem for {filename}")

    my_input = get_input(filename)
    sum_invalid_ids = 0

    for curr_range in my_input:
        (start, end) = curr_range
        print(f"The current range {start} - {end}")

        for i in range(start, end + 1):
            i_len2 = len(str(i)) // 2
            i_left = str(i)[:i_len2]
            i_right = str(i)[i_len2:]
            if i_left == i_right:
                print(f"Founded it: {i}")
                sum_invalid_ids += int(i)
        print("\n")

    print(f"\nThe sum of all invalid ids: {sum_invalid_ids}\n")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
if __name__=="__main__":
    print("Advent of Code 2025, day 02")
    print("===========================")

#    add_invalid_ids_problem_one("day02_example.txt")
    add_invalid_ids_problem_one("day02_input.txt")

    sys.exit(0)

#=======================================================================
