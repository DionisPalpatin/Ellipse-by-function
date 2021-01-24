import pygame as pg
from math import sqrt


try:
    n = int(input())
    size = 800
    step = size // n // 2

    pg.init()
    window = pg.display.set_mode((size, size), pg.SHOWN)
    window.fill((0, 0, 0))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
                
                
        pg.draw.circle(window, (255, 255, 255), (size // 2, size // 2), step, 1)
        for i in range(1, n + 1):
            width_or_height = 2 * step * i
            position_of_corner = size // 2 - step * i
            pg.draw.ellipse(window, (255, 255, 255), (position_of_corner, 0, width_or_height, size), 1)
            pg.draw.ellipse(window, (255, 255, 255), (0, position_of_corner, size, width_or_height), 1)
            
            
        pg.display.update()
        pg.time.delay(10)
        
except:
    print("Unsupported input format")
