import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

window = Tk()
window.configure(bg='black')

window.title('Temperature of Water Cooling')  # Title added

a_label = ttk.Label(window, text="A Label")  # Simply add a label
a_label.grid(row=2, column=1)  # only appears in empty areas

ttk.Label(window, text='Enter a name:').grid(row=2, column=1)  # change the label

def km_to_miles():
    print("Success!" + e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

def suqare():
    value = float(e2_value.get())**2 - float(e1_value.get())
    t2.insert(END, value)

# Add Button
b1 = Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0, column=0, rowspan=1)

b2 = Button(window, text='Square', command=suqare)
b2.grid(row=1, column=0, rowspan=1)

# Add check buttons
ttk.Label(window, text='Choose a number:').grid(row=3, column=0)
number = StringVar()
number_chosen = ttk.Combobox(window, width=12, textvariable=number, state='readonly')
number_chosen.grid(row=3, column=1)
number_chosen['values'] = (1, 23, 45, 67, 100)
number_chosen.current(4)

chvardis = IntVar()
check1 = Checkbutton(window, text='Disabled', variable=chvardis, state='disabled')
check1.select()

# Add image
logo = PhotoImage(file='Roctool_logo.PNG')
imgLabel = ttk.Label(window, image=logo)
imgLabel.grid(row=1,column=4)

e1_value = StringVar()  # String vary function: Textbox Entry Widget
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value = StringVar()  # String vary function: Textbox Entry Widget
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=1, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=2)

window.mainloop()