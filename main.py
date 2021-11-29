import pygame as pg
import sys


def main():
    pg.init()
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
    print("update Test")
