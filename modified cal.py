from tkinter import*
root=Tk()
def btnClick(number):
    global op
    op=op+str(number)
    text_input.set(op)
def btnClear():
    global op
    op=""
    text_input.set("")
def btnEquals():
    global op
    sumup = str(eval(op))
    text_input.set(sumup)
root.title("Ramana calculator")
op=""
root.config(bg="gray3")
text_input=StringVar()
txtDisplay=Entry(root,font=('arial',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="powder blue",justify="right")
txtDisplay.grid(columnspan=4)
btn7=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
add=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+")).grid(row=1,column=3)

btn6=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row=2,column=0)
btn5=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn4=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row=2,column=2)
sub=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-")).grid(row=2,column=3)

btn3=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row=3,column=0)
btn2=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn1=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row=3,column=2)
mul=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*")).grid(row=3,column=3)

btnclear=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="C",command=btnClear).grid(row=4,column=0)
btn0=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0)).grid(row=4,column=1)
btnequal=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="=",command=btnEquals).grid(row=4,column=2)
div=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/")).grid(row=4,column=3)
btnpow=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="**",command=lambda:btnClick("**")).grid(row=5,column=0)
btnper=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="%",command=lambda:btnClick("%")).grid(row=5,column=1)
btnopen=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="(",command=lambda:btnClick("(")).grid(row=5,column=2)
btnclose=Button(root,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text=")",command=lambda:btnClick(")")).grid(row=5,column=3)

root.mainloop()