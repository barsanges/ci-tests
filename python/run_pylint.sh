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
# Temporary file used to store pylint results:
output='pylint_results'
pylint $module | tee $output
# Searching pylint results for the score:
res=$(grep -oE "^Your code has been rated at "$regex $output | grep -oE $regex)
# Removing temporary output file:
rm $output
# Test if the score is below or above the threshold:
accepted=$(bc <<< "$res >= $threshold")
if [ $accepted = 1 ]; then
    echo "Accepted: pylint score $res above $threshold"
    exit 0 # OK
else
    echo "Rejected: pylint score $res below $threshold"
    exit 1 # Error
fi
