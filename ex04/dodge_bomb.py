import pygame as pg
import sys

def main():
    clock=pg.time.Clock()                       #時間計測用のオブジェクト
    
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバー    
    screen_sfc=pg.display.set_mode((1600,900))      #1400*800の画面Surfaceを生成

    bg_img=pg.image.load("pg_bg.jpg")           #Surface
    bg_rect=bg_img.get_rect()                   #Rect
    screen_sfc.blit(bg_img,bg_rect) 
    
    tori_img=pg.image.load("fig/6.png")       #Surface
    tori_img=pg.transform.rotozoom(tori_img, 0, 2.0) #Surface
    tori_rect=tori_img.get_rect()               #Rect
    tori_rect.center= 900, 400

    while True:
        screen_sfc.blit(bg_img,bg_rect) 
        screen_sfc.blit(tori_img,tori_rect)
        for event in pg.event.get():        #イベントを繰り返して処理
            if event.type == pg.QUIT: return    #ウィンドウのXボタンをクリックしたら
        pg.display.update()
        clock.tick(1000)        #1000fpsの時を刻む

if __name__=="__main__":
    pg.init()       #モジュールを初期化
    main()          #ゲームのメイン関数
    pg.init()       #モジュールの初期化を解除
    sys.exit()      #プログラム終了