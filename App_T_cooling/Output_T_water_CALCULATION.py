Flow_rate = float(input('Please input the flow rate of cooling:'))
T_water_C = float(input('Please input the cooling temperature:'))
Heat_capacity_15 = float(4187)  # J/(kg.K) at 15C
T_water_K = float(T_water_C+273)  # K
Density_water = 998  # kg/m^3
Mass_water = Density_water*Flow_rate/(60*1000)  # kg/s
T_water_ini = T_water_K  # degree Kelvin


import xlrd

data = xlrd.open_workbook('d1.xls')
table_1=data.sheets()[0]  # start from column 0 and sheet 0
data_power = table_1.col_values(1)
data_time = table_1.col_values(0)
print(table_1, data_power, '\n', data_time)
last_second = data_time[len(data_time)-1]
print('number of T:', len(data_power))
if data_power:
    print('Successfully extracting the data of power')
    print(type(data_power), 'There are', last_second, 'seconds counted')
if len(data_time) == len(data_power):
    print('keep going on')
else:
    print('You pasted wrongly for the data')



print('*'*55, 'Confirm', '*'*85)
print('The flow rate is:', Flow_rate, 'L/min')
print('The heat capacity of water is:', Heat_capacity_15, 'J/kg.C', 'at 15C')
print('Water temperature is:', T_water_K, 'degree of Kelvin')

i = 0
data_T_water = [T_water_ini]
while i+1 < len(data_power): #((data_time[i+1]-data_time[i])*0)
    det_T = ((data_power[i+1]))/(Mass_water * Heat_capacity_15)
    T_water_ini = T_water_ini+det_T
    data_T_water.append(T_water_ini)
    T_water_ini = T_water_K
    i += 1
    print(data_T_water)
    if not i+1 < len(data_power):
        break


j = 0
data_T_water_C = []
while j+1 < len(data_T_water):
    a = data_T_water[j] - 273
    data_T_water_C.append(a)
    j += 1
    if not j+1 < len(data_T_water):
        break


fin_1 = open('obtained_data1.txt', 'wt')
fin_1.write(str(data_T_water_C))
fin_1.close()


print('\t')
print(item for item in data_T_water_C)

import xlsxwriter
workbook = xlsxwriter.Workbook('answer.xlsx')
worksheet = workbook.add_worksheet(u'sheet1')
worksheet.set_column('B:B', 20)
for i in range(len(data_T_water_C)):
    worksheet.write('B%s'%str(i+1), data_T_water_C[i])
for j in range(len(data_time)):
    worksheet.write('A%s'%str(j+1), data_time[j])
workbook.close()