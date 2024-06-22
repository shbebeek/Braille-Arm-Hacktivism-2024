import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Robotic Arm Drawing Braille")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Define robotic arm parameters
link_lengths = [100, 75, 50]
joint_angles = [0, 0, 0]

# Function to compute joint positions
def get_joint_positions(angles):
    x = [400]
    y = [300]
    for i in range(len(angles)):
        x.append(x[-1] + link_lengths[i] * math.cos(sum(angles[:i+1])))
        y.append(y[-1] + link_lengths[i] * math.sin(sum(angles[:i+1])))
    return x, y

# Function to draw the robotic arm
def draw_arm(screen, angles):
    x, y = get_joint_positions(angles)
    for i in range(len(x) - 1):
        pygame.draw.line(screen, BLACK, (x[i], y[i]), (x[i+1], y[i+1]), 5)
        pygame.draw.circle(screen, BLACK, (int(x[i+1]), int(y[i+1])), 5)

# Define Braille mapping for all letters
braille_mapping = {
    'a': [(0, 0)],
    'b': [(0, 0), (0, 1)],
    'c': [(0, 0), (1, 0)],
    'd': [(0, 0), (1, 0), (1, 1)],
    'e': [(0, 0), (1, 1)],
    'f': [(0, 0), (0, 1), (1, 0)],
    'g': [(0, 0), (0, 1), (1, 0), (1, 1)],
    'h': [(0, 0), (0, 1), (1, 1)],
    'i': [(0, 1), (1, 0)],
    'j': [(0, 1), (1, 0), (1, 1)],
    'k': [(0, 0), (2, 0)],
    'l': [(0, 0), (0, 1), (2, 0)],
    'm': [(0, 0), (1, 0), (2, 0)],
    'n': [(0, 0), (1, 0), (1, 1), (2, 0)],
    'o': [(0, 0), (1, 1), (2, 0)],
    'p': [(0, 0), (0, 1), (1, 0), (2, 0)],
    'q': [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)],
    'r': [(0, 0), (0, 1), (1, 1), (2, 0)],
    's': [(0, 1), (1, 0), (2, 0)],
    't': [(0, 1), (1, 0), (1, 1), (2, 0)],
    'u': [(0, 0), (2, 0), (2, 1)],
    'v': [(0, 0), (0, 1), (2, 0), (2, 1)],
    'w': [(0, 1), (1, 0), (1, 1), (2, 0), (2, 1)],
    'x': [(0, 0), (1, 0), (2, 0), (2, 1)],
    'y': [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)],
    'z': [(0, 0), (1, 1), (2, 0), (2, 1)],
}

# Function to move arm to draw Braille
def draw_braille_letter(screen, letter, offset=(0, 0)):
    if letter in braille_mapping:
        points = braille_mapping[letter]
        for point in points:
            x, y = point
            # Calculate the position on the screen
            screen_x = 400 + x * 20 + offset[0]
            screen_y = 300 + y * 20 + offset[1]
            pygame.draw.circle(screen, BLACK, (screen_x, screen_y), 5)

# Function to animate the rectangle moving to each point
def animate_rectangle(screen, points, offset=(0, 0)):
    for point in points:
        x, y = point
        # Calculate the position on the screen
        screen_x = 400 + x * 20 + offset[0]
        screen_y = 300 + y * 20 + offset[1]
        pygame.draw.rect(screen, RED, (screen_x - 5, screen_y - 5, 10, 10))
        pygame.display.flip()
        pygame.time.delay(500)  # Delay to simulate movement
        screen.fill(WHITE)
        draw_arm(screen, joint_angles)
        draw_braille_letter(screen, current_letter, offset)

# Main loop
running = True
current_letter = 'a'  # Start with letter 'a'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in braille_mapping:
                current_letter = event.unicode

    # Clear the screen
    window.fill(WHITE)

    # Draw the robotic arm
    draw_arm(window, joint_angles)

    # Draw the current Braille letter
    draw_braille_letter(window, current_letter)

    # Animate the rectangle moving to each point
    animate_rectangle(window, braille_mapping[current_letter])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()