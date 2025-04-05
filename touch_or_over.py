import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gang Man Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont("Arial", 48)

# Clock
clock = pygame.time.Clock()

# Player setup
player = pygame.Rect(100, HEIGHT - 150, 60, 100)
player_speed = 5
is_punching = False
punch_cooldown = 0
PUNCH_DURATION = 10  # frames

# Enemy setup
enemies = []
ENEMY_SPEED = 3
enemy_spawn_delay = 1000  # milliseconds
last_enemy_spawn = pygame.time.get_ticks()

# Game state
game_over = False

def draw_player():
    pygame.draw.rect(screen, RED, player)
    if is_punching:
        punch_rect = pygame.Rect(player.x + player.width, player.y + 30, 30, 20)
        pygame.draw.rect(screen, BLACK, punch_rect)
        return punch_rect
    return None

def spawn_enemy():
    x = random.randint(WIDTH, WIDTH + 100)
    enemy = pygame.Rect(x, HEIGHT - 150, 50, 100)
    enemies.append(enemy)

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, enemy)

def check_collisions(punch_rect):
    global enemies
    if punch_rect:
        enemies = [enemy for enemy in enemies if not punch_rect.colliderect(enemy)]

def show_game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

# Main game loop
while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x = max(player.x - player_speed, 0)
        if keys[pygame.K_RIGHT]:
            player.x = min(player.x + player_speed, WIDTH - player.width)
        if keys[pygame.K_SPACE] and punch_cooldown == 0:
            is_punching = True
            punch_cooldown = PUNCH_DURATION

        # Update punch
        if punch_cooldown > 0:
            punch_cooldown -= 1
        if punch_cooldown == 0:
            is_punching = False

        # Spawn enemies
        now = pygame.time.get_ticks()
        if now - last_enemy_spawn > enemy_spawn_delay:
            spawn_enemy()
            last_enemy_spawn = now

        # Move enemies
        for enemy in enemies:
            enemy.x -= ENEMY_SPEED
            if enemy.colliderect(player):
                game_over = True

        # Draw everything
        punch_rect = draw_player()
        draw_enemies()
        check_collisions(punch_rect)
    else:
        show_game_over()

    pygame.display.flip()
    clock.tick(60)
