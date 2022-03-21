#!/bin/bash

################################################################################
# Messi is a soccer player with goals in three leagues:
#  - LaLiga
#  - Copa del Rey
#  - Champions
# Complete the function to return his total number of goals in all three leagues
################################################################################

# laLigaGoals=$1
# copaDelReyGoals=$2
# championsLeagueGoals=$3

sum_goals() {
    echo $(expr $1 + $2 + $3)
}

# TESTS
sum_goals 10 5 2
sum_goals 0 0 0
sum_goals 0 10 15 20
