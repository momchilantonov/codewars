#!/bin/bash

################################################################################
# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.
################################################################################

# base=$1
# factor=$2

check_for_factor() {
    if [ $(($1 % $2)) -eq 0 ]; then echo true; else echo false; fi
    # $(($1 % $2)) && echo false || echo true
}

#TESTS
check_for_factor 10 2    # true
check_for_factor 63 7    # true
check_for_factor 2450 5  # true
check_for_factor 24612 3 # true

check_for_factor 9 2     # false
check_for_factor 653 7   # false
check_for_factor 2453 5  # false
check_for_factor 24617 3 # false
