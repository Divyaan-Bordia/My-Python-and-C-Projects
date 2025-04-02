from tkinter  import *

window = Tk()
window.title("Calculator")

l1 = Label(window,
           text  = 'Choose an operation',
           font = ('Times New Roman', 20),
           bg = 'white',
           fg = 'blue')
l1.pack(side = TOP)


def add():
    l1.destroy()
    Badd.destroy()
    Bsub.destroy()
    Bmul.destroy()
    Bdivi.destroy()

    l2 = Label(window,
               text  = 'Enter the numbers you want to add',
               font = ('Times New Roman', 20),
               bg = 'white',
               fg = 'blue')
    l2.pack(side = TOP)
    e1 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e1.pack(side = TOP)
    e2 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e2.pack(side = TOP)

    def ADD():
        num1 = int(e1.get())
        num2 = int(e2.get())
        result = num1 + num2
        l2.destroy()
        e1.destroy()
        e2.destroy()
        submit.destroy()
        l1 = Label(window,
                   text  = 'The result is: ' + str(result),
                   font = ('Times New Roman', 20),
                   bg = 'white',
                   fg = 'blue')
        l1.pack(side = TOP)

    submit = Button(window,
                     text = 'Submit',
                     bg = 'black',
                     fg = '#00ff00',
                     font = ('Times New Roman', 20),
                     command = ADD)
    submit.pack(side = BOTTOM)


def sub():
    l1.destroy()
    Badd.destroy()
    Bsub.destroy()
    Bmul.destroy()
    Bdivi.destroy()

    l2 = Label(window,
               text  = 'Enter the numbers you want to subtract',
               font = ('Times New Roman', 20),
               bg = 'white',
               fg = 'blue')
    l2.pack(side = TOP)
    e1 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e1.pack(side = TOP)
    e2 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e2.pack(side = TOP)

    def SUB():
        num1 = int(e1.get())
        num2 = int(e2.get())
        result = num1 - num2
        l2.destroy()
        e1.destroy()
        e2.destroy()
        submit.destroy()
        l1 = Label(window,
                   text  = 'The result is: ' + str(result),
                   font = ('Times New Roman', 20),
                   bg = 'white',
                   fg = 'blue')
        l1.pack(side = TOP)

    submit = Button(window,
                     text = 'Submit',
                     bg = 'black',
                     fg = '#00ff00',
                     font = ('Times New Roman', 20),
                     command = SUB)
    submit.pack(side = BOTTOM)

def mul():
    l1.destroy()
    Badd.destroy()
    Bsub.destroy()
    Bmul.destroy()
    Bdivi.destroy()

    l2 = Label(window,
               text  = 'Enter the numbers you want to multiply',
               font = ('Times New Roman', 20),
               bg = 'white',
               fg = 'blue')
    l2.pack(side = TOP)
    e1 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e1.pack(side = TOP)
    e2 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e2.pack(side = TOP)

    def MUL():
        num1 = int(e1.get())
        num2 = int(e2.get())
        result = num1 * num2
        l2.destroy()
        e1.destroy()
        e2.destroy()
        submit.destroy()
        l1 = Label(window,
                   text  = 'The result is: ' + str(result),
                   font = ('Times New Roman', 20),
                   bg = 'white',
                   fg = 'blue')
        l1.pack(side = TOP)

    submit = Button(window,
                     text = 'Submit',
                     bg = 'black',
                     fg = '#00ff00',
                     font = ('Times New Roman', 20),
                     command = MUL)
    submit.pack(side = BOTTOM)

def divi():
    l1.destroy()
    Badd.destroy()
    Bsub.destroy()
    Bmul.destroy()
    Bdivi.destroy()

    l2 = Label(window,
               text  = 'Enter the numbers you want to divide',
               font = ('Times New Roman', 20),
               bg = 'white',
               fg = 'blue')
    l2.pack(side = TOP)
    e1 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e1.pack(side = TOP)
    e2 = Entry(window,
               font = ('Times New Roman', 20),
               bg = 'black',
               fg = '#00ff00')
    e2.pack(side = TOP)

    def DIVI():
        num1 = int(e1.get())
        num2 = int(e2.get())
        try:
            result = num1 / num2
            l2.destroy()
            e1.destroy()
            e2.destroy()
            submit.destroy()
            l1 = Label(window,
                       text  = 'The result is: ' + str(result),
                       font = ('Times New Roman', 20),
                       bg = 'white',
                       fg = 'blue')
            l1.pack(side = TOP)
        except ZeroDivisionError:
            l2.destroy()
            e1.destroy()
            e2.destroy()
            submit.destroy()
            l1 = Label(window,
                       text  = 'Error: Division by zero',
                       font = ('Times New Roman', 20),
                       bg = 'white',
                       fg = 'blue')
            l1.pack(side = TOP)

    submit = Button(window,
                     text = 'Submit',
                     bg = 'black',
                     fg = '#00ff00',
                     font = ('Times New Roman', 20),
                     command = DIVI)
    submit.pack(side = BOTTOM)
  
    

Badd = Button(window,
           text='Add',
           bg = 'black',
           fg = '#00ff00',
           font = ('Times New Roman', 20),
           command = add)
Badd.pack(side = BOTTOM)

Bsub = Button(window,
              text='Subtract',
              bg = 'black',
              fg = '#00ff00',
              font = ('Times New Roman', 20),
              command = sub)
Bsub.pack(side = BOTTOM)

Bmul = Button(window,
                text='Multiply',
                bg = 'black',
                fg = '#00ff00',
                font = ('Times New Roman', 20),
                command = mul)
Bmul.pack(side = BOTTOM)

Bdivi = Button(window,
                text='Divide',
                bg = 'black',
                fg = '#00ff00',
                font = ('Times New Roman', 20),
                command = divi)               
Bdivi.pack(side = BOTTOM)


window.mainloop()