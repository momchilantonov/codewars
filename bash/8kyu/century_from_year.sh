#!/bin/bash

################################################################################
# The first century spans from the year 1 up to and including the year 100,
# the second century - from the year 101 up to and including the year 200, etc.
# Given a year, return the century it is in.
################################################################################

# year=$1

get_century() {
    echo $(expr $(expr $1 - 1) \/ 100 + 1)
}

# TESTS
get_century 1705 # 18
get_century 1900 # 19
get_century 1601 # 17
get_century 2000 # 20
get_century 89   # 1
