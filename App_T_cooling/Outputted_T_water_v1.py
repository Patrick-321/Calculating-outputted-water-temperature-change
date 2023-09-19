import tkinter
from tkinter import *
from tkinter import ttk
import xlsxwriter
# *****************************************************************************************************************************
import xlrd
data = xlrd.open_workbook('d1.xls')
table_1=data.sheets()[0]  # start from column 0 and sheet 0
data_power = table_1.col_values(1)
data_time = table_1.col_values(0)
last_second = data_time[len(data_time)-1]


Heat_capacity_15 = 4187  # J/(kg.K) at 15C
Density_water = 998  # kg/m^3


# **************************************************************************************************************************

window = Tk()
window.configure(bg='black', height=200, width=200)
window.geometry("1000x500+200+20")

window.title('Temperature of Water Cooling')  # Title added

a_label = ttk.Label(window, text="A Label")  # Simply add a label
a_label.grid(row=0, column=1)  # only appears in empty areas
ttk.Label(window, text='Flow rate').grid(row=0, column=1)  # change the label

a_label = ttk.Label(window, text="Mass flow rate")  # Simply add a label
a_label.grid(row=0, column=2)  # only appears in empty areas

a_label = ttk.Label(window, text="Inputted Water")  # Simply add a label
a_label.grid(row=2, column=1)  # only appears in empty areas

a_label = ttk.Label(window, text="Outputted Water")  # Simply add a label
a_label.grid(row=2, column=2)  # only appears in empty areas

# *******************************************************************************************************************************
tree = ttk.Treeview(window)
tree["columns"] = ('Time', 'Outputted water temperature')
tree.column('Time', width=100)
tree.column('Outputted water temperature', width=200)
tree.heading('Time', text='Time')
tree.heading('Outputted water temperature', text='Outputted water temperature')
tree.grid(row=15, column=6, rowspan=100, columnspan=100)

# **********************************************************************************************************************

def mass_water():
    fr = float(e1_value.get())*Density_water/(60*1000)
    t1.insert(END, fr)

def output_water():
    i = 0
    data_T_water = [e2_value.get()]

    while i + 1 < len(data_power):
        det_T = (abs(data_power[i])) / (float(e1_value.get())*Density_water/(60*1000) * Heat_capacity_15)
        T_water_ini = float(e2_value.get()) + det_T  # float
        data_T_water.append(T_water_ini)
        T_water_ini = e2_value.get()
        i += 1
        tree.insert("", i+1, text='line', values=(data_time[i], data_T_water[i]))
        if not i + 1 < len(data_power):
            break
    print(len(data_T_water), 'values are obtained:', data_T_water)
    print(len(data_time), 'values are obtained:', data_time)
    t2.insert(END, data_T_water)
    print(type(data_T_water), type(e2_value))

    workbook = xlsxwriter.Workbook ( 'answer.xlsx' )
    worksheet = workbook.add_worksheet ( u'sheet1' )
    worksheet.set_column ( 'B:B' , 20 )
    for i in range ( len ( data_T_water ) ):
        worksheet.write ( 'B%s' % str ( i + 1 ) , data_T_water[ i ] )
    for j in range ( len ( data_time ) ):
        worksheet.write ( 'A%s' % str ( j + 1 ) , data_time[ j ] )
    workbook.close ()


# **********************************************************************************************************************

# Add Button
b1 = Button(window, text='Execute', command = mass_water)
b1.grid(row=1, column=0, rowspan=1)

b3 = Button(window, text='Execute', command = output_water)
b3.grid(row=3, column=0, rowspan=1)



# Add check buttons
number = StringVar()
number_chosen = ttk.Combobox(window, width=12, textvariable=number, state='readonly')
number_chosen.grid(row=0, column=5)
number_chosen['values'] = ('injection', 'compression')
number_chosen.current(0)

chvardis = IntVar()
check1 = Checkbutton(window, text='Disabled', variable=chvardis, state='disabled')
check1.select()

# Add image
logo = PhotoImage(file='Roctool_logo.PNG')
imgLabel = ttk.Label(window, image=logo)
imgLabel.grid(row=1, column=6, rowspan=5, columnspan=15)

e1_value = StringVar()  # String vary function: Textbox Entry Widget
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=1, column=1)


e2_value = StringVar()  # String vary function: Textbox Entry Widget
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=3, column=1, rowspan=1)



t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=2)

t2 = Text(window, height=1, width=20)
t2.grid(row=3, column=2, rowspan=1)


window.mainloop()
