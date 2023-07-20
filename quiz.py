import pygame
from random import *
#################################################################

#기본 초기화(반드시 해야 하는 것들)
pygame.init()  #초기화 (반드시 필요)


#화면 크기 설정

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")  # 게임 이름

#FPS
clock = pygame.time.Clock()
#################################################################
 
# 1. 사용자 게임 초기화(배경화면 , 게임 이미지, 좌표, 속도 , 폰트 등)
background = pygame.image.load('/Users/jewoonlee/PythonGameWorkSpace/background.png')
character = pygame.image.load('/Users/jewoonlee/PythonGameWorkSpace/character.png')
enemy = pygame.image.load('/Users/jewoonlee/PythonGameWorkSpace/enemy.png')

#캐릭터
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]  #캐릭터의 가로 크기
character_height = character_size[1]    #캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height
character_speed = 0.6

to_x = 0


# 똥
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0]  #캐릭터의 가로 크기
enemy_height = enemy_size[1]    #캐릭터의 세로 크기
enemy_x_pos = randint(0,screen_width-enemy_width)
enemy_y_pos = 0
enemy_spped = 10


start_ticks = pygame.time.get_ticks()

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게이화면의 초당 프레임 수를 설정


   # 2. 이벤트, 처리(키포드 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트?
        if event.type == pygame.QUIT: #창 닫기가 눌러졌는가
            running = False #게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  #캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt


    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 3. 게임 케릭터 위치 정의

    enemy_y_pos += enemy_spped

    #elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    #enemy_y_pos =  elapsed_time * 700
    if enemy_y_pos >= screen_height:
        # start_ticks = pygame.time.get_ticks()
        # elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        enemy_y_pos =  0
        enemy_x_pos = randint(0,screen_width-enemy_width)
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        \

    # 5. 화면에 그리기
    screen.blit(background,(0,0))   #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    pygame.display.update()     #게임화면 다시 그리기


pygame.quit()