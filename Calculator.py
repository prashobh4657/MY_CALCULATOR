from tkinter import *

def click(event):
    text=event.widget.cget("text")  #event.widget will return button and further .cget() function will return the text on that button;
    if text=="=":
        if scvalue.get().isdigit():
            value*int(scvalue.get())
        else:
            try: 
                value= eval(screen.get())  #eval in-built function in python;   
            except Exception as e:  # If input string is wrong like 5%/+ etc.. then eval() function gives error hence handling that. 
                print(e)
                value="Error"
       
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update
def direct_calculate(event):
    try: 
        value= eval(screen.get())  #eval in-built function in python;   
    except Exception as e:  # If input string is wrong like 5%/+ etc.. then eval() function gives error hence handling that. 
        print(e)
        value="Error"
    scvalue.set(value)
    screen.update()

root=Tk()
root.geometry("644x900")
root.title("MY CALCULATOR")
# root.wm_iconbitmap()  for icon; 
scvalue=StringVar()
scvalue.set("")
screen =Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(pady=10,padx=10)

b=Button(root,text="ENTER",padx=28,pady=18,font="lucida 35 bold",height=1,width=21)
b.place(x=300,y=100)
b.pack()
# b.pack(side=RIGHT,padx=18,pady=5)
b.bind("<Button-1>",direct_calculate)

#FRAME 1
f=Frame(root,bg="grey")
b=Button(f,text="9",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="C",padx=31,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()


#FRAME2
f=Frame(root,bg="grey")
b=Button(f,text="6",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="4",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=25,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
f.pack()


#FRAME3
f=Frame(root,bg="grey")
b=Button(f,text="3",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="1",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=28,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
f.pack()

#FRAME4
f=Frame(root,bg="grey")
b=Button(f,text="0",padx=31,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=30,pady=17,font="lucida 40 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=25,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=25,pady=18,font="lucida 35 bold",height=1,width=2)
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
f.pack()


root.mainloop()
