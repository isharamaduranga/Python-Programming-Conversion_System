from tkinter import *
root=Tk()
root.title('Convertor')
root.geometry('1280x720')

Label(root,text='Conversion System',font=('times new rommon ',50,'bold'),bg='gray',fg='white',relief=RIDGE).pack(pady=10)


n=Label(root,text='Enter Number :',font=('times new rommon ',20,'bold'),fg='blue')
n.place(x=300,y=150)

n=Label(root,text='Binary :',font=('times new rommon ',20,'bold'),fg='blue')
n.place(x=300,y=230)

n=Label(root,text='Decimal :',font=('times new rommon ',20,'bold'),fg='blue')
n.place(x=300,y=310)

n=Label(root,text='HexaDecimal :',font=('times new rommon ',20,'bold'),fg='blue')
n.place(x=300,y=390)

n=Label(root,text='Octal :',font=('Poppins''sans-serif',20,'bold'),fg='blue')
n.place(x=300,y=470)





root.mainloop()