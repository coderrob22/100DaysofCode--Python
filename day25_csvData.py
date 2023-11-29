with open('weather_data.csv') as weather:
    data = weather.readlines()
    print(data)

import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')

print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

list_temp = data['temp'].to_list()
print(sum(list_temp)/len(list_temp))

print(max(data['temp']))

print(data[data.temp== data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.temp)