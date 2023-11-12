## Requirements

- Python 3.x
- Matplotlib library
- Bitarray library

## Getting Started

1. Clone the repository.
2. Install the required libraries using `pip install matplotlib bitarray`.
3. Run `collatz_runner.py` to generate the Collatz sequence and visualize it.

Feel free to explore and fork the code to suit your specific requirements. Code in this repository was written by myself; though, much of the documentation was written by ChatGPT.

# collatz_generator.py

The `collatz_generator.py` file contains the implementation of the `CollatzGenerator` class and the `CollatzMember` class. These classes represent the generator and individual members of the Collatz sequence, respectively.

## CollatzMember Class

The `CollatzMember` class represents an individual member of the Collatz sequence. It contains properties and methods for handling the value, distance, bit array, and relationships with other members.

## CollatzGenerator Class

The `CollatzGenerator` class generates the Collatz sequence and provides methods for writing sequence information to a file and creating 2D and 3D line graphs to visualize the sequence.

## Visualizations

The script provides two types of visualizations:

- **2D Line Graph:** Plots the distance from 1 on the x-axis and the corresponding values on the y-axis.
  
- **3D Line Graph:** Plots the distance from 1 on the x-axis, the decimal values on the y-axis, and the integer values of Collatz codes on the z-axis.


# Collatz Sequence Generator

## Overview

This Python program generates and explores the Collatz sequence, a mathematical sequence defined by the following rules:

1. Start with any positive integer.
2. If the current number is even, divide it by 2.
3. If the current number is odd, triple it and add 1.
4. Repeat the process indefinitely.

This progam produces collatz codes for each CollatzMember. A collatz code is an array of bits that represents the steps to generate a collatz number. In this implementation, 0 represents rule 2 above and 1 represents rule 3 above.

The program consists of two files:

1. **collatz_runner.py**: The main script that utilizes the CollatzGenerator class to generate and analyze the Collatz sequence.
2. **collatz_generator.py**: The implementation of the CollatzGenerator class and the CollatzMember class, which represents individual members of the sequence.

