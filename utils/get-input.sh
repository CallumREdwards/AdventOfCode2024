#!/bin/sh
set -e

# Ensure DAY is set
: "${DAY:?}"

# Create the directory if it doesn't exist
mkdir -p "../data/${DAY}"

# Download the input file and save it to the specified location
curl "https://adventofcode.com/2024/day/${DAY}/input" \
--cookie "session=$(cat ~/code/AdventOfCode2024/utils/.session)" \
-o "../data/${DAY}/input.txt"

