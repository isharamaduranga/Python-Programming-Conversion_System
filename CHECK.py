from tkinter import *
root=Tk()
root.title('Convertor')
root.geometry('1280x720')

Label(root,text='Conversion System',font=('times new rommon ',50,'bold'),bg='gray',fg='white',relief=RIDGE).pack(pady=10)


n=Label(root,text='Enter Number :',font=('times new rommon ',20,'bold'),fg='blue')
n.place(x=300,y=150)

b=Label(root,text='Binary :',font=('times new rommon ',20,'bold'),fg='blue')
b.place(x=300,y=230)

d=Label(root,text='Decimal :',font=('times new rommon ',20,'bold'),fg='blue')
d.place(x=300,y=310)

h=Label(root,text='HexaDecimal :',font=('times new rommon ',20,'bold'),fg='blue')
h.place(x=300,y=390)

o=Label(root,text='Octal :',font=('Poppins''sans-serif',20,'bold'),fg='blue')
o.place(x=300,y=470)





root.mainloop()