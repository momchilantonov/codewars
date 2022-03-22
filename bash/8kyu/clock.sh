#!/bin/bash

################################################################################
# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since
# midnight in milliseconds.
################################################################################

# h=$1
# m=$2
# s=$3

convert_time() {
    echo $((($1 * 3600 + $2 * 60 + $3) * 1000))
}

# TESTS
convert_time 0 1 1
convert_time 1 1 1
convert_time 0 0 0
convert_time 1 0 1
convert_time 1 0 0
