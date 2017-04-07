
# coding: utf-8

# # Q3_PartOne : CRICKET MATCHES ANALYSIS
# # Calculate the average score for each team which host game and win game.
# # Display a few rows of the output use df.head ().

# In[1]:

#Importing CSV.
import csv


# In[2]:

#Importing Pandas.
import pandas as pd


# In[3]:

dataFrame=pd.read_csv('D:/Users/vin/Desktop/Rohini/cricket_matches.csv') #Reading the CSV file.
newDataFrame=dataFrame[['home','winner','innings1','innings1_runs','innings2','innings2_runs']] #Fetching the necessary columns.


# In[4]:

winner=newDataFrame[newDataFrame['home']==newDataFrame['winner']]


# In[5]:

winner['Filtered_Scores'] = winner['innings1_runs'].where(winner['innings1'] == winner['home'], winner['innings2_runs'])


# In[6]:

output=winner.groupby('home')['Filtered_Scores'].mean().reset_index()


# In[9]:

output.head()


# In[10]:

output.to_csv('D:/Users/vin/Desktop/Rohini/Q3_Part1.csv')


# In[ ]:




# In[ ]:



