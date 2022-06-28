import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global cx,cy,mx,my
    if key=="Up":my-=1    
    elif key=="Down":my+=1    
    elif key=="Left":mx-=1
    elif key=="Right":mx+=1
    cx,cy=mx*100+50,my*100+50    
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__=="__main__":
    #タイトル
    root=tk.Tk()
    root.title("迷えるこうかとん")
    
    #Canvasの生成
    canvas=tk.Canvas(root,height=900,width=1500,bg="black")
    canvas.pack()
    
    #迷路の生成
    maze_mk=mm.make_maze(15,9)
    mm.show_maze(canvas,maze_mk)
    
    #こうかとんの描写
    tori=tk.PhotoImage(file="fig/5.png")
    mx,my=1,1
    canvas.create_image(mx,my,image=tori,tag="tori")
    
    #キー入力
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    root.after(100,main_proc)

    root.mainloop()