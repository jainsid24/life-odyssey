import pygame
import random
import math
import numpy as np
from config import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

import math


def create_grid():
    """Create a new grid with random alive/dead cells, and optionally some zombies."""
    # Initialize an empty grid
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    if START_PATTERN == "square":
        # Set all cells inside a square to 1
        side_length = min(ROWS, COLS) // 2
        left = COLS // 2 - side_length // 2
        top = ROWS // 2 - side_length // 2
        for row in range(top, top + side_length):
            for col in range(left, left + side_length):
                grid[row][col] = 1
    elif START_PATTERN == "star":
        # Set all cells inside a star to 1
        radius = min(ROWS, COLS) // 4
        center_row, center_col = ROWS // 2, COLS // 2
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    abs(row - center_row) <= radius / 2
                    or abs(col - center_col) <= radius / 2
                    or abs(row - center_row) + abs(col - center_col) <= radius
                ):
                    grid[row][col] = 1
    elif START_PATTERN == "hex":
        radius = min(ROWS, COLS) // 2
        center_row, center_col = ROWS // 2, COLS // 2
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    abs(row - center_row) + abs(col - center_col / 2) <= radius / 2
                    or abs(col - center_col) <= radius / 2
                ):
                    grid[row][col] = 1
    elif START_PATTERN == "star_thick":
        # Set all cells inside a star with thicker arms to 1
        radius = min(ROWS, COLS) // 4
        center_row, center_col = ROWS // 2, COLS // 2
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    abs(row - center_row) <= radius
                    or abs(col - center_col) <= radius
                    or abs(row - center_row) + abs(col - center_col) <= radius + 1
                ):
                    grid[row][col] = 1
    else:
        # Generate a grid of random values between 0 and 1
        random_grid = np.random.rand(ROWS, COLS)
        # Threshold the random values with the spawn rate to get a grid of 0s and 1s
        grid = np.where(random_grid < SPAWN_RATE, 1, 0)

    if ZOMBIE:
        # Count the number of existing zombies
        num_zombies = np.sum(grid == 2)
        # Spawn new zombies until the desired total is reached
        while num_zombies < MAX_ZOMBIES:
            row, col = np.random.randint(0, ROWS), np.random.randint(0, COLS)
            if grid[row][col] != 2:
                grid[row][col] = 2
                num_zombies += 1
    return grid


def count_neighbors(grid, row, col):
    """Count the number of alive neighbors around a cell."""
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if row + i < 0 or row + i >= ROWS or col + j < 0 or col + j >= COLS:
                continue
            count += grid[row + i][col + j]
    return count


def get_cell_color(row, zombie=False):
    """Get the color for a cell based on the row number."""
    top_color = (60, 173, 100)  # Color for top of the wave
    bottom_color = (52, 152, 219)  # Color for bottom of the wave
    alpha = min(255, max(0, int(255 * (row / ROWS))))  # Opacity based on the row number
    if zombie:
        top_color = (255, 0, 0)
        bottom_color = (255, 255, 0)
    color = (
        int((top_color[0] * alpha + bottom_color[0] * (255 - alpha)) / 255),
        int((top_color[1] * alpha + bottom_color[1] * (255 - alpha)) / 255),
        int((top_color[2] * alpha + bottom_color[2] * (255 - alpha)) / 255),
    )
    return color


def conway_rules(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[row][col] = 0
            elif grid[row][col] == 0 and neighbors == 3:
                new_grid[row][col] = 1
            else:
                new_grid[row][col] = grid[row][col]
    if RANDOM_FLIP:
        randomly_flip_cells(new_grid)
    return new_grid


def update_grid(grid):
    """Update the grid based on the rules of Conway's Game of Life."""
    if ZOMBIE:
        return zombie(grid)
    else:
        return conway_rules(grid)


def darker(color, depth=0.2):
    """Return a darker version of the given color."""
    r, g, b = color
    return int(r * (1 - depth)), int(g * (1 - depth)), int(b * (1 - depth))


def lighter(color, depth=0.2):
    """Return a lighter version of the given color."""
    r, g, b = color
    return (
        int(r + (240 - r) * depth // 2),
        int(g + (240 - g) * depth // 2),
        int(b + (240 - b) * depth // 2),
    )


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WIDTH, y))


def draw_color_scheme(grid, scale_factor, last_grid):
    """Draw the grid on the screen as spheres with a color gradient and a pulsating effect."""
    # Draw the background color gradient
    for y in range(HEIGHT):
        color = interpolate_colors(BACKGROUND_TOP, BACKGROUND_BOTTOM, y / HEIGHT)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    # Draw the cells as 3D circles with the wave pattern and pulsating effect
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] != last_grid[row][col]:
                if grid[row][col] >= 1:
                    if grid[row][col] == 2:
                        color = get_cell_color(row, True)
                    if grid[row][col] == 1:
                        color = get_cell_color(row)
                    size = int(CELL_SIZE + CELL_SIZE * scale_factor)
                    x = col * CELL_SIZE + CELL_SIZE // 2
                    y = row * CELL_SIZE + CELL_SIZE // 2

                    # Draw the circle
                    pygame.draw.circle(screen, color, (x, y), size // 2)

                    # Draw the circle highlight
                    highlight_size = size // 4
                    highlight_color = lighter(color, 0.2)
                    highlight_pos = (x - highlight_size, y - highlight_size)
                    highlight_rect = pygame.Rect(
                        highlight_pos, (highlight_size * 2, highlight_size * 2)
                    )
                    pygame.draw.ellipse(screen, highlight_color, highlight_rect)

                    # Draw the circle shadow
                    shadow_size = size // 4
                    shadow_color = darker(color, 0.2)
                    shadow_pos = (x + shadow_size, y + shadow_size)
                    shadow_rect = pygame.Rect(
                        shadow_pos, (size - shadow_size * 4, size - shadow_size * 4)
                    )
                    pygame.draw.ellipse(screen, shadow_color, shadow_rect)

                    # Draw the specular highlight
                    specular_size = size // 10
                    specular_color = (255, 255, 255)
                    pygame.draw.circle(
                        screen,
                        specular_color,
                        (x - specular_size, y + specular_size),
                        specular_size,
                    )
                else:
                    # Draw a circle for dead cells
                    x = col * CELL_SIZE + CELL_SIZE // 2
                    y = row * CELL_SIZE + CELL_SIZE // 2
                    size = int(CELL_SIZE + CELL_SIZE * scale_factor)
                    color = interpolate_colors(CELL_COLORS[1], (0, 0, 0), 0.5)
                    pygame.draw.circle(screen, color, (x, y), size // 2)

    if GRID:
        draw_grid()
    pygame.display.update()


def interpolate_colors(color1, color2, t):
    """Interpolate between two colors."""
    r = int(color1[0] + (color2[0] - color1[0]) * t)
    g = int(color1[1] + (color2[1] - color1[1]) * t)
    b = int(color1[2] + (color2[2] - color1[2]) * t)
    return (r, g, b)


def create_glider(grid, row, col):
    """Create a glider pattern at the specified row and column."""
    glider = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]
    for i in range(3):
        for j in range(3):
            grid[row + i][col + j] = glider[i][j]
    return grid


def randomly_flip_cells(grid):
    """Randomly flip the states of a few cells on the grid."""
    if FLIP <= 1:
        return
    num_flips = random.randint(1, FLIP)
    for i in range(num_flips):
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLS - 1)
        grid[row][col] = 1 - grid[row][col]


def check_if_neighbor(grid, row, col, cell_type=1):
    return any(
        grid[(row + i) % ROWS][(col + j) % COLS] == cell_type
        for i in range(-1, 2)
        for j in range(-1, 2)
    )


def zombie(grid):
    """Apply the zombie infection rule to the given grid."""
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col] == 0:
                if neighbors >= 3 and check_if_neighbor(grid, row, col, 2):
                    if random.random() < INFECT_PROBABILITY:
                        new_grid[row][col] = 2  # Cell turns into a zombie
                elif neighbors == 3 and not check_if_neighbor(grid, row, col, 2):
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0  # Cell stays dead
            elif grid[row][col] == 1:
                if neighbors < 1 or neighbors > 3:
                    new_grid[row][col] = 0  # Live cell dies
                else:
                    new_grid[row][col] = 1  # Live cell stays alive
            elif grid[row][col] == 2:
                if neighbors == 3 and not check_if_neighbor(grid, row, col, 2):
                    new_grid[row][col] = 0
                else:
                    new_grid[row][col] = 2
    return new_grid


def main():
    """Run the game."""
    grid = create_grid()
    last_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    running = True
    scale_factor = 1
    scale_direction = 1
    zoom_factor = 0.0
    drawing = False
    paused = False
    paused_before_draw = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zoom_factor += 0.1
                elif event.key == pygame.K_DOWN:
                    if zoom_factor > 0:
                        zoom_factor -= 0.1
                elif event.key == pygame.K_0:
                    zoom_factor = 1.0
                elif event.key == pygame.K_SPACE:
                    grid = create_grid()
                elif event.key == pygame.K_RETURN:
                    if not paused_before_draw:
                        paused = not paused
                elif event.key == pygame.K_g:
                    row = random.randint(0, ROWS - 3)
                    col = random.randint(0, COLS - 3)
                    grid = create_glider(grid, row, col)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Start drawing
                    paused_before_draw = paused
                    paused = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    # Stop drawing
                    paused = paused_before_draw
                    paused_before_draw = False
            elif event.type == pygame.MOUSEMOTION:
                if paused and pygame.mouse.get_pressed():
                    # Draw the pattern
                    x, y = event.pos
                    row = y // CELL_SIZE
                    col = x // CELL_SIZE
                    grid[row][col] = 1
                    if ZOMBIE:
                        grid[row][col] = 2
        scaled_width = int(WIDTH * zoom_factor)
        scaled_height = int(HEIGHT * zoom_factor)
        scaled_screen = pygame.transform.scale(screen, (scaled_width, scaled_height))
        screen.blit(
            scaled_screen, ((WIDTH - scaled_width) // 2, (HEIGHT - scaled_height) // 2)
        )
        pygame.display.update()
        if not paused:
            last_grid = grid
            grid = update_grid(grid)
        draw_color_scheme(grid, scale_factor, last_grid)
        # Update the scale factor for the pulsating effect
        scale_factor += 0.025 * scale_direction
        if scale_factor > SCALE_FACTOR or scale_factor < 0:
            scale_direction *= -1
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
