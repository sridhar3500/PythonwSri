#calculator using tkinter gui

from tkinter import *
from tkinter import font

exp=""

def get_click(item):
    global exp
    exp=exp+str(item)
    input_var.set(exp)
    
def get_clr():
    global exp
    exp=""
    input_var.set("")
    
def get_eql():
    global exp
    ans=str(eval(exp))
    input_var.set(ans)
    exp=" "
  
calc=Tk()
calc.title('Calculator')
calc.geometry('310x280')
calc.configure(bg='black')
calc.resizable(0,0)

#result
input_var=StringVar()
result=Label(calc,text='',bg='black',fg='white',font=70,justify='right',textvariable=input_var)
result.grid(row=0,column=0,pady=(50,20),padx=20,columnspan=5,sticky='e')

#to create a button
but_1=Button(calc,text='1',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2', command=lambda:get_click(1))
but_1.grid(row=1,column=0)

but_2=Button(calc,text='2',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(2))
but_2.grid(row=1,column=1)

but_3=Button(calc,text='3',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(3))
but_3.grid(row=1,column=2)

but_add=Button(calc,text='+',bg='chartreuse2',fg='black',relief=GROOVE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click('+'))
but_add.grid(row=1,column=3)
 
but_4=Button(calc,text='4',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(4))
but_4.grid(row=2,column=0)

but_5=Button(calc,text='5',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,
             cursor='hand2',command=lambda:get_click(5))
but_5.grid(row=2,column=1)

but_6=Button(calc,text='6',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(6))
but_6.grid(row=2,column=2)

but_sub=Button(calc,text='-',bg='chartreuse2',fg='black',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click('-'))
but_sub.grid(row=2,column=3)

but_7=Button(calc,text='7',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(7))
but_7.grid(row=3,column=0)

but_8=Button(calc,text='8',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(8))
but_8.grid(row=3,column=1)

but_9=Button(calc,text='9',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(9))
but_9.grid(row=3,column=2)

but_mul=Button(calc,text='*',bg='chartreuse2',fg='black',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click('*'))
but_mul.grid(row=3,column=3)

but_clr=Button(calc,text='C',bg='cyan2',fg='black',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_clr())
but_clr.grid(row=4,column=0)

but_0=Button(calc,text='0',bg='black',fg='white',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click(0))
but_0.grid(row=4,column=1)

but_div=Button(calc,text='/',bg='chartreuse2',fg='black',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_click('/'))
but_div.grid(row=4,column=3)

but_eql=Button(calc,text='=',bg='cyan2',fg='black',relief=RIDGE,font=50,width=6,height=1,cursor='hand2',command=lambda:get_eql())
but_eql.grid(row=4,column=2)



calc.mainloop()