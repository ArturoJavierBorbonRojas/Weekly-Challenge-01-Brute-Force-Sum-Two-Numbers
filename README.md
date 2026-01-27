# Weekly-Challenge-01-Brute-Force-Sum-Two-Numbers
A python implementation of the "Two Sum" problem using a Brute Force approach. The script generates a random dataset using Numpy and iterates through the list to find two elements that add up to a specific target value.

# Week 1: Two Sum Algorithm brute force

## Description
This project is part of my weekly challenge to explore and explain algorithms using Python.

## How it works
1. Data Generation: It creates a list of 'n' random integers, 'n' is also random.
2. Target Selection: It generates a random objective value.
3. Search logic: It uses nested loops to check every possible pair of numbers until it finds a match.

## Complexity Analysis
1. Time Complexity: O(n^2), because we use a nested loop, an if inside an if. So the execution time grows quadratically with the size of the input.
2. Space Complexity: O(1), we are not using extra data structures to store values during the search.

## Dependencies
Python
Numpy
