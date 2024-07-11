import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

paddle = pygame.Rect(350, 550, 100, 10)
paddle_color = (255, 255, 255)

block_width = 100
block_height = 30
block_color = (255, 0, 0)
blocks = []

for row in range(5):
    for col in range(7):
        block_x = col * (block_width + 10) + 35
        block_y = row * (block_height + 10) + 50
        block = pygame.Rect(block_x, block_y, block_width, block_height)
        blocks.append(block)


ball = pygame.Rect(390, 300, 20, 20)
ball_color = (0, 255, 0)
ball_speed = [4, -4]


game_started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x > 0:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle.x < 700:
        paddle.move_ip(10, 0)
    
    if game_started:
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        if ball.left <= 0 or ball.right >= 800:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]
        
        for block in blocks[:]:
            if ball.colliderect(block):
                blocks.remove(block)
                ball_speed[1] = -ball_speed[1]
                break

        if ball.bottom >= 600:
            pygame.quit()
            sys.exit()
        
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, paddle_color, paddle)

    for block in blocks:
        pygame.draw.rect(screen, block_color, block)
    
    pygame.draw.ellipse(screen, ball_color, ball)

    pygame.display.flip()
    
    clock.tick(60)


