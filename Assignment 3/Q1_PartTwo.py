
# coding: utf-8

# # Q1_PartTwo : NYC VEHICLE COLLISION ANALYSIS
# # For each borough, find out distribution of collision scale. (One car For each borough, find out distribution of collision scale. (One car For each borough, find out distribution of collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
# # Display a few rows of the output use df.head ().
# # Generate a csv output with five columns ('borough', 'one-vehicle', 'two vehicle','three -vehicles', 'more vehicles')

# In[1]:

#Importing CSV.
import csv


# In[2]:

#Importing Pandas.
import pandas as pd


# In[4]:

#Reading the "vehicle_collisions.csv" CSV file.
dataFrame=pd.read_csv('D:/Users/vin/Desktop/Rohini/vehicle_collisions.csv')


# In[5]:

dataFrame['DATE'] = pd.to_datetime(dataFrame['DATE']) #Convertion of datatype of DATE field in the Data Frame to proper data-time format is being done here.


# In[9]:

newDataFrame=dataFrame[(dataFrame.DATE > '2014-12-31')] #Getting all the records of the year '2015- present and storing it in the newDataFrame.


# In[14]:

temporaryDataFrame=newDataFrame.groupby('BOROUGH')['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'].count().reset_index()
# Temp dataset is created to store the temp values of vehicles.


# In[15]:

#Empty dataframe is created with column as 'Borough'.
emptySet=pd.DataFrame()
emptySet['BOROUGH']=temporaryDataFrame.iloc[:,[0]]


# In[16]:

emptySet['One_Vehicle_Involved']=temporaryDataFrame['VEHICLE 1 TYPE']-temporaryDataFrame['VEHICLE 2 TYPE']
emptySet['Two_Vehicles_Involved']=temporaryDataFrame['VEHICLE 2 TYPE']-temporaryDataFrame['VEHICLE 3 TYPE']
emptySet['Three_Vehicles_Involved']=temporaryDataFrame['VEHICLE 3 TYPE']-temporaryDataFrame['VEHICLE 4 TYPE']
emptySet['More_Vehicles_Involved']=temporaryDataFrame['VEHICLE 4 TYPE']


# In[18]:

emptySet.head()


# In[19]:

emptySet.to_csv('D:/Users/vin/Desktop/Rohini/Q1_Part2.csv')


# In[ ]:



