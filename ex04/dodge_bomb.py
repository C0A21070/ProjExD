from random import randint
import pygame as pg
import sys

def main():
    clock=pg.time.Clock()                       #時間計測用のオブジェクト
    #画面
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバー    
    screen_sfc=pg.display.set_mode((1600,900))      #1400*800の画面Surfaceを生成
    screen_rct=screen_sfc.get_rect()
    #背景
    bg_img=pg.image.load("pg_bg.jpg")           #Surface
    bg_rect=bg_img.get_rect()                   #Rect
    screen_sfc.blit(bg_img,bg_rect) 
    #画像
    kk_img=pg.image.load("fig/6.png")       #Surface
    kk_img=pg.transform.rotozoom(kk_img, 0, 2.0) #Surface
    kk_rct=kk_img.get_rect()               #Rect
    kk_rct.center = 900, 400
    #爆弾
    bmimg_sfc=pg.Surface((20,100))          #Surface
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255, 0, 0), (10,10), 10)
    bmimg_rct=bmimg_sfc.get_rect()         #Rect
    bmimg_rct.centerx = randint(0,screen_rct.width)
    bmimg_rct.centery = randint(0,screen_rct.height)
    vx,vy= +1,+1

    while True:
        screen_sfc.blit(bg_img,bg_rect)         #背景の表示
        #イベント
        for event in pg.event.get():        #イベントを繰り返して処理
            if event.type == pg.QUIT: return    #ウィンドウのXボタンをクリックしたら
        #
        key_states=pg.key.get_pressed() #辞書
        if key_states[pg.K_UP] == True : kk_rct.centery -=1       #Y座標を-1
        if key_states[pg.K_DOWN] == True : kk_rct.centery +=1     #Y座標を+1
        if key_states[pg.K_LEFT] == True : kk_rct.centerx -=1     #X座標を-1
        if key_states[pg.K_RIGHT] == True : kk_rct.centerx +=1    #X座標を+1
        if check_bound(kk_rct,screen_rct) != (1,1):               #領域外だったら
            if key_states[pg.K_UP] == True : kk_rct.centery -=1       #Y座標を-1
            if key_states[pg.K_DOWN] == True : kk_rct.centery +=1     #Y座標を+1
            if key_states[pg.K_LEFT] == True : kk_rct.centerx -=1     #X座標を-1
            if key_states[pg.K_RIGHT] == True : kk_rct.centerx +=1    #X座標を+1
        screen_sfc.blit(kk_img,kk_rct)     #画像の表示

        bmimg_rct.move_ip(vx,vy)
        screen_sfc.blit(bmimg_sfc,bmimg_rct)        #爆弾の表示
        yk,tt = check_bound(bmimg_rct,screen_rct)
        vx *=yk
        vy *=tt

        if kk_rct.colliderect(bmimg_rct) : return

        pg.display.update()
        clock.tick(1000)        #1000fpsの時を刻む
def check_bound(rct,scr_rct):
    yoko,tate = +1 , +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom  < rct.bottom : tate = -1
    return (yoko,tate)
if __name__=="__main__":
    pg.init()       #モジュールを初期化
    main()          #ゲームのメイン関数
    pg.init()       #モジュールの初期化を解除
    sys.exit()      #プログラム終了