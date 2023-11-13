import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블록 깨기 게임")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# 패들 설정
paddle_width, paddle_height = 80, 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - 30

# 공 설정
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_dx, ball_dy = 5, -5

# 블록 설정
block_width, block_height = 50, 20
block_rows, block_cols = 4, 10
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * (block_width + 5), row * (block_height + 5), block_width, block_height)
        blocks.append(block)

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 8
    paddle_x = max(0, min(width - paddle_width, paddle_x))

    ball_x += ball_dx
    ball_y += ball_dy

    # 벽과의 충돌 처리
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_dx *= -1

    if ball_y - ball_radius <= 0:
        ball_dy *= -1

    # 패들과의 충돌 처리
    if (
        paddle_x <= ball_x <= paddle_x + paddle_width
        and paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height
    ):
        ball_dy *= -1

    # 블록과의 충돌 처리
    for block in blocks:
        if block.colliderect((ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            blocks.remove(block)
            ball_dy *= -1

    # 게임 오버 처리
    if ball_y + ball_radius >= height:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, white)
        screen.blit(text, (width // 2 - 100, height // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, blue, (ball_x, ball_y), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, white, block)

    pygame.display.flip()

    clock.tick(60)