#!/bin/bash

################################################################################
# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres
# of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres
# Nathan will drink, rounded to the smallest value.
################################################################################

# time=$1

count_liters() {
    echo "$1/2" | bc
}

# TESTS
count_liters 3
count_liters 6.7
count_liters 11.8