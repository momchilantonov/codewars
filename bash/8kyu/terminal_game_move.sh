#!/bin/bash

################################################################################
# In this game, the hero moves from left to right. The player rolls the die and
# moves the number of spaces indicated by the die two times.
# Create a function for the terminal game that takes the current position of the
# hero and the roll (1-6) and return the new position.
################################################################################

# position=$1
# roll=$2

move() {
    echo $(expr $1 + $2 \* 2)
}

# TESTS
move 3 6
