import pygame

pygame.init()  #초기화 (반드시 필요)


#화면 크기 설정

screen_width = 480 # 가로 크기
scree_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,scree_height))

#화면 타이틀 설정
pygame.display.set_caption("제운 게임")  # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트?
        if event.type == pygame.QUIT: #창 닫기가 눌러졌는가
            running = False #게임이 진행중이 아님


#pygame 종료
pygame.quit()