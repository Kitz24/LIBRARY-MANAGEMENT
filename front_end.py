import tkinter
from PIL import ImageTk, Image
from back_end import report_generation, average, best_user


def minimize(window):
    window.attributes("-fullscreen", False)
    window.bind("<F12>", lambda event:maximize(window))


def maximize(window):
    window.attributes("-fullscreen", True)
    window.bind("<Escape>", lambda event:minimize(window))


win = tkinter.Tk()
win.title("LIBRARY E-GATE REGISTER")
win.state("zoomed")
win.bind("<F12>", lambda event:maximize(win))

w, h = win.winfo_screenwidth(), win.winfo_screenheight()

pic = Image.open("img1.png")
pic = pic.resize((400, 400), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(pic)

cvs = tkinter.Canvas(win, width=w, height=h, bg="#B5164E")
cvs.create_image(3*w/4, 2*h/5, image=pic)
cvs.pack()

tkinter.Label(win, text="LIBRARY E-GATE REGISTER", bg="#B5164E", fg="#FFFFFF", font="Helvetica 30 bold underline").place(relx=0.30, rely=0.10)
tkinter.Label(win, text="FROM\nDATE", bg="#B5164E", fg="#FFFFFF", font="Helvetica 20 bold").place(relx=0.15, rely=0.25)
tkinter.Label(win, text="TO\nDATE", bg="#B5164E", fg="#FFFFFF", font="Helvetica 20 bold").place(relx=0.15, rely=0.45)
    
e1 = tkinter.Entry(win, width=12, font="Helvetica 30 bold")
e1.place(relx=0.25, rely=0.25)
e1.insert(0, "1990-01-01")
    
e2 = tkinter.Entry(win, width=12, font="Helvetica 30 bold")
e2.place(relx=0.25, rely=0.45)
e2.insert(0, "3000-01-01")

f, t = str(e1.get()), str(e2.get())

gen = tkinter.Button(cvs, text="GENERATE\nREPORT", bg="#B5164E", fg="#FFFFFF", font="Helvetica 20 bold", width=15, height=3, command=lambda:report_generation(f, t))
gen.place(relx=0.10, rely=0.65)

avg = tkinter.Button(cvs, text="AVERAGE\nREPORT\nSTATISTICS", bg="#B5164E", fg="#FFFFFF", font="Helvetica 20 bold", width=15, height=3, command=lambda:average(f, t))
avg.place(relx=0.30, rely=0.65)

usr = tkinter.Button(cvs, text="BEST\nLIBRARY\nUSER", bg="#B5164E", fg="#FFFFFF", font="Helvetica 20 bold", width=15, height=3, command=best_user())
usr.place(relx=0.65, rely=0.65)

win.mainloop()
