import pygame as pg
import sys

def main():
    clock=pg.time.Clock()

    #画面
    pg.display.set_caption("始めてのPygame") #タイトルバー    
    screen=pg.display.set_mode((800,600))    #800*600の画面Surfaceを生成
    #画像
    tori_img=pg.image.load("fig/6.png")       #Surface
    tori_img=pg.transform.rotozoom(tori_img, 0, 2.0) #Surface
    tori_rect=tori_img.get_rect()               #Rect
    tori_rect.center= 700, 400
    screen.blit(tori_img,tori_rect)
    #時間
    
    clock.tick(0.2)     #5秒間表示


if __name__=="__main__":
    pg.init()       #モジュールを初期化
    main()          #ゲームのメイン関数
    pg.init()       #モジュールの初期化を解除
    sys.exit()      #プログラム終了
