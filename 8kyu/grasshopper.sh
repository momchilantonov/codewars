#!/bin/bash

<<DESCRIPTION
    Messi is a soccer player with goals in three leagues:
    - LaLiga
    - Copa del Rey
    - Champions
    Complete the function to return his total number of goals in all three leagues.
DESCRIPTION

laLigaGoals=$1
copaDelReyGoals=$2
championsLeagueGoals=$3

grasshopper() {
    echo $(expr $1 + $2 + $3)
}

# TESTS
grasshopper 10 5 2
grasshopper 0 0 0
grasshopper 0 10 15 20