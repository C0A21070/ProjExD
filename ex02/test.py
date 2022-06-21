import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.title("おためし")
root.geometry("500x200")

label=tk.Label(root,
                text="らべるを書いた",
                font=("Ricty Diminished",20)
                )
label.pack()

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")
    
button=tk.Button(root,text="押すな")
button.bind("<1>", button_click)
button.pack()

entry=tk.Entry(root,width=30)
entry.insert(tk.END,"fugapiyo")
entry.pack()

#tkm.showwarning("警告","ボタン押すな")

root.mainloop()