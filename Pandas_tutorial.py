import pandas


"""

work with pandas:
https://pandas.pydata.org/docs/getting_started/index.html#getting-started

"""
# read csv file
data = pandas.read_csv("weather_data.csv")

# print a table format automatically
#print(data)

# print a column:
# Pandas takes the first row of each column: one single column is series.
#print(type(data["temp"]))


#check type in Pandas: the whole dataframe
#print(type(data))

"""
datafram: is the whole table of the  data, 整个表格就是，dataframe
series: is the single column in the list, 就是一列，一列的，就叫 series
"""

# Dataframe covert data to dictionary:
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html#pandas.DataFrame.to_dict
data_dict = data.to_dict()
print(data_dict)


# Series covert to a list: https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#pandas.Series.to_list
temp_list = data["temp"].to_list()
print(temp_list)
#print(len(temp_list)) the len of the list

# to get average temp in the list
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

# to use pandas series to get the average temp: same result as above
#https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean
average_temp_series = data["temp"].mean()
print(average_temp_series)

# to get the max value in the list by use pandas series method:
#https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max
max_temp = data["temp"].max()
print(max_temp)


# get data in columns: the name of the column, is the first of row of the data:
print(data["condition"])
# another way to get the data from the column is just : pandas coverted the columns as attributes:
print(data.condition) # is the same result as above.

# get data in a row: to get one single row value
row_data_monday = data[data.day == "Monday"]
print(row_data_monday)

# get the max temp in the row:
row_data_max_temp = data[data.temp == data.temp.max()] # check if two values are equal .
print(row_data_max_temp)


# get one single value from a single row first , then get one single value from that column,
monday = data[data.day == "Monday"]
monday_condition = monday.condition
print(monday_condition)

# get monday"s temp and covert temperature to Celsius to Fahrenheit Conversion Formula: (9/5) +32
monday_temp = int(monday.temp) # or monday["temp"]
monday_temp_f = monday_temp* 9/5+32
print(monday_temp_f)

# (Celsius x 1.8) + 32  : same result as above
monday_temp_f = monday_temp * 1.8 + 32
print(monday_temp_f)

# how to create a dataframe from scratch:
dataframe_dict = {
    "students": ["Sophia", "Steven", "Amy"],  # students and sores will the the first row
    "scores": [89, 78, 65]
}
data_table = pandas.DataFrame(dataframe_dict)
print(data_table)
# covert dataframe to a csv file:
data_table.to_csv("dataframe_sample.csv") # inside you can name a file name
