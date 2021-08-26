"""
CSV = Comma Separated Values
"""

# with open a data and covert into a list :
# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)



import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file) # print as an object, and this object can be loop through.
    #print(data)
    temperature = []
    for row in data: #print(row) # print each row and each value in a list
        if row[1] != "temp": # just print out the numbers
            temperature.append(int(row[1])) # string into int
    print(temperature)

"""
work with pandas:
https://pandas.pydata.org/docs/getting_started/index.html#getting-started

"""

import pandas

# read csv file
data = pandas.read_csv("weather_data.csv")
print(data) # print a table format automatically


# print a column:
# Pandas takes the first row of each column:
print(data["day"])

examples = "examples"
print(examples.find("m"))