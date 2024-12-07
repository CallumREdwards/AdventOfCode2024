#!/bin/sh
set -e

# Define the root path
ROOT_PATH=$HOME/code/AdventOfCode2024

# Ensure DAY is set
: "${DAY:?}"

# Create the directory if it doesn't exist
mkdir -p "$ROOT_PATH/data"

# Download the input file and save it to the specified location
curl "https://adventofcode.com/2024/day/${DAY}/input" \
--cookie "session=$(cat $ROOT_PATH/utils/.session)" \
-o "$ROOT_PATH/data/input${DAY}.txt"

