#!/bin/bash

################################################################################
# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# https://en.wikipedia.org/wiki/Triangle
################################################################################

# a=$1
# b=$2

find_third_angle() {
    echo $(expr 180 - $1 - $2)
}

# TESTS
find_third_angle 30 60 # 90
find_third_angle 60 60 # 60
find_third_angle 43 78 # 59
find_third_angle 10 20 # 150
