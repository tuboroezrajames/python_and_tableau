# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:42:23 2023

@author: EZRA
"""
#importing pandas function and assigning a variable pd to shorten the pandas word
import pandas as pd


#loading csv file 

data = pd.read_csv('transaction2.csv')

#correcting separator if pandas do not recognize the delimiter used
data = pd.read_csv('transaction2.csv',sep=';')


#summary of the dataset
data.info()


#Writing script to calculate the following
# to update the dataframe for example adding a column onto it,the syntax to do this is

#table namae ["new column name"]= table name[""] see the script below

data["SalesPerTransaction"]=data["SellingPricePerItem"]*data["NumberOfItemsPurchased"]

data["CostPerTransaction"]=data["NumberOfItemsPurchased"]*data["CostPerItem"]

data["ProfitPerTransaction"]=data["SalesPerTransaction"]-data["CostPerTransaction"]

data["MarkUp"]=data["ProfitPerTransaction"] /data["CostPerTransaction"]

#===================================================================================

#rounding values with a decimal data type

data["MarkUp"]=round(data['MarkUp'],2)


#Changing the data type of values in the dataset


day= data["Day"].astype(str)
month= data["Month"].astype(str)
year= data["Year"].astype(str)

#other way to check the data type of a value
print(month.dtype)

date= day +"-"+month+"-"+year

data["date"]= date


#==================================================================================
#using iloc function

#Both column and row start to count at 0

data.iloc[0]#Info of index 0 showing data

#head() means showing the first five rows in the dataset
data.head()


#tail() means showing the last five rows in the dataset
data.tail()

#the number 4 inside the bracket stands for the row number 5 in the dataset
# and the number 7 stands for the column 8
data.iloc[4,7]


#Spliting the column

split_to_column= data["ClientKeywords"].str.split(",",expand=True)

data["AgeType"]= split_to_column[0]

data["ClientType"]= split_to_column[1]

data["LenghtOfContract"]= split_to_column[2]


#===============================================================================
#using replace function 

data["AgeType"] = data["AgeType"].str.replace("[","")

data["AgeType"] = data["AgeType"].str.replace("'","")


data["ClientType"] = data["ClientType"].str.replace("'","")

data["LenghtOfContract"] = data["LenghtOfContract"].str.replace("'","")

data["LenghtOfContract"] = data["LenghtOfContract"].str.replace("]","")



data.info()
#using the lower function to chage the format of the letters

data["ItemDescription"]= data["ItemDescription"].str.lower()

#importing new dataset

seasons=pd.read_csv('C:/Users/EZRA/Downloads/Python and Tableau Course/value_inc_seasons.csv')

seasons=pd.read_csv('C:/Users/EZRA/Downloads/Python and Tableau Course/value_inc_seasons.csv',sep=";")

#=====================================================================================================+
#merging two datasets

seasons.info()

data=pd.merge(data,seasons, on = "Month")

#Deleting or Droping columns

data=data.drop("Year",axis = 1)
data=data.drop("Month",axis = 1)
data=data.drop("Day",axis = 1)
data=data.drop("ClientKeywords",axis = 1)


#export data to csv

data.to_csv('ValueIncClean.csv',index= False)




































































































