



from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title('BMI')
root.geometry('500x500')
root.config(bg='teal')
'''def progress():
  meters = (feet.get()+ (inch.get() * 0.083))*0.3048
'''  
myWeight = IntVar()
myInch = IntVar()
myFeet = IntVar()
def BMI():
  '''weight_num = weight.get()
  weight_int = float(weight_num)
  feet_num = feet.get()
  inch_num = inch.get()
  feet_int = float(feet_num)
  inch_int = float(inch)'''
  kg = int(myWeight.get() * 0.45359237)
  meters = (myFeet.get()+ (myInch.get() * 0.083))*0.3048
  BMI = kg/(meters*meters)
  print(kg,meters,BMI)
  
  BMI_Cal(BMI)

def myEx():
    root.quit()  
    

def BMI_Cal(BMI):
  if BMI < 18.5:
    messagebox.showinfo('UnderWeight', f'Your BMI = {BMI} is underweight')
  elif (BMI >= 18.5) and (BMI < 24.9):
    messagebox.showinfo('Normal', f'Your BMI = {BMI} is Normal')
  elif (BMI >= 25) and (BMI < 29.9):
    messagebox.showinfo('Overweight', f'Your BMI = {BMI} is Overweight')
  elif (BMI>30):
    messagebox.showinfo('Obesity', f'Your BMI = {BMI} is Obesity')
  else:
    messagebox.showerror('Error', 'Something wend wrong!')
  

age_lb = Label(root,text="Enter Age (18 - 65)", bg='teal', fg = 'white')
age_lb.grid(row=1, column=1)
age_entry = Entry(root, bg = 'skyblue')
age_entry.grid(row=1, column=2, pady=5)

male = Checkbutton(root, text = "Male", bg='teal', fg = 'white')
female = Checkbutton(root, text = "Female", bg='teal', fg = 'white')
male.grid(row=2, column = 1)
female.grid(row=2, column = 2)

hieght_lb = Label(root, text = "Hieght:", bg='teal', fg = 'white')
hieght_lb.place(x=60,y=60)


feet_lb = Label(root, text = "feet:", bg='teal', fg = 'white')
feet_lb.place(x=86,y=80)
feet = Spinbox(root, from_=0 , to=10, bg = 'skyblue',textvariable=myFeet)
inch = Spinbox(root, from_=0 , to=11, bg = 'skyblue',textvariable=myInch)
weight = Entry(root, bg = 'skyblue',textvariable=myWeight)
feet.place(x=125,y=80)
inch_lb = Label(root, text = "inches:", bg='teal', fg = 'white')
inch_lb.place(x=76,y=100)
inch.place(x=125,y=100)

weight_lb = Label(root, text = 'Weight:', bg='teal', fg = 'white')
weight_lb.place(x=60,y=125)
weight.place(x=125,y=125)

save = Button(root,text = 'CALCULATE', command = BMI, bg = 'skyblue', fg = 'black')
save.place(x=150,y=150)

myExit = Button(root,text = 'EXIT', bg = 'skyblue', fg = 'black',command=myEx)
myExit.place(x=430,y=430)

root.mainloop()


