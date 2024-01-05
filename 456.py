import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設定視窗大小和標題
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("簡單的2D遊戲")

# 定義顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 定義角色和障礙物的位置和速度
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = 0
obstacle_speed = 3

# 計分
score = 0
font = pygame.font.Font(None, 36)

# 遊戲主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 控制角色移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 更新角色和障礙物的位置
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    obstacle_y += obstacle_speed

    # 碰撞檢測
    if player_rect.colliderect(obstacle_rect):
        running = False

    # 畫背景和角色
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, 50, 50))

    # 畫障礙物
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # 更新計分
    score += 1
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    # 更新視窗
    pygame.display.update()

    # 控制遊戲速度
    pygame.time.delay(20)

# 退出Pygame
pygame.quit()
sys.exit()
