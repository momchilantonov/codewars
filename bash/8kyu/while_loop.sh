#!/bin/bash

################################################################################
# Create a simple while loop in bash that prints the numbers 1-20 to stdout.
################################################################################

countToTwenty() {
    INDEX=0

    while [ $INDEX -lt 20 ]; do
        INDEX=$(($INDEX + 1))
        echo "Count:" $INDEX
    done

    # echo "Count:" {1..20}
}

# TESTS
countToTwenty
