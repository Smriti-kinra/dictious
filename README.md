# DICTious — Dictionary Rank Finder

A Python CLI tool that calculates the lexicographic (dictionary) rank of a given word, accounting for duplicate characters.

## Features

- Computes dictionary rank of any valid word
- Handles repeated characters correctly
- Simple and clean command-line interface
- Input validation for better usability

## How It Works

The program calculates how many permutations of the word would appear before it in dictionary order using:

- Factorial-based permutation counting
- Frequency adjustment for duplicate characters

## Requirements

- Python 3.x

## Usage

Run the program:

bash python dictious.py 

Enter a word when prompted, and the program will display its rank.

## Example

Enter a word: banana Rank: 35

## Project Structure

dictious.py README.md

## Future Improvements

- GUI version
- Web-based interface
- Performance optimization for large inputs

## License

This project is open-source and free to use.
