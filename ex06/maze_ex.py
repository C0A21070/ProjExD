import pygame as pg
import random
import sys
import maze_maker

class Screen:
    def __init__(self, title: str, wh: tuple, image: str) :
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.x_count = wh[0]//100
        self.y_count = wh[1]//100

        self.map_init(self.sfc, self.x_count, self.y_count, wh)

    def blit(self):
        self.sfc.fill((255,255,255))
        self.s_tile_blit()     #特殊マスの描写
        pass
        self.map_blit()

    def map_init(self, base_obj, x:int, y:int, wh:tuple) -> None:
        self.map_ary = maze_maker.make_maze(x, y)
        
        self.x_size = round(wh[0]/x)
        self.y_size = round(wh[1]/y)
        self.b_color = ( 150, 150, 150)

        self.map_ary[1][1]=2  #スタート地点
        self.s_color = ( 255, 0, 0)

        goal_pos = self.goal_p()   #ゴール地点
        self.map_ary[goal_pos[1]][goal_pos[0]] = 3
        self.g_color = (0,  255,  255)

        self.block_lst = list()
        self.s_tile_lst = list() #superなtileのリスト
        #for i in self.map_ary:
        #    print(i)
        
        for i in range(len(self.map_ary)):
            for j in range(len(self.map_ary[i])):
                if self.map_ary[i][j]==1:
                    self.block_lst.append(Block(self.b_color, self.x_size, self.y_size, (j, i), self.sfc))
                elif self.map_ary[i][j]==2:   #スタートなら
                    self.block_lst.append(Block(self.s_color, self.x_size, self.y_size, (j, i), self.sfc))
                elif self.map_ary[i][j] == 3: #ゴールなら
                    self.s_tile_lst.append(Block(self.g_color, self.x_size, self.y_size, (j, i), self.sfc)) 
        pg.display.update()

    def map_blit(self):
        for i in self.block_lst:
            i.blit(self.sfc)

    def s_tile_blit(self):#特殊なタイルを描写.
        for i in self.s_tile_lst:
            i.blit(self.sfc)
    
    def goal_p(self):
        height = len(self.map_ary) #高さを取得
        end_p=[] #ゴール候補のy座標のリスト
        for i in range(0, height):
            if not self.map_ary[i][-2]: #そのマスが床なら
                if self.map_ary[i][-3] + self.map_ary[i-1][-2] + self.map_ary[i+1][-2] == 2: #かつ、右側を除く3方のうち、2方が壁なら
                    end_p.append(i) # 候補リストに追加
        #print(end_p)
        if len(end_p): #候補が一つでもあれば
            i = random.randint(0,len(end_p)-1) #リストのインデックスをランダムに選び
            #print(i)
            y = end_p[i] # y に代入
        else: #候補がない場合
            for i in range(height): #とりあえず右端から２列目の床のマスにゴールを設定
                if not self.map_ary[i][-2]:
                    y = i
        x = len(self.map_ary[-2])-2 #x座標を設定
        return(x, y) #設定した座標を返す

class Block:
    def __init__(self, color, x_size, y_size, xy, base_obj:Screen):
        self.x_size = x_size
        self.y_size = y_size

        self.sfc = pg.Surface((self.x_size, self.y_size)) 
        self.rct = self.sfc.get_rect()

        pg.draw.rect(self.sfc, color, (0,0,self.x_size, self.y_size))
        self.rct = self.sfc.get_rect() 
        self.rct.centerx = xy[0] * x_size + x_size/2
        self.rct.centery = xy[1] * y_size + y_size/2

    def blit(self, base_obj):
        base_obj.blit(self.sfc, self.rct)
        pass


class Bird:
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom_rate)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, base_obj: Screen):
        base_obj.sfc.blit(self.sfc, self.rct)
    
    def update(self, base_obj: Screen, map_ary):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] : 
            self.rct.centery -= base_obj.y_size
        if key_states[pg.K_DOWN] : 
            self.rct.centery += base_obj.y_size
        if key_states[pg.K_LEFT] : 
            self.rct.centerx -= base_obj.x_size
        if key_states[pg.K_RIGHT] : 
            self.rct.centerx += base_obj.x_size
        if collision_detect(self.rct, base_obj.block_lst) or check_bound(self.rct, base_obj.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: self.rct.centery += base_obj.y_size
            if key_states[pg.K_DOWN]  == True: self.rct.centery -= base_obj.y_size
            if key_states[pg.K_LEFT]  == True: self.rct.centerx += base_obj.x_size
            if key_states[pg.K_RIGHT] == True: self.rct.centerx -= base_obj.x_size
        self.blit(base_obj)
        
class Enemy(Bird):
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        super().__init__(image, zoom_rate, xy)
    
    def update(self, base_obj: Screen, map_obj):
        #if
        pass


class main: # mainをクラスに。
    def __init__(self) -> None: #main の main。Javaでいうpublic static void main(String args[]){}なとこ。
        clock = pg.time.Clock()

        scr = Screen("戦え！こうかとん", (1500, 900), "fig/pg_bg.jpg")
        bird = Bird("fig/6.png", 1.5, (scr.x_size+scr.y_size//2, scr.y_size+scr.y_size//2))
        #enemy = Enemy("fig/s_exp.png", 1.5, (50,50))
        
        while True:
            bird.blit(scr)
            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    return
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN or event.key == pg.K_UP or event.key == pg.K_LEFT or event.key==pg.K_RIGHT:
                        bird.update(scr, scr.map_ary)
            #enemy.update(scr, scr.map_ary)
            pg.display.update()
            clock.tick(1000)
            scr.blit()

    def game_over(self, base_obj: Screen): #接触時に実行
        font = pg.font.Font(None, 80)
        self.sfc = font.render(str("GAME OVER"), True, (255,0,0))
        self.rct = self.sfc.get_rect()
        self.rct.center = base_obj.rct.width/2,base_obj.rct.height/2
        base_obj.sfc.blit(self.sfc,self.rct) #文言を表示
        pg.display.update()
        while True: #バッテンが押されるまで無限ループ
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

def collision_detect(rct, block_rct:list):
    bool = False
    for b in block_rct:
        if rct.colliderect(b.rct) == True:
            print("True")
            bool = True
            break
        else :
            print("False")
    return bool
# 練習7
def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
"""
if __name__ == "__main__":
    main()
"""