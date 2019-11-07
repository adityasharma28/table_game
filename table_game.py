from tkinter import *
root=Tk()
root.config(bg='powder blue')
root.title("Table Game")
for i in range(1,11):
    label=Label(root,text=str(i),font="arial 20 bold",bg='#556699',fg='#11ffaa')
    label.grid(row=0,column=i,padx=5,pady=5,ipadx=5,ipady=5,sticky='nswe')

for i in range(1,11):
    label=Label(root,text=str(i),font="arial 20 bold",bg='#556699',fg='#11ffaa')
    label.grid(row=i,column=0,padx=5,pady=5,ipadx=5,ipady=5,sticky='nswe')
def Result(x,y):
    global lb
    lb[10*(x-1)+(y-1)]['text']=str(x*y)

lb=[]
for i in range(1,11):
    for j in range(1,11):
        lb.append(Button(root, text='?', font="arial 20 bold", bg='#556699',
                        fg='#11ffaa',command=lambda t=(i,j):Result(t[0],t[1])))
        lb[-1].grid(row=i, column=j, padx=5, pady=5, ipadx=5, ipady=5, sticky='nswe')
def EnterEvent(event,i):
    lb[i]['bg']='#aaffee'
    lb[i]['fg'] = 'black'
    lb[i]['bd'] = 5

def LeaveEvent(event,i):
    lb[i]['bg']='#556699'
    lb[i]['fg'] = '#11ffaa'
    lb[i]['bd'] = 0
for i,button in enumerate(lb):
    button.bind('<Enter>',lambda event,x=i:EnterEvent(event,x))
    button.bind('<Leave>',lambda event,x=i:LeaveEvent(event,x))
for i in range(11):
    root.grid_rowconfigure(i,weight=10)
for i in range(11):
    root.grid_columnconfigure(i,weight=1)
root.mainloop()
