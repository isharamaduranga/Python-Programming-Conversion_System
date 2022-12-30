from tkinter import *
root=Tk()
root.title('Convertor')
root.geometry('1280x720')

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

e1= Entry(root,font='arial 20 ',fg='red',justify=CENTER,relief=GROOVE)
e1.place(x=650,y=150)




root.mainloop()