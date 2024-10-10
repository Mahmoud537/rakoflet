import pygame
import time
import random

pygame.init()

# نعدل حجم الشاشة ليكون مناسب للموبايل
width, height = 320, 480
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game - Mobile Version')

black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

snake_block = 10
snake_speed = 10  # نبطئ السرعة عشان الموبايل

clock = pygame.time.Clock()

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    x, y = width / 2, height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0    
