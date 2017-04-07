
# coding: utf-8

# # Q2_PartTwo : EMPLOYEE COMPENSATION ANALYSIS 
# # For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total Compensation). Create a new column to hold percentage value
# # Display top 5 job families depending on percentage using df.head ().

# In[1]:

#Importing CSV.
import  csv


# In[2]:

#Importing Pandas.
import pandas as pd


# In[3]:

dataFrame=pd.read_csv('D:/Users/vin/Desktop/Rohini/employee_compensation.csv') #Reading the CSV file.


# In[6]:

newDataFrame=dataFrame[dataFrame['Year Type']=='Calendar'] #Fetching the values with Year Type=Calendar.


# In[8]:

var1=newDataFrame.groupby(['Job Family','Employee Identifier']).mean().reset_index()
#Grouping the data based on Job Family and Employee Identifier and then calculating the mean.


# In[10]:

var1['Overtime_Salaries']=(var1.Overtime/var1.Salaries)*100
var2=var1[var1.Overtime_Salaries > 5]
#Poeple whose overtime salary is greater than 5% of salaries and then storing all the rows in a dataframe named var2.


# In[12]:

var3=var2.groupby('Job Family')['Total Benefits','Total Compensation'].mean().reset_index()
var3['Percent_Total_Benefit']=(var3['Total Benefits']/var3['Total Compensation'])*100
#Grouping by based on Total Benefits and Total Compensation and then taking the mean and calulating the percentage.
    


# In[13]:

var3.head()


# In[14]:

var3.to_csv('D:/Users/vin/Desktop/Rohini/Q2_Part2.csv')


# In[ ]:



