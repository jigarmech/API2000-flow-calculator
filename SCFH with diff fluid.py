from math import *
from tkinter import *


def show_data():
  P = float(ent1.get())
  Pb = float(ent2.get())
  D = float(ent3.get())
  T = float(ent4.get())
  F = str(variable.get())
  k_air = 1.4
  M_air = 28.964
  Z_air = 1
  k_pro = 1.2
  M_pro = 26
  Z_pro = 1
  Pg = 14.69595
  Pi = P + Pg
  Po = Pb + Pg
  Amin = pi * (D * D) / 4

  if F != "air":
      qtho = 278200 * Pi * Amin * (((k_pro / (M_pro * T * Z_pro * (k_pro - 1))) * (
              (Po / Pi) ** (2 / k_pro) - ((Po / Pi) ** ((k_pro + 1) / k_pro)))) ** (0.5))
      sentense = "The theoretical flow as per API 2000 is " + str(qtho) + " SCFH"
      txt.insert(0.0, sentense)

  else:
      qtha = 278200 * Pi * Amin * (((k_air / (M_air * T * Z_air * (k_air - 1))) * (
              (Po / Pi) ** (2 / k_air) - ((Po / Pi) ** ((k_air + 1) / k_air)))) ** (0.5))
      sentense = "The theoretical flow as per API 2000 is " + str(qtha) + " SCFH"
      txt.insert(0.0, sentense)



Fluid = [
"air",
"propane",
"butane"
] #etc write other fluid here
root = Tk()
root.title("API 2000 Flow Calculator")
operator=""
text_Input=StringVar()
variable = StringVar(root)
variable.set(Fluid[0]) # default value
root.geometry("500x180")


l1 = Label(root, text="Enter the inlet Pressure (in Psi): ")
l2 = Label(root, text="Enter the outlet/back Pressure (in Psi): ")
l3 = Label(root, text="Enter Seat Diameter (inch): ")
l4 = Label(root, text="Enter Temperature (in Rankine): ")
l5 = Label(root, text="Please choose fluid media: ")


btn1 = Button(root,text="Calculate Flow",bg="Black", fg="white", command=show_data)
btn1.grid(row=6,columnspan=2)

ent1 = Entry(root)
ent2 = Entry(root)
ent3 = Entry(root)
ent4 = Entry(root)


l1.grid(row=0)
l2.grid(row=1)
l3.grid(row=2)
l4.grid(row=3)
l5.grid(row=4)


ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)
ent3.grid(row=2, column=1)
ent4.grid(row=3, column=1)

txt = Text (root, width=60, height=2, wrap=WORD)
txt.grid(row=7,columnspan=2,sticky=W)
w = OptionMenu(root, variable, *Fluid)
w.grid(row=4, column=1)


root.mainloop()
