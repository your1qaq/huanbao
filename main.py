import pygame as pg
import sys
import random

class player():
    def __init__(self,px,py):
        self.pic=(pg.image.load("pic/danger.png"),pg.image.load("pic/food.png"),pg.image.load("pic/reuse.png"),pg.image.load("pic/nouse.png"))
        self.rect=(self.pic[0].get_rect(),self.pic[1].get_rect(),self.pic[2].get_rect(),self.pic[3].get_rect())
        self.pics = self.pic[0]
        self.rects = self.rect[0]
        self.type = 0     #垃圾桶类型
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
    def __init__(self, px, py,type = 0):
        self.pic = [pg.image.load("pic/t1.png")]
        self.rect = [self.pic[type].get_rect()]
        self.pics = self.pic[type]
        self.rects = self.rect[type]
        self.type = type
        self.posX = px
        self.posY = py
        self.moveSpeed = 0
        self.g = 1  # 重力
        self.cheek = True          #判断是不是检测过

    def drop(self):
        self.upSpeed()
        self.posY = self.posY+self.moveSpeed
    def upSpeed(self):
        self.moveSpeed = self.moveSpeed+self.g
    def isFinish(self,player):                      #判断是否得分
        global score
        global wrong
        global lost
        if self.posY>=480 and self.cheek:
            if self.posX>=player.posX and self.posX<=(player.posX+79):
                if self.type == player.type:
                    score+=1
                    self.cheek = False
                if self.type != player.type:
                    wrong+=1
                    self.cheek = False
            else:
                lost+=1
                self.cheek = False

#-----------------分数显示----------------------
score = 0      #得分
lost = 0       #丢分
wrong = 0      #错误分类

def main():
    pg.init()
    size = width, height = 800, 600
    screen = pg.display.set_mode(size)
    background = pg.image.load("pic/background.png")
    backrect = background.get_rect()        #创建背景

    font = pg.font.Font('freesansbold.ttf', 32)

    def show_score():                   #显示分数
        text = f''' scores:{score} 
                    lost:{lost}
                    wrong:{wrong}'''
        sco_render = font.render(text, True, (255, 255, 255))
        screen.blit(sco_render, (10, 10))

#--------------------这里测试单人运行模式---------------------#

    rubbishs=[]    #垃圾列表

    mosterTest = monster(0,0)   #怪物
    playerTest = player(0,480)  #玩家

    clock = pg.time.Clock()  #计时器

    ADD_RUBISH = pg.USEREVENT
    pg.time.set_timer(ADD_RUBISH,1500)  #自定义时间，每1.5秒添加一个垃圾

    while True:
        clock.tick(60)
        screen.blit(background, backrect)
        for rub in rubbishs:
            screen.blit(rub.pics,(rub.posX,rub.posY))
        screen.blit(playerTest.pics,(playerTest.posX,playerTest.posY))
        screen.blit(mosterTest.pic,(mosterTest.posX,mosterTest.posY))
        show_score()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    playerTest.pics = playerTest.pic[0]
                    playerTest.rects = playerTest.rect[0]
                    playerTest.type=0
                if event.key == pg.K_2:
                    playerTest.pics = playerTest.pic[1]
                    playerTest.rects = playerTest.rect[1]
                    playerTest.type=1
                if event.key ==pg.K_3:
                    playerTest.pics = playerTest.pic[2]
                    playerTest.rects = playerTest.rect[2]
                    playerTest.type=2
                if event.key == pg.K_4:
                    playerTest.pics = playerTest.pic[3]
                    playerTest.rects = playerTest.rect[3]
                    playerTest.type=3
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
            if event.type == ADD_RUBISH:
                rubbishs.append(rubbish(int(mosterTest.posX),int(mosterTest.posY)))
        if playerTest.posX < 0:
            playerTest.moveSpeed = 0
            playerTest.posX=0
        if playerTest.posX > 722:
            playerTest.moveSpeed = 0
            playerTest.posX=722
        playerTest.moveX()      #移动对象
        mosterTest.update()     #怪物移动
        for rub in rubbishs:
            rub.drop()
            rub.isFinish(playerTest)
            if rub.posY>600:
                rubbishs.remove(rub)
        pg.display.flip()       #刷新


if __name__ == '__main__':
    main()
    print("update Test")
