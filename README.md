# Life Odyssey

![License: MIT](https://img.shields.io/bower/l/bootstrap?style=flat-square)
![Commit Activity](https://img.shields.io/github/last-commit/jainsid24/neural-network-simulation?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/jainsid24/neural-network-simulation?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Pygame Version](https://img.shields.io/badge/Pygame-2.0.2-red?style=flat-square)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black?style=flat-square)

Life Odyssey is a research project that explores the emergent behaviors of cellular automata. The program allows users to experiment with various rules and initial conditions to see how these affect the growth and evolution of cells on a grid. With the added "zombie mode," players can watch as cells can infect and transform into zombies, adding a new level of complexity and challenge. Life Odyssey offers a visually immersive and engaging experience that is perfect for students, researchers, or anyone interested in the study of complex systems.

---
<p align="center">
    <img src="game.gif" alt="Gameplay" width="200" style="max-width: 100%;"/>
    <img src="zombie.gif" alt="Zombie Mode" width="200" style="max-width: 100%;"/>
    <img src="draw.gif" alt="Draw Mode" width="200" style="max-width: 100%;"/>
</p>
<p align="center">
    <em><b>Gameplay</b> | <b>Zombie Mode</b> | <b>Draw Mode</b></em>
</p>


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Key Bindings](#key-bindings)
   - [Configuration](#configuration)
5. [Code Documentation](#code-documentation)
6. [References](#references)
7. [License](#license)

## Introduction

Cellular Automata is an intriguing concept that involves discrete mathematical models used for modeling and simulating complex systems. It has been used to simulate and model various phenomena across several fields, including physics, biology, and engineering. In recent years, it has gained popularity in computer science and artificial intelligence for simulating complex systems, developing machine learning algorithms, and solving optimization problems. One of the most popular Cellular Automata applications is Conway's Game of Life, which simulates the evolution of a colony of cells and demonstrates the emergence of complex patterns and behaviors.

In this work, a modified version of Conway's Game of Life called **Life Odyssey** is presented, which adds an exciting new twist to the game. In addition to the standard evolution rules, a zombie infection mode has been added, where the live cells can become zombies and infect their neighboring cells. This unique feature adds a new level of complexity and dynamics to the game, where players can observe the spread of the infection and the resulting patterns and behaviors. Life Odyssey has been implemented using Python and Pygame, which provides a visually appealing and interactive environment for the players. The game has several customization options, including the ability to create and edit patterns, adjust the speed and size of the game, and activate the zombie mode.

Life Odyssey can serve as an educational tool for learning cellular automata, and also as an entertaining game for casual players. It can also be used as a research tool for investigating complex systems and phenomena, such as the spread of diseases and the dynamics of social networks.

## Features

* **Zombie Infection Mode** : In addition to the standard evolution rules, live cells can become zombies and infect their neighboring cells, adding a new level of complexity and dynamics to the game.
* **Customizable Patterns** : Players can create and edit patterns using the drawing tool, and use them to explore and observe the dynamics of the game.
* **Adjustable Game Settings** : Life Odyssey provides several customization options, including the ability to adjust the speed and size of the game, and activate the zombie mode.
* **Pulsating Color Scheme** : The game uses a pulsating color scheme that provides a visually appealing and dynamic experience for the players.
* **Educational Tool** : Life Odyssey can serve as an educational tool for learning about cellular automata and complex systems.
* **Research Tool** : Life Odyssey can also be used as a research tool for investigating complex phenomena, such as the spread of diseases and the dynamics of social networks.

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

### Key Bindings

- SPACE - clear the grid
- RETURN - pause/play the game
- g - generate a random glider pattern
- Left Mouse Button - start drawing on the grid (when the game is paused)
- Left Mouse Button Release - stop drawing on the grid (when the game is paused)

### Configuration

The game can be customized by modifying the following parameters in the config.py file:

1. ROWS - the number of rows in the grid
2. COLS - the number of columns in the grid
3. CELL_SIZE - the size of each cell in pixels
4. FPS - the frame rate of the game
5. INFECT_PROBABILITY - the probability of a live cell turning into a zombie (if the zombie mode is enabled)
6. FLIP - the maximum number of cells that can be randomly flipped in one step (if the zombie mode is enabled)
7. SCALE_FACTOR - the maximum scale factor for the pulsating effect
8. ZOMBIE - enable or disable the zombie mode (True or False)
9. The game also supports customization of the color scheme used for drawing the grid. This can be done by modifying the color_scheme dictionary in the config.py file. The dictionary contains three keys: DEAD_COLOR, LIVE_COLOR, and ZOMBIE_COLOR, each representing the RGB values of the corresponding color. The colors can be modified by changing the RGB values to the desired values.

## Code Documentation

[Documentation](https://jainsid24.github.io/life-odyssey/)

## References

[Conway's Game of Life on Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
[The Game of Life - John Horton Conway](https://www.youtube.com/watch?v=R9Plq-D1gEk)

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Want to Contribute?

Check out `CONTRIBUTING.md`.
