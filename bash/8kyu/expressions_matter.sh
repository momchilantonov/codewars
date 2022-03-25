#!/bin/bash

################################################################################
# Given three integers a ,b ,c, return the largest number obtained after
# inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] ,
# and return the Maximum Obtained
################################################################################

expressions_metter() {
    a=$1
    b=$2
    c=$3

    e1=$((a + b + c))
    e2=$((a * b * c))
    e3=$(((a + b) * c))
    e4=$((a * (b + c)))

    arr=($e1 $e2 $e3 $e4)

    # max=${arr[0]}

    # for n in "${arr[@]}"; do
    #     ((n > max)) && max=$n
    # done

    # echo $max
    
    IFS=$'\n'

    echo "${arr[*]}" | sort -nr | head -n1
}

# #TESTS
expressions_metter 2 1 1  #  4
expressions_metter 2 2 4  #  16
expressions_metter 3 3 3  #  27
expressions_metter 2 1 2  #  6
expressions_metter 1 1 1  #  3
expressions_metter 1 2 3  #  9
expressions_metter 1 3 1  #  5
expressions_metter 2 2 2  #  8
expressions_metter 5 1 3  #  20
expressions_metter 3 5 7  #  105
expressions_metter 5 6 1  #  35
expressions_metter 1 6 1  #  8
expressions_metter 2 6 1  #  14
expressions_metter 6 7 1  #  48
expressions_metter 2 10 3 #  60
expressions_metter 1 8 3  #  27
expressions_metter 9 7 2  #  126
expressions_metter 1 1 10 #  20
expressions_metter 9 1 1  #  18
expressions_metter 10 5 6 #  300
expressions_metter 1 10 1 #  12
