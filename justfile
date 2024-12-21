set shell := ["fish", "-c"]
set working-directory := '/home/callume/code/AdventOfCode2024'

# fetch the input and open a marimo session for a specific advent day
edit day:
  DAY={{day}} utils/get-input.sh
  marimo edit src/{{day}}.py
