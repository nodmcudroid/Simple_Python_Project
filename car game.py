import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100
ROAD_WIDTH = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load car image
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (CAR_WIDTH, CAR_HEIGHT))

# Car starting position
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 20

# Obstacle properties
obstacle_width, obstacle_height = 50, 100
obstacle_x = random.randint(WIDTH//2 - ROAD_WIDTH//2, WIDTH//2 + ROAD_WIDTH//2 - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > WIDTH//2 - ROAD_WIDTH//2:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < WIDTH//2 + ROAD_WIDTH//2 - CAR_WIDTH:
        car_x += 5
    
    # Move obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(WIDTH//2 - ROAD_WIDTH//2, WIDTH//2 + ROAD_WIDTH//2 - obstacle_width)
    
    # Collision Detection
    if car_x < obstacle_x + obstacle_width and car_x + CAR_WIDTH > obstacle_x and car_y < obstacle_y + obstacle_height and car_y + CAR_HEIGHT > obstacle_y:
        print("Game Over!")
        running = False
    
    # Draw elements
    pygame.draw.rect(screen, BLACK, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
    screen.blit(car, (car_x, car_y))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()