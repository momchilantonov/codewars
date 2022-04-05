#!/bin/bash

################################################################################
# You have an amount of money a0 > 0 and you deposit it with an interest rate
# of p percent divided by 360 per day on the 1st of January 2016.
# You want to have an amount a >= a0.

# Task:
# The function date_nb_days (or dateNbDays...) with parameters a0, a, p
# will return, as a string, the date on which you have just reached a.

# Example:
# date_nb_days(100, 101, 0.98) --> "2017-01-01" (366 days)

# date_nb_days(100, 150, 2.00) --> "2035-12-26" (7299 days)

# Notes:
# The return format of the date is "YYYY-MM-DD"
# The deposit is always on the "2016-01-01"
# Don't forget to take the rate for a day to be p divided by 36000 since
# banks consider that there are 360 days in a year.
# You have: a0 > 0, p% > 0, a >= a0
################################################################################

# amount of money
# a0=$1
# wanted amount
# a=$2
# percent divided by 360 per day on the 1st of January 2016
# p=$3

date_nb_days() {
    deposit_data="2016-01-01"
    day_counter=0
    while [ $1 -le $2 ]; do

    done
}

date_nb_days 1 5
#TESTS
# date_nb_days 9683 9740 9 # "2016-01-25"
# date_nb_days 2848 2987 7 # "2016-09-03"
# date_nb_days 4289 4420 7 # "2016-06-04"
