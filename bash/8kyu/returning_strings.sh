#!/bin/bash

################################################################################
# Make a function that will return a greeting statement that uses an input;
# your program should return, "Hello, <name> how are you doing today?".
################################################################################

return_string() {
    echo "'Hello, $1 how are you doing today?'"
}

# TESTS
return_string shell # 'Hello, shell how are you doing today?'
