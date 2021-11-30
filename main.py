import pygame as pg
import sys
import random

class player():
    def __init__(self,px,py):
        self.pic=(pg.image.load("pic/danger.png"),pg.image.load("pic/food.png"),pg.image.load("pic/reuse.png"),pg.image.load("pic/nouse.png"))
        self.rect=(self.pic[0].get_rect(),self.pic[1].get_rect(),self.pic[2].get_rect(),self.pic[3].get_rect())
        self.pics = self.pic[0]
        self.rects = self.rect[0]
        self.posX = px     #x位置
        self.posY = py     #y位置
        self.moveSpeed = 0 #移动速度
    def moveX(self):
        self.posX = self.posX+self.moveSpeed


class monster():
    def __init__(self,px,py):
        self.pic=pg.image.load("pic/monsert.png")
        self.rect=self.pic.get_rect()
        self.posX=px
        self.posY=py
        self.moveSpeed = 4
    def moveX(self):
        self.posX=self.posX+self.moveSpeed
    def moveY(self):
        self.posY=self.posY+self.moveSpeed
    def update(self):
        if self.posX<0 or self.posX>600:
            self.moveSpeed = -self.moveSpeed
        self.moveX()

class rubbish():
    def __init__(self):
        def __init__(self, px, py):
            self.pic = [pg.image.load("pic/t1.png")]
            self.rect = [self.pic[0].get_rect()]
            self.pics = self.pic[0]
            self.rects = self.rect[0]
            self.posX = px
            self.posY = py
            self.moveSpeed = 0
            self.g = 2              #重力
    def drop(self):
        self.posY = self.posY+self.moveSpeed
    def upSpeed(self):
        self.moveSpeed = self.moveSpeed+self.g

def main():
    pg.init()
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)
    background = pg.image.load("pic/background.png")
    backrect = background.get_rect()        #创建背景

#--------------------这里测试单人运行模式---------------------#

    rubbishs=[]    #垃圾列表

    mosterTest = monster(0,0)
    playerTest = player(0,480)

    clock = pg.time.Clock()  #计时器

    while True:
        clock.tick(60)
        screen.blit(background, backrect)
        screen.blit(playerTest.pics,(playerTest.posX,playerTest.posY))
        screen.blit(mosterTest.pic,(mosterTest.posX,mosterTest.posY))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    playerTest.pics = playerTest.pic[0]
                    playerTest.rects = playerTest.rect[0]
                if event.key == pg.K_2:
                    playerTest.pics = playerTest.pic[1]
                    playerTest.rects = playerTest.rect[1]
                if event.key ==pg.K_3:
                    playerTest.pics = playerTest.pic[2]
                    playerTest.rects = playerTest.rect[2]
                if event.key == pg.K_4:
                    playerTest.pics = playerTest.pic[3]
                    playerTest.rects = playerTest.rect[3]
                if event.key == pg.K_RIGHT:
                    playerTest.moveSpeed=5
                if event.key == pg.K_LEFT:
                    playerTest.moveSpeed=-5
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    if playerTest.moveSpeed==5:
                        playerTest.moveSpeed=0
                if event.key == pg.K_LEFT:
                    if playerTest.moveSpeed==-5:
                        playerTest.moveSpeed=0
        if playerTest.posX < 0:
            playerTest.moveSpeed = 0
            playerTest.posX=0
        if playerTest.posX > 722:
            playerTest.moveSpeed = 0
            playerTest.posX=722
        playerTest.moveX()      #移动对象
        mosterTest.update()
        pg.display.flip()


if __name__ == '__main__':
    main()
    print("update Test")
