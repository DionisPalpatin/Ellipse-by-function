import pygame as pg
from math import sqrt, ceil

size = 800
try:
    n = int(input())
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
            pg.draw.ellipse(window, (255, 255, 255), (size // 2 - step * i, 0, 2 * step * i, size), 1)
            pg.draw.ellipse(window, (255, 255, 255), (0, size // 2 - step * i, size, 2 * step * i), 1)
            
            
        pg.display.update()
        pg.time.delay(10)
        
except:
    print("Unsupported input format")
