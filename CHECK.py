from tkinter import *
root=Tk()
root.title('Convertor')
root.geometry('1280x720')

# Define Variables
num=IntVar()
lblbinary  = StringVar()
lbldecimal = StringVar()
lblhexa = StringVar()
lbloctal = StringVar()
# Define Functions
def convert():

Label(root,text='Conversion System',font=('Poppins',50,'bold'),bg='gray',fg='white',relief=RIDGE).pack(pady=10)


n=Label(root,text='Enter Number :',font=('Poppins',20,'bold'),fg='blue')
n.place(x=300,y=150)

b=Label(root,text='Binary :',font=('Poppins',20,'bold'),fg='green')
b.place(x=300,y=230)

d=Label(root,text='Decimal :',font=('Poppins',20,'bold'),fg='orange')
d.place(x=300,y=310)

h=Label(root,text='HexaDecimal :',font=('Poppins',20,'bold'),fg='deeppink')
h.place(x=300,y=390)

o=Label(root,text='Octal :',font=('Poppins ',20,'bold'),fg='purple')
o.place(x=300,y=470)


e1= Entry(root,font='arial 20 ',fg='blue',justify=CENTER,relief=GROOVE,textvariable=num)
e1.place(x=650,y=150)

e2= Entry(root,font='arial 20 ',fg='red',justify=CENTER,relief=GROOVE,textvariable=lblbinary)
e2.place(x=650,y=230)

e3= Entry(root,font='arial 20 ',fg='red',justify=CENTER,relief=GROOVE,textvariable=lbldecimal)
e3.place(x=650,y=310)

e4= Entry(root,font='arial 20 ',fg='red',justify=CENTER,relief=GROOVE,textvariable=lblhexa)
e4.place(x=650,y=390)

e5= Entry(root,font='arial 20 ',fg='red',justify=CENTER,relief=GROOVE,textvariable=lbloctal)
e5.place(x=650,y=470)

btn1=Button(root,text='Converter',font='arial  20 bold',fg='lime',bg='black',width=8,border= 5)
btn1.place(x=300,y=580)


btn1=Button(root,text='Clear',font='arial  20 bold',fg='gold',bg='black',width=8,border= 5)
btn1.place(x=550,y=580)

btn1=Button(root,text='Exit...',font='arial  20 bold',fg='red',bg='black',width=8,border= 5)
btn1.place(x=800,y=580)

root.mainloop()