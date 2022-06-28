import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr,jid
    tmr = tmr+1
    label["text"] = tmr
    jid=root.after(1000,count_up)

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    #key=event.keysym
    #tkm.showinfo("キー押下",f"{key}が押されました")
    root.after(10,count_up)

if __name__ == "__main__":
    root = tk.Tk()
    label=tk.Label(root,font=("Times New Roman",80))
    label.pack()
    tmr=0
    jid=None
    #root.after(1000,count_up)
    root.bind("<KeyPress>",key_down)
    root.mainloop()