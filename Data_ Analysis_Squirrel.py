import pandas

# pandas read csv data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data)


""" 
#print one single column :
fur_color = data['Primary Fur Color']


# check if the color is gray: maybe covert into a list:
color_list = fur_color.to_list()
#print(color_list)


#count how many differet colors in the list:
grey = color_list.count("Gray")
print(grey)
red = color_list.count("Cinnamon")
print(red)
black = color_list.count("Black")
print(black)



# how to create a dataframe from scratch:
dataframe_dict = {
   "fur Color": ["grey", "red","black"], # the colors
    "Count": [grey, red, black] # the value of the

}
data_table = pandas.DataFrame(dataframe_dict)
print(data_table)

# covert dataframe to a csv file:
data_table.to_csv("squirrel_count.csv") # inside you can name a file name

"""
#solution:

# get one single value from a single row first , then get one single value from that column,
# to check how many grey color in the column use len()
grey_color_count = len(data[data['Primary Fur Color'] == "Gray"])
print(grey_color_count)

cinnamon_color_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
print(cinnamon_color_count)

black_color_count = len(data[data['Primary Fur Color'] == "Black"])
print(black_color_count)

# to create a dataframe from scratch:
# create a dict first:
data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    'Count': [grey_color_count, cinnamon_color_count, black_color_count]

}

# crete a dataframe:
dataframe = pandas.DataFrame(data_dict)

#datafrme covert to a csv file:

dataframe.to_csv("squirrel_count.csv")

