#!/bin/bash

# Display some kind of help:
if [ $1 = '-h' ]; then
    echo "Usage: run_pylint.sh module threshold"
    echo "Run pylint on a given module and check that the corresponding score is higher than the given threshold."
    exit 0
fi

module=$1
threshold=$2
regex='[0-9]+[\.]?[0-9]*'
# Searching pylint results for the score:
res=$(pylint $module | tee /dev/tty | grep -oE "^Your code has been rated at "$regex $output | grep -oE $regex)
# Test if the score is below or above the threshold:
accepted=$(python -c "print(1 if $res > $threshold else 0)")
if [ $accepted = 1 ]; then
    echo "Accepted: pylint score $res above $threshold"
    exit 0 # OK
else
    echo "Rejected: pylint score $res below $threshold"
    exit 1 # Error
fi
