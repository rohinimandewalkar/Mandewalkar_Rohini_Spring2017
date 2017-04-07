
# coding: utf-8

#  # Q1_PartOne: NYC VEHICLE COLLISION ANALYSIS 
# # For each month in 2016, find out the percentage of collisions for each month in Manhattan out of that year's total accidents in New York City.
# # Display a few rows of the output use df.head ().
# # Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)
# 

# In[ ]:

# Importing CSV.
import csv


# In[ ]:

#Importing Pandas.
import pandas as pd


# In[ ]:

#Importing Calendar.
import calendar


# In[ ]:

dataFrame=pd.read_csv('D:/Users/vin/Desktop/Rohini/vehicle_collisions.csv') #Reading the CSV file.


# In[ ]:

dataFrame['DATE'] = pd.to_datetime(dataFrame['DATE']) #Convertion of datatype of DATE field in the Data Frame to proper data-time format is being done here.


# In[ ]:

dataFrame['Month'] = dataFrame['DATE'].dt.month #Creating a column called 'Month' in the dataFrame by taking the 'Month' part from the DATE column in the dataFrame.


# In[ ]:

newDataFrame=dataFrame[(dataFrame.DATE > '2015-12-31') & (dataFrame.DATE < '2017-01-01')] #Getting all the records of the year '2016' and storing it in the newDataFrame.


# In[ ]:

collisions=newDataFrame.groupby('Month')['UNIQUE KEY'].count().reset_index(name='NYC') #Getting the collisions in NYC and storing it in collisions data frame.


# In[ ]:

# Getting "Manhattan" records.
newDataFrame2=newDataFrame[newDataFrame.BOROUGH=='MANHATTAN']


# In[ ]:

#Getting the collisions in 'Manhattan' and storing it in collisions 2 data frame.
collisions2=newDataFrame2.groupby('Month')['UNIQUE KEY'].count().reset_index(name='MANHATTAN')


# In[ ]:

mergedDataFrame=pd.merge(collisions, collisions2, on='Month', how='outer') #Combing 'collisions' and 'collisions2' data frames.


# In[ ]:

mergedDataFrame['PERCENTAGE']=mergedDataFrame.MANHATTAN/mergedDataFrame.NYC #Creating a column named 'Percentage' that is going to store the percentage of collisions in Manhattan out of that year's total accidents in the NYC.


# In[ ]:

mergedDataFrame['Month'] = mergedDataFrame['Month'].apply(lambda x: calendar.month_name[x]) #Replacing the digits present in 'Month' field with words in 'Calendar' library present in the mergedDataFrame.


# In[ ]:

mergedDataFrame.head()


# In[ ]:

mergedDataFrame.to_csv('D:/Users/vin/Desktop/Rohini/Q1_Part1.csv')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



