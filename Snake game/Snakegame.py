# from turtle import *
# from random import  randrange
# from freegames import square,vector
# food=vector(0,0)
# snake=[vector(10,0)]
# aim=vector(0,-10)
#
# def change(x,y):
#     aim.x=x
#     aim.y=y
#
# def inside(head):
#     return-200<head.x<190 and -200 <head.y < 190
#
#
# def randrage(param, param1):
#     pass
#
#
# def changes(param, param1):
#     pass
#
#
# def move():
#     head=snake[-1].copy()
#     head.move(aim)
#
#     if not inside(head) or head in snake:
#         square(head.xhead,y,9,'red')
#         update()
#         return
#
#     snake.append()
#
#     if head==food:
#         print('snake',len(snake))
#         food.x=randrage(-15,15)*10
#         food.y=randrage(-15,15)*10
#
#     else:
#         snake.pop(0)
#         clear()
#
#         for body in snake:
#             square(food.x,food.y,9,'red')
#             update()
#             ontimer(move,100)
#
#             hideturtle()
#             tracer(False)
#             listen()
#             onkey(lambda:changes(10,0),'Right')
#             onkey(lambda: changes(-10, 0),'left')
#             onkey(lambda: changes(0,10),'Up')
#             onkey(lambda: changes(0, -10),'down')
#         move()
#         done()
#
#
#
# import pygame
# import time
# import random
#
# pygame.init()
#
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# blue = (0, 0, 255)
#
# dis_width = 800
# dis_height = 600
#
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by Edureka')
#
# clock = pygame.time.Clock()
#
# snake_block = 10
# snake_speed = 10
#
# font_style = pygame.font.SysFont(None, 30)
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 3, dis_height / 3])
#
#
# def gameLoop():  # creating a function
#     game_over = False
#     game_close = False
#
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#
#     x1_change = 0
#     y1_change = 0
#
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(white)
#             message("You Lost! Press Q-Quit or C-Play Again", red)
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(white)
#         pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
#         pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
#         pygame.display.update()
#
#         if x1 == foodx and y1 == foody:
#             print("Yummy!!")
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
#
# gameLoop()


import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 9

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()