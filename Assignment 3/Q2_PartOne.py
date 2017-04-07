
# coding: utf-8

# # Q2_PartOne : EMPLOYEE COMPENSATION ANALYSIS 
# # Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
# # Output should contain the organization group and departments in each organization group with the total compensation from highest to lowest()
# # Display a few rows of the output use df.head ().

# In[1]:

#Importing CSV.
import csv


# In[2]:

#Importing Pandas.
import pandas as pd


# In[3]:

dataFrame=pd.read_csv('D:/Users/vin/Desktop/Rohini/employee_compensation.csv') #Reading the CSV file.


# In[7]:

newDataFrame=dataFrame.groupby(['Organization Group','Department']).mean().reset_index() #Grouping the data based on Organization Group and Department and then calculating the mean..


# In[8]:

var1=newDataFrame[['Organization Group','Department','Total Compensation']]


# In[10]:

var1.head()


# In[11]:

var1.to_csv('D:/Users/vin/Desktop/Rohini/Q2_Part1.csv')


# In[ ]:



