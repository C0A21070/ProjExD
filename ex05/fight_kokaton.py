from random import randint
import pygame as pg
import sys

class Screen:
    
    def __init__ (self,title,wh,bgimage):
    
        pg.display.set_caption(title)            #タイトルバー    
        self.sc_sfc=pg.display.set_mode(wh)      #1600*900の画面Surfaceを生成
        self.sc_rct=self.sc_sfc.get_rect()
        self.bg_sfc=pg.image.load(bgimage)       #Surface
        self.bg_rct=self.bg_sfc.get_rect()       #Rect
    
    def blit(self):
        self.sc_sfc.blit(self.bg_sfc,self.bg_rct)

class Bird:
    
    def __init__(self,kkimg,size,xy):
        self.kk_sfc=pg.image.load(kkimg)                         #Surface
        self.kk_sfc=pg.transform.rotozoom(self.kk_sfc, 0, size) #Surface
        self.kk_rct=self.kk_sfc.get_rect()                      #Rect
        self.kk_rct.center = xy

    def blit(self,scr:Screen):
        scr.sc_sfc.blit(self.kk_sfc,self.kk_rct)     #画像の表示
    
    def update(self,scr):
        key_states=pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]  : self.kk_rct.centery -=5       #Y座標を-2
        if key_states[pg.K_DOWN]  : self.kk_rct.centery +=5     #Y座標を+2
        if key_states[pg.K_LEFT]  : self.kk_rct.centerx -=5     #X座標を-2
        if key_states[pg.K_RIGHT]  : self.kk_rct.centerx +=5    #X座標を+2
        if check_bound(self.kk_rct,scr.sc_rct) != (1,1):               #領域外だったら
            if key_states[pg.K_UP] : self.kk_rct.centery +=5       #Y座標を+2
            if key_states[pg.K_DOWN] : self.kk_rct.centery -=5     #Y座標を-2
            if key_states[pg.K_LEFT] : self.kk_rct.centerx +=5     #X座標を+2
            if key_states[pg.K_RIGHT] : self.kk_rct.centerx -=5    #X座標を-2
        self.blit(scr)

class Bomb:
    
    def __init__(self,color,size,vxy,scr:Screen):
        self.bmimg_sfc1=pg.Surface((2*size,2*size))          #Surface
        self.bmimg_sfc1.set_colorkey((0,0,0))
        pg.draw.circle(self.bmimg_sfc1,color,(size,size),size)     
        self.bmimg_rct1=self.bmimg_sfc1.get_rect()         #Rect
        self.bmimg_rct1.centerx = randint(0,scr.sc_rct.width)
        self.bmimg_rct1.centery = randint(0,scr.sc_rct.height)
        self.vx1,self.vy1= vxy
    
    def bilt(self,scr):
        scr.sc_sfc.blit(self.bmimg_sfc1,self.bmimg_rct1)   #爆弾1の表示 

    def update(self,scr):
        self.bmimg_rct1.move_ip(self.vx1,self.vy1)
        yk1,tt1 = check_bound_bomb(self.bmimg_rct1,scr.sc_rct)
        self.vx1 *=yk1
        self.vy1 *=tt1
        self.bilt(scr)


"""
class Shot:
    def __init__(self,chr:Bird):
        self.sfc=pg.image.load("")                         #Surface
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.1) #Surface
        self.rct=self.kk_sfc.get_rect()                      #Rect
        self.rct.midleft = chr.rct.center
    
    def bilt(self,scr:Screen):
        scr.sc_sfc.blit(self.sfc,self.rct)
    
    def updata(self,scr:Screen):
        self.rct.move_ip(+1,0)
        if check_bound(self.rct,scr.bg_rct) != (1,1):
            del self
        self.bilt(scr)
"""

def main():
    clock=pg.time.Clock()                       #時間計測用のオブジェクト
    
    scr=Screen("逃げろ！こうかとん",(1600,900),"fig/pg_bg.jpg")     #画面

    kkt=Bird("fig/6.png",2.0,(900, 400))   #こうかとん

    bkd1=Bomb((255, 0, 0),10,(+1,+1),scr)   #爆弾1  
    bkd2=Bomb((0, 0, 255),10,(+1,+1),scr)   #爆弾2
    bkd3=Bomb((0, 255, 255),10,(+1,+1),scr) #爆弾3

    #beam = None

    while True:
        scr.blit()

        #イベント
        for event in pg.event.get():        #イベントを繰り返して処理
            if event.type == pg.QUIT: return    #ウィンドウのXボタンをクリックしたら
            if event.type == pg.KEYDOWN and event.key == pg.K_r:    #Rを押すと再描画がされる
                kkt=Bird("fig/6.png",2.0,(900, 400))            
                bkd1=Bomb((255, 0, 0),10,(+1,+1),scr)
                bkd2=Bomb((0, 0, 255),10,(+1,+1),scr)
                bkd3=Bomb((0, 255, 255),10,(+1,+1),scr)
            #if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            #    beam = kkt.attack()
        
        kkt.update(scr)
        bkd1.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)
        #if beam:
        #    beam.updata(scr)
        
        if kkt.kk_rct.colliderect(bkd1.bmimg_rct1) : return    #爆弾1の当たり判定
        if kkt.kk_rct.colliderect(bkd2.bmimg_rct1) : return    #爆弾2の当たり判定
        if kkt.kk_rct.colliderect(bkd3.bmimg_rct1) : return    #爆弾3の当たり判定

        pg.display.update()
        clock.tick(1000)        #1000fpsの時を刻む

def check_bound(rct,scr_rct):
    yoko,tate = +1 , +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom  < rct.bottom : tate = -1
    return (yoko,tate)
def check_bound_bomb(rct,scr_rct):
    yoko,tate = +1 , +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1*1.3
    if rct.top < scr_rct.top or scr_rct.bottom  < rct.bottom : tate = -1*1.3
    return (yoko,tate)

if __name__=="__main__":
    pg.init()       #モジュールを初期化
    main()          #ゲームのメイン関数
    pg.init()       #モジュールの初期化を解除
    sys.exit()      #プログラム終了