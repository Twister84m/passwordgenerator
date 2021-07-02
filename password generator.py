#Build GUI (add elements)
#Take user input
#Generate password
#


import tkinter as tk
import random
import pyperclip
import string
from tkinter import *

root= tk.Tk()
root.tk_setPalette(background='#ffffff', foreground='#3594f2',
               activeBackground='#3594f2', activeForeground="#ffffff")




#create a string of letters to randomise
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))



# build the password
def rand_pass():
    global x1 
    global x2
    button2.destroy()
    x1 = wbst.get()
    x2 =  random_char(random.randrange (2,5)) + str(random.randrange (1000,9000,1)) + random_char(random.randrange (5,10))
    return x2


def secondcv():
    
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("Saved")
  
    # sets the geometry of toplevel
    newWindow.geometry("400x400")
    Label(newWindow, 
          text ="These are your saved passwords").pack()

    text = tk.Text(newWindow, background=root.cget('background'), relief='flat', height=10) 
# insert text 
    f= open("savedpswrd.txt","r")
    content = f.read()
    text.insert('1.0', content)
# disable text widget to prevent editing
    text.configure(state='disabled')

# scrolling
    scroll = tk.Scrollbar(newWindow, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scroll.set)

    scroll.pack(side='right', fill='y')
    text.pack(side='left', fill='both', expand=True)

    


def copybox(m):

    passw.delete(0, "end")
    passw.insert(0, m)
    pyperclip.copy(str(m))
    label3 = tk.Label(root,text="Is copied to clipbord " + "\n" + "Use Ctrl + v to paste")
    canvas1.create_window(68, 95, window=label3)
    return m

def save():
    if len(wbst.get()) < 1:
        label1 = tk.Label(root, text="please enter a website name")
        canvas1.create_window(125, 200, window=label1)

    else:   
        f= open("savedpswrd.txt","a")
        f.write ( "\n" + x1 + " " + x2 )
        f.close

def makesave():
    global canvas1
    button2 = tk.Button(text='save', command=save, state=NORMAL)
    canvas1.create_window(125, 300, window=button2)

# tell the user whats going on and display password
def  where():  
    
    if len(wbst.get()) < 1:
        label1 = tk.Label(root, text="please enter a website name")
        canvas1.create_window(125, 200, window=label1)

    else:
        label1 = tk.Label(root, text= (copybox(rand_pass()) + "\n" + "is the generated password for:" + "\n" + x1 + "\n" + "would you like to save?"))
        makesave()


    canvas1.create_window(125, 200, window=label1)
    



canvas1 = tk.Canvas(root, width = 250, height = 400)
canvas1.pack()

label2 = tk.Label(root, text="Enter website name: ")
canvas1.create_window(70, 20, window=label2)

wbst = tk.Entry (root)
canvas1.create_window(70, 40, window=wbst)

passw = tk.Entry (root)
canvas1.create_window(70, 65, window=passw)



#Bottons Bottons Bottons Bottons Bottons Bottons 
button1 = tk.Button(text='generate', relief="ridge", borderwidth=6, background='#cef5dc', foreground='#3594f2',  command=where)
canvas1.create_window(170, 40, window=button1)

button2 = tk.Button(text='save', relief="ridge", borderwidth=6, command=save, state=DISABLED)
canvas1.create_window(125, 300, window=button2)

button3 = tk.Button(text='saved', relief="ridge", borderwidth=6, command=secondcv)
canvas1.create_window(125, 335, window=button3)

#rect = canvas1.create_rectangle(20,20, 1, 1, outline='red')

def copy_to_clipboard(self, event=None):
    try:
        sel = self.get("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(sel)
    except TclError:
        pass


m = Menu(root, tearoff = 0)
m.add_command(label ="Cut")
m.add_command(label ="Copy",command=lambda: copy_to_clipboard(wbst))
m.add_command(label ="Paste")
m.add_command(label ="Reload")
m.add_separator()
m.add_command(label ="Rename")
  
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()
chars="fd"
def charsget():
    global chars
    chars = wbst.get("sel.first", "sel.last")
    
wbst.bind("<Button-3>", charsget())



root.mainloop()