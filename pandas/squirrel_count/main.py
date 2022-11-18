import pandas

data = pandas.read_csv("pandas/squirrel_count/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"], "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]}
print(data_dict)

data_df = pandas.DataFrame(data_dict)
data_df.to_csv("squirrel_count.csv")
