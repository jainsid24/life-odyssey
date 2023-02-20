# Conway's Game of Life in Python

![License: MIT](https://img.shields.io/bower/l/bootstrap?style=flat-square)
![Commit Activity](https://img.shields.io/github/last-commit/jainsid24/neural-network-simulation?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/jainsid24/neural-network-simulation?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Pygame Version](https://img.shields.io/badge/Pygame-2.0.2-red?style=flat-square)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black?style=flat-square)

This is an implementation of Conway's Game of Life in Python using the Pygame library. The program generates a 2D grid of cells, with each cell being either alive or dead. The code then updates the grid based on the rules of Conway's Game of Life, where a cell survives if it has two or three neighbors, and a dead cell comes back to life if it has exactly three neighbors.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
6. [References](#references)
8. [License](#license)

## Introduction

Conway's Game of Life is a cellular automaton developed by British mathematician John Conway in 1970. The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game is played on a two-dimensional grid of square cells, with each cell being in one of two possible states: alive or dead. The cells interact with their eight neighbors, following a set of rules that determine whether they live or die. The game is a popular subject of study in computer science, mathematics, and physics, as it demonstrates how complex behavior can emerge from simple rules.

![Animated GIF](game.gif)

## Installation

- Clone the repository:

```python
git clone https://github.com/username/repository.git
```

- Install the required dependencies:

```python
pip install -r requirements.txt
```

## Usage

To run the program, navigate to the root directory of the project and run the following command:

```python
python game.py
```

The Pygame window will open and the game will start. The program can be stopped by closing the window or pressing Ctrl-C in the terminal.

## References

[Conway's Game of Life on Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
[The Game of Life - John Horton Conway](https://www.youtube.com/watch?v=R9Plq-D1gEk)

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Want to Contribute?

Check out `CONTRIBUTING.md`.