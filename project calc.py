from tkinter import *
from tkinter import messagebox
from math import *

calc = Tk()
calc.title("Calculator")  # creating title of gui

width=380
height=475

screen_width=calc.winfo_screenwidth()
screen_height=calc.winfo_screenheight()
pos_top=int((screen_height)/2-(height)/2)
pos_side=int((screen_width)/2-(width)/2)

calc.geometry(f'{width}x{height}+{pos_side}+{pos_top}')#to position the window at the center of the screen


#calc.iconbitmap('pes.ico')  # icon

text1 = Label(calc,text="Let's Calculate", fg="black", font=('Comic Sans MS',22))#heading
text1.pack()
screen = Entry(calc,font=("lucida",25),borderwidth=2,relief=GROOVE,justify=RIGHT,)  # screen of calculator
screen.pack(fill=X,  pady=5, padx=5)
screen.bind("<Key>", lambda e: "break")         # Disable characters from keyboard

#importing the functions for calculator operation

#defining the normal function
def clickbtn(val):
    b = val.widget
    txt = b["text"]  # to get the text from the clicked button

    # to account for multiplication sign
    if txt== "x":
        screen.insert(END, "*")
        return


    # backspace
    if txt == "C":
        screen.delete(len(screen.get())-1,END)
        return


    # all clear
    if txt == "AC":
        screen.delete(0,END)
        return
    #to evaluate the entered expression
    if txt == "=":
        try :
            a=screen.get()
            ans=eval(a)
            screen.delete(0,END)
            screen.insert(0,ans)

        except Exception as e:
            screen.delete(0,END)
            screen.insert(END,"Invalid expression")
            messagebox.showinfo("message","clear the screen")
        else:
            pass
        return
    screen.insert(END,txt)


#sc:scientific calculator function 

def scientific(text):
    key = text.widget
    txt = key['text']
    no = screen.get()  # giving var name to the numbers on screen
    result = ''  # its for storing the solution
    if txt == 'sqrt':  # to find square root
        result = str(sqrt(float(no)))  # m is the math module ,float is used to change the string to floting number
    if txt == 'sin':  # to find sin in radians
        if no=='':
            return
        else:
            result = sin(float(no))
    if txt == 'tan':  # to find tan in radians
        if no=='':
            return
        else:
            result = tan(float(no))
    if txt == 'cos':  # to find cos in radians
        if no=='':
            return
        else:
            result = cos(float(no))
    if txt == 'log':     # to find log to base 10
        if no=='':
            return
        result = log10(float(no))
    if txt == 'ln':  # to find ln base e
        if no=='':
            return
        result = log(float(no))
    if txt == 'x!':  # to find factorial
        result = factorial(float(no))
    if txt == 'deg':  # to change radians to degree
        result = degrees(float(no))
    if txt == 'x^3':  # to find cube
        result = ((float(no)) ** 3)
    if txt == 'x^2':  # to find square
        result = ((float(no)) ** 2)
    if txt == '1/x':
        result = 1 / (float(no))
    if txt == 'e':
        if no == '':  # dispaly only e value
            result = e
        else:  # exponential of e
            result = e ** float(no)

    screen.delete(0, END)
    screen.insert(0, result)



# buttons

#buttonframe-to change the geometry of buttons by using grid and placing them on the frame
buttonframe = Frame(calc)
buttonframe.pack(expand=100)#expand is used to keep the button frame in the center when the window is resized


#buttonwidgets
button1 = Button(buttonframe, text='1',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button1.bind('<Button-1>',clickbtn)#to invoke the function by the left click of the mouse
button1.grid(row=2,column=0,padx=2,pady=2)

button2 = Button(buttonframe, text='2',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button2.bind('<Button-1>',clickbtn)
button2.grid(row=2,column=1,padx=2,pady=2)

button3 = Button(buttonframe, text='3',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button3.bind('<Button-1>',clickbtn)
button3.grid(row=2,column=2,padx=2,pady=2)

button4 = Button(buttonframe, text='4',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button4.bind('<Button-1>',clickbtn)
button4.grid(row=1,column=0,padx=2,pady=2)

button5 = Button(buttonframe, text='5',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button5.bind('<Button-1>',clickbtn)
button5.grid(row=1,column=1,padx=2,pady=2)

button6 = Button(buttonframe, text='6',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button6.bind('<Button-1>',clickbtn)
button6.grid(row=1,column=2,padx=2,pady=2)

button7 = Button(buttonframe, text='7',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button7.bind('<Button-1>',clickbtn)
button7.grid(row=0,column=0,padx=2,pady=2)

button8 = Button(buttonframe, text='8',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button8.bind('<Button-1>',clickbtn)
button8.grid(row=0,column=1,padx=2,pady=2)

button9 = Button(buttonframe, text='9',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button9.bind('<Button-1>',clickbtn)
button9.grid(row=0,column=2,padx=2,pady=2)

button0 = Button(buttonframe, text='0',bg='white', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='orange',relief='groove')
button0.bind('<Button-1>',clickbtn)
button0.grid(row=3,column=1,padx=2,pady=2)

button_add = Button(buttonframe, text='+',bg='honeydew', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_add.bind('<Button-1>',clickbtn)
button_add.grid(row=3,column=3,padx=2,pady=2)

button_sub = Button(buttonframe, text='-',bg='honeydew', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_sub.bind('<Button-1>',clickbtn)
button_sub.grid(row=2,column=3,padx=2,pady=2)

button_div = Button(buttonframe, text='/',bg='honeydew', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_div.bind('<Button-1>',clickbtn)
button_div.grid(row=0,column=3,padx=2,pady=2)

button_mul = Button(buttonframe, text='x',bg='honeydew', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_mul.bind('<Button-1>',clickbtn)
button_mul.grid(row=1,column=3,padx=2,pady=2)

button_eq = Button(buttonframe, text='=',bg='aquamarine', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_eq.bind('<Button-1>',clickbtn)
button_eq.grid(row=3,column=2,padx=2,pady=2)

button_deci = Button(buttonframe, text='.',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_deci.bind('<Button-1>',clickbtn)
button_deci.grid(row=3,column=0,padx=2,pady=2)

button_clear = Button(buttonframe, text='AC',bg='white', fg='black',width=15,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')#all clear button
button_clear.grid(row=7,column=2,columnspan=100,padx=1,pady=1)
button_clear.bind('<Button-1>',clickbtn)


button_back = Button(buttonframe, text='C',bg='white', fg='black',width=15,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')#backspace button
button_back.grid(row=7,column=0,columnspan=2,padx=1,pady=2)
button_back.bind('<Button-1>',clickbtn) 

button_square = Button(buttonframe, text='x^2',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_square.grid(row=4,column=0,padx=1,pady=2)
button_square.bind('<Button-1>',scientific)

button_sin = Button(buttonframe, text='sin',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_sin.grid(row=4,column=2,padx=1,pady=2)
button_sin.bind('<Button-1>',scientific)

button_cos = Button(buttonframe, text='cos',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_cos.grid(row=4,column=3,padx=1,pady=2)
button_cos.bind('<Button-1>',scientific)

button_e = Button(buttonframe, text='e',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_e.grid(row=5,column=1,padx=1,pady=2)
button_e.bind('<Button-1>',scientific)

button_cube = Button(buttonframe, text='x^3',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_cube.grid(row=4,column=1,padx=1,pady=2)
button_cube.bind('<Button-1>',scientific)

button_log = Button(buttonframe, text='log',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_log.grid(row=5,column=0,padx=1,pady=2)
button_log.bind('<Button-1>',scientific)

button_sqrt = Button(buttonframe, text='sqrt',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_sqrt.grid(row=5,column=2,padx=1,pady=2)
button_sqrt.bind('<Button-1>',scientific)

button_tan = Button(buttonframe, text='tan',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_tan.grid(row=5,column=3,padx=1,pady=2)
button_tan.bind('<Button-1>',scientific)

button_inverse = Button(buttonframe, text='1/x',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_inverse.grid(row=6,column=3,padx=1,pady=2)
button_inverse.bind('<Button-1>',scientific)

button_fact = Button(buttonframe, text='x!',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_fact.grid(row=6,column=2,padx=1,pady=2)
button_fact.bind('<Button-1>',scientific)

button_ln = Button(buttonframe, text='ln',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_ln.grid(row=6,column=1,padx=1,pady=2)
button_ln.bind('<Button-1>',scientific)

button_deg = Button(buttonframe, text='deg',bg='azure', fg='black',width=7,height=1,font=('Comic Sans MS',13),activeforeground='white',activebackground='lightgreen',relief='groove')
button_deg.grid(row=6,column=0,padx=1,pady=2)
button_deg.bind('<Button-1>',scientific)

calc.mainloop()