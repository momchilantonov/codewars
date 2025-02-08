#!/bin/bash

################################################################################
# Bob needs a fast way to calculate the volume of a cuboid with three values:
# length, width and the height of the cuboid.
# Write a function to help Bob with this calculation.
################################################################################

# length=$1
# width=$2
# height=$3

cuboid_volume() {
    echo "$1 * $2 * $3" | bc
}

# TESTS
cuboid_volume 2 5 6
cuboid_volume 6.3 3 5
