import pygame
import sys
import random

# 초기 설정
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)  # 흰색 정의 추가

# 색상 정의
BLACK = (0, 0, 0)

# 플레이어 설정
player_size = 50
player_pos = [width // 2, height - 2 * player_size]

# 플레이어 이미지 로드
player_image = pygame.image.load('metal_graymon-removebg-preview.png')
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# 장애물 설정
obstacle_size = 50
obstacle_pos = [width, height - 2 * obstacle_size]
obstacle_speed = 20

# 점프 메커니즘
gravity = 0.8
jump_speed = -13
velocity = 0
is_jumping = False

def detect_collision(player_pos, obstacle_pos):
    p_x, p_y = player_pos
    o_x, o_y = obstacle_pos

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obstacle_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obstacle_size)):
            return True
    return False

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                velocity = jump_speed

    # 플레이어 움직임
    if is_jumping:
        player_pos[1] += velocity
        velocity += gravity
        if player_pos[1] >= height - 2 * player_size:
            player_pos[1] = height - 2 * player_size
            is_jumping = False

    # 장애물 움직임
    obstacle_pos[0] -= obstacle_speed
    if obstacle_pos[0] < 0:
        obstacle_pos[0] = width

    # 충돌 감지
    if detect_collision(player_pos, obstacle_pos):
        game_over = True
        break

    # 그래픽 렌더링
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, WHITE, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

    pygame.display.update()
    clock.tick(30)

    # 화면 그리기
    screen.fill(BLACK)

    # 플레이어 이미지 그리기
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    # 장애물 그리기 (흰색 사용 예시)
    pygame.draw.rect(screen, WHITE, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

    # 화면 업데이트
    pygame.display.update()

    # 프레임 속도 설정
    clock.tick(30)