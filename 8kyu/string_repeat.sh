#!/bin/bash

################################################################################
# Write a function called repeatStr which repeats the given string string
# exactly n times.
################################################################################

# repeat=$1
# string=$2

repeatStr() for i in $(seq $1); do
    echo -n $2
done

# TESTS
repeatStr 10 "I"
repeatStr 3 "Hello World"
