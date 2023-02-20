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

<style>#mermaid-1676852247410{font-family:"trebuchet ms",verdana,arial;font-size:16px;fill:#ccc;}#mermaid-1676852247410 .error-icon{fill:#a44141;}#mermaid-1676852247410 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1676852247410 .edge-thickness-normal{stroke-width:2px;}#mermaid-1676852247410 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1676852247410 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1676852247410 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1676852247410 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1676852247410 .marker{fill:lightgrey;}#mermaid-1676852247410 .marker.cross{stroke:lightgrey;}#mermaid-1676852247410 svg{font-family:"trebuchet ms",verdana,arial;font-size:16px;}#mermaid-1676852247410 .label{font-family:"trebuchet ms",verdana,arial;color:#ccc;}#mermaid-1676852247410 .label text{fill:#ccc;}#mermaid-1676852247410 .node rect,#mermaid-1676852247410 .node circle,#mermaid-1676852247410 .node ellipse,#mermaid-1676852247410 .node polygon,#mermaid-1676852247410 .node path{fill:#1f2020;stroke:#81B1DB;stroke-width:1px;}#mermaid-1676852247410 .node .label{text-align:center;}#mermaid-1676852247410 .node.clickable{cursor:pointer;}#mermaid-1676852247410 .arrowheadPath{fill:lightgrey;}#mermaid-1676852247410 .edgePath .path{stroke:lightgrey;stroke-width:1.5px;}#mermaid-1676852247410 .flowchart-link{stroke:lightgrey;fill:none;}#mermaid-1676852247410 .edgeLabel{background-color:hsl(0,0%,34.4117647059%);text-align:center;}#mermaid-1676852247410 .edgeLabel rect{opacity:0.5;background-color:hsl(0,0%,34.4117647059%);fill:hsl(0,0%,34.4117647059%);}#mermaid-1676852247410 .cluster rect{fill:hsl(180,1.5873015873%,28.3529411765%);stroke:rgba(255,255,255,0.25);stroke-width:1px;}#mermaid-1676852247410 .cluster text{fill:#F9FFFE;}#mermaid-1676852247410 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial;font-size:12px;background:hsl(20,1.5873015873%,12.3529411765%);border:1px solid rgba(255,255,255,0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1676852247410:root{--mermaid-font-family:sans-serif;}#mermaid-1676852247410:root{--mermaid-alt-font-family:sans-serif;}#mermaid-1676852247410 flowchart{fill:apa;}</style>
