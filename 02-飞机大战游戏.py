import pygame
import time
from pygame.locals import *
# 导入所有按键
# from time import sleep
# 英雄飞机坐标
hero_x = 150
hero_y = 600
#子弹
bullet_list = []
#  敌机坐标
enemy_x = 150
enemy_path = "left"
# 敌机是否存活
enemy_life = "live"
# 爆炸效果图
a = pygame.image.load("./feiji/enemy2_down1.png")
b = pygame.image.load("./feiji/enemy2_down2.png")
c = pygame.image.load("./feiji/enemy2_down3.png")
d = pygame.image.load("./feiji/enemy2_down4.png")
# 计数
num = 0
num_list = [a, b, c ,d]
def hero_plane(screen, hero, bullet):
    global hero_x
    global hero_y
    screen.blit(hero, (hero_x, hero_y))
    for envet in pygame.event.get():
        if envet.type == QUIT:
            exit()
        elif envet.type == KEYDOWN:
            if envet.key == K_DOWN:
                hero_y += 10
            elif envet.key == K_UP:
                hero_y -= 10
            elif envet.key == K_LEFT:
                hero_x -= 10
            elif envet.key == K_RIGHT:
                hero_x += 10
            elif envet.key == K_SPACE:
                bullet_list.append({"x": hero_x + 39, "y": hero_y})
    # 让子弹飞一会
    for i in bullet_list:
        screen.blit(bullet, (i["x"], i["y"]))
        i["y"] -= 10
    # print(bullet_list)

def enemy_plane(screen, enemy):
    global enemy_x
    global enemy_path, enemy_life, num
    if enemy_life == "live":
        screen.blit(enemy, (enemy_x, 0))
        # enemy_x += 10
        if enemy_path == "left":
            enemy_x -= 10
            if enemy_x <= 0:
                enemy_path = "right"
        elif enemy_path == "right":
            enemy_x += 10
            if enemy_x >= 250:
                enemy_path = "left"
        for i in bullet_list:
            if (i["x"] >= enemy_x and i["x"] - enemy_x > -50) and (i["y"] >= 0 and i["y"] <= 200):
                enemy_life = "dead"
    elif enemy_life == "dead":
        if num < 4:
            screen.blit(num_list[num], (enemy_x, 0))
            num += 1


def main():
    """显示游戏窗口及控制流程"""
    # display创建窗口
    screen = pygame.display.set_mode((400, 800), 0, 32)
    # 创建背景
    back_ground = pygame.image.load("./feiji/background.png")
    hero = pygame.image.load("./feiji/hero1.png")
    bullet = pygame.image.load("./feiji/bullet.png")
    enemy = pygame.image.load("./feiji/enemy2_n2.png")



    while True:
        # 把图片加载到窗口上
        screen.blit(back_ground, (0, 0))
        hero_plane(screen, hero, bullet)
        enemy_plane(screen, enemy)


        # 数据更新
        pygame.display.update()
        # mac加一下
        pygame.event.get()
        # 时间暂停
        time.sleep(0.1)



if __name__ == '__main__':
    main()