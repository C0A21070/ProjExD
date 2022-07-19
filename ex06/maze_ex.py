import random
import pygame as pg
import maze_maker_ex

class Screen:
    
    def __init__ (self,title,wh):
    
        pg.display.set_caption(title)            #タイトルバー    
        self.sc_sfc=pg.display.set_mode(wh)      #1600*900の画面Surfaceを生成
        self.sc_rct=self.sc_sfc.get_rect()
    
    def blit(self):
        self.sc_sfc.fill((200,200,200))

class Bird:
    
    def __init__(self,kkimg,size,xy):
        self.kk_sfc=pg.image.load(kkimg)                         #Surface
        self.kk_sfc=pg.transform.rotozoom(self.kk_sfc, 0, size) #Surface
        self.kk_rct=self.kk_sfc.get_rect()                      #Rect
        self.kk_rct.center = xy

    def blit(self,scr:Screen):
        scr.sc_sfc.blit(self.kk_sfc,self.kk_rct)

    def update(self,scr):
        key_states=pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]  : self.kk_rct.centery -=100      #Y座標を-
        if key_states[pg.K_DOWN]  : self.kk_rct.centery +=100    #Y座標を+
        if key_states[pg.K_LEFT]  : self.kk_rct.centerx -=100    #X座標を-
        if key_states[pg.K_RIGHT]  : self.kk_rct.centerx +=100   #X座標を+
        if check_bound(self.kk_rct,scr.sc_rct) != (1,1):               #領域外だったら
            if key_states[pg.K_UP] : self.kk_rct.centery +=100       #Y座標を+
            if key_states[pg.K_DOWN] : self.kk_rct.centery -=100     #Y座標を-
            if key_states[pg.K_LEFT] : self.kk_rct.centerx +=100     #X座標を+
            if key_states[pg.K_RIGHT] : self.kk_rct.centerx -=100    #X座標を-
        self.blit(scr)

def main(): #メイン部分の中身
    clock=pg.time.Clock()                       #時間計測用のオブジェクト
    scr=Screen("逃げろ！こうかとん",(1500,900))
    kkt=Bird("fig/6.png",1.0,(100, 100))   #こうかとん
    while True:
        scr.blit()

        for event in pg.event.get():        #イベントを繰り返して処理
            if event.type == pg.QUIT: return    #ウィンドウのXボタンをクリックしたら
        
        kkt.update(scr)

        pg.display.update()
        clock.tick(10)        #1fpsの時を刻む

def check_bound(rct,scr_rct):
    yoko,tate = +1 , +1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom  < rct.bottom : tate = -1
    return (yoko,tate)
"""""

    map = maze_maker_ex.make_maze(width//100, height//100) #一マス100pxになるように調整
    maze_maker_ex.show_maze(canvas, map) 

    goal_pos = goal_p() # ゴール座標を設定しそのマスを赤く上書きする関数を呼ぶ  戻り値はゴール座標
    #print(goal_pos)

    start_p(mx, my) #スタート座標をmx, myから設定し、ライム色で上書きする関数を呼ぶ 引数はmx,my

def start_p(x, y): #渡された座標から
    canvas.create_rectangle(y*100, x*100, y*100+100, x*100+100, 
                            fill="lime") #その座標をライム色の四角形で上書きする

def goal_p(): #
    global map, canvas
    height = len(map) #高さを取得
    #width = len(map[-2])
    end_p=[] #ゴール候補のy座標のリスト
    for i in range(0, height):
        #print(map[i][-2])
        if not map[i][-2]: #そのマスが床なら
            if map[i][-3] + map[i-1][-2] + map[i+1][-2] == 2: #かつ、右側を除く3方のうち、2方が壁なら
                end_p.append(i) # 候補リストに追加
    #print(end_p)
    if len(end_p): #候補が一つでもあれば
        i = random.randint(0,len(end_p)-1) #リストのインデックスをランダムに選び
        #print(i)
        y = end_p[i] # y に代入
    else: #候補がない場合
        for i in range(height): #とりあえず右端から２列目の床のマスにゴールを設定
            if not map[i][-2]:
                y = i
    x = len(map[-2])-2 #x座標を設定
    #print(x, y)
    canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, 
                            fill="red") #ゴールマスを赤色にする
    return(x, y) #設定した座標を返す

def goal(): #ゴールマスに付いたら
    global root
    tkm.showinfo("通知", "ゴールです！おめでとう！\nOKボタンを押してプログラムを終了")
    root.destroy() #rootのmainroopを殺してプログラムを最後まで終える

def main_proc():
    global canvas, mx, my, cx, cy, key, map, goal_pos

    if (mx, my) == goal_pos: #現在座標がゴール座標と同一ならば
        goal() #ゴール時の処理をする関数を呼ぶ
    root.after(100, main_proc)
"""

if __name__ == "__main__":
    main()