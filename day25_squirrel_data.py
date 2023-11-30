import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(len(data[data["Primary Fur Color"] == 'Black']))


squirrels_gon_wild = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [2473, 392, 103]
}


pandas.DataFrame(squirrels_gon_wild).to_csv('squirrel_count.csv')