import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global cx,cy
    if key=="Up":cy-=20    
    elif key=="Down":cy+=20    
    elif key=="Left":cx-=20
    elif key=="Right":cx+=20    
    canvas.coords("tori",cx,cy)
    root.after(5,main_proc)

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
    cx,cy=300,400
    canvas.create_image(cx,cy,image=tori,tag="tori")
    
    #キー入力
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    root.after(5,main_proc)

    root.mainloop()