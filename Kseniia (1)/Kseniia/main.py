#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
from button import *
from platformerhabrahabr import *
import pygame
from pygame import *


WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
COLOR = (235, 255, 235)
COLOR1 = (3, 64, 3)


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("The best game in your life")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    sc.fill((200, 255, 200))

    font = pygame.font.Font(None, 28)
    text = font.render("Привет! Спасибо, что решил воспользоваться нашей игрой :). ", True, COLOR1)
    place = text.get_rect(center=(400, 120))
    sc.blit(text, place)
    text1 = font.render("Чтобы пройти игру тебе нужно будет найти финиш, обозначенный ", True, COLOR1)
    place1 = text1.get_rect(center=(400, 160))
    sc.blit(text1, place1)
    text2 = font.render("зелёным цветом и добраться до него.", True, COLOR1)
    place2 = text2.get_rect(center=(400, 200))
    sc.blit(text2, place2)
    text2 = font.render("А теперь пора выбрать уровень!", True, COLOR1)
    place2 = text2.get_rect(center=(400, 240))
    sc.blit(text2, place2)
    bt1 = Button()
    button1 = bt1.create_button(screen, Color(COLOR), 125, 300, 150, 150, 50, 'Уровень 1', Color(COLOR1))
    bt2 = Button()
    button2 = bt2.create_button(screen, Color(COLOR), 325, 300, 150, 150, 50, 'Уровень 2', Color(COLOR1))
    bt3 = Button()
    button3 = bt3.create_button(screen, Color(COLOR), 525, 300, 150, 150, 50, 'Уровень 3', Color(COLOR1))
    pygame.display.update()  # обновление и вывод всех изменений на экран
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if 125 <= mouse_pos[0] <= 275 and 300 <= mouse_pos[1] <= 450:
                    level1()
                elif 325 <= mouse_pos[0] <= 475 and 300 <= mouse_pos[1] <= 450:
                    level2()
                elif 525 <= mouse_pos[0] <= 675 and 300 <= mouse_pos[1] <= 450:
                    level3()
            if e.type == QUIT:
                running = False

main()
