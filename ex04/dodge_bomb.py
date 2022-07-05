from random import randint
import pygame as pg
import sys

def main():
    clock=pg.time.Clock()                       #時間計測用のオブジェクト
    #画面
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバー    
    screen_sfc=pg.display.set_mode((1600,900))      #1600*900の画面Surfaceを生成
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
    #爆弾1
    bmimg_sfc1=pg.Surface((20,20))          #Surface
    bmimg_sfc1.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc1,(255, 0, 0), (10,10), 10)     
    bmimg_rct1=bmimg_sfc1.get_rect()         #Rect
    bmimg_rct1.centerx = randint(0,screen_rct.width)
    bmimg_rct1.centery = randint(0,screen_rct.height)
    vx1,vy1= +1,+1
    #爆弾2
    bmimg_sfc2=pg.Surface((20,20))          #Surface
    bmimg_sfc2.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc2,(0, 0, 255), (10,10), 10)
    bmimg_rct2=bmimg_sfc2.get_rect()         #Rect
    bmimg_rct2.centerx = randint(0,screen_rct.width)
    bmimg_rct2.centery = randint(0,screen_rct.height)
    vx2,vy2= +1,+1

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
            if key_states[pg.K_UP] == True : kk_rct.centery +=1       #Y座標を+1
            if key_states[pg.K_DOWN] == True : kk_rct.centery -=1     #Y座標を-1
            if key_states[pg.K_LEFT] == True : kk_rct.centerx +=1     #X座標を+1
            if key_states[pg.K_RIGHT] == True : kk_rct.centerx -=1    #X座標を-1
        screen_sfc.blit(kk_img,kk_rct)     #画像の表示

        bmimg_rct1.move_ip(vx1,vy1)
        screen_sfc.blit(bmimg_sfc1,bmimg_rct1)        #爆弾1の表示
        yk1,tt1 = check_bound_bomb(bmimg_rct1,screen_rct)
        vx1 *=yk1
        vy1 *=tt1
        if kk_rct.colliderect(bmimg_rct1) : return    #爆弾１の当たり判定

        bmimg_rct2.move_ip(vx2,vy2)
        screen_sfc.blit(bmimg_sfc2,bmimg_rct2)
        yk2,tt2 = check_bound_bomb(bmimg_rct2,screen_rct)  
        vx2 *=yk2
        vy2 *=tt2
        if kk_rct.colliderect(bmimg_rct2) : return     #爆弾２の当たり判定

        pg.display.update()
        clock.tick(1000)        #1000fpsの時を刻む
def check_bound(rct,scr_rct):
    yoko,tate = +1 , +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom  < rct.bottom : tate = -1
    return (yoko,tate)

def check_bound_bomb(rct,scr_rct):
    yoko,tate = +1 , +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1*1.1
    if rct.top < scr_rct.top or scr_rct.bottom  < rct.bottom : tate = -1*1.1
    return (yoko,tate)

if __name__=="__main__":
    pg.init()       #モジュールを初期化
    main()          #ゲームのメイン関数
    pg.init()       #モジュールの初期化を解除
    sys.exit()      #プログラム終了