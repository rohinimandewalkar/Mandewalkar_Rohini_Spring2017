
# coding: utf-8

# # Q4_PartOne 
# # You are supposed to extract data from the awards column in this dataset and split it into several columns.
# # - If a movie has 2 Oscar nominations and 4 won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2.You should also have total_won and nominated column which aggregates all the awards (won or nominated).

# In[15]:

#Importing CSV
import csv


# In[16]:

#Importing Pandas
import pandas as pd


# In[17]:

dataFrame=pd.read_csv('D:/Users/vin/Desktop/Rohini/movies_awards.csv') #Reading the CSV file.


# In[18]:

#Matching the patterns and getting the digits 
dataFrame['Oscar_Awards_Won']= dataFrame['Awards'].str.extract('Won (\d+) Oscar')
dataFrame['Oscar_Awards_Nominated']= dataFrame['Awards'].str.extract('Nominated for (\d+) Oscar')
dataFrame['GoldenGlobe_Awards_Won']= dataFrame['Awards'].str.extract('Won (\d+) Golden Globe')
dataFrame['GoldenGlobe_Awards_Nominated']= dataFrame['Awards'].str.extract('Nominated for (\d+) Golden Globe')


# In[19]:

dataFrame['Awards_Won'] = dataFrame['Awards'].str.extract('(\d+) win')
dataFrame['Awards_Nominated'] = dataFrame['Awards'].str.extract('(\d+) nomination')
dataFrame['Prime_Awards_Won']= dataFrame['Awards'].str.extract('Won (\d+) Primetime')
dataFrame['Prime_Awards_Nominated']= dataFrame['Awards'].str.extract('Nominated for (\d+) Primetime')
dataFrame['Bafta_Awards_Won']= dataFrame['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
dataFrame['Bafta_Awards_Nominated']= dataFrame['Awards'].str.extract('Nominated for (\d+) BAFTA')


# In[20]:

newDataFrame=dataFrame[[15,21,22,23,24,25,26,27,28,29,30]]


# In[21]:

newDataFrame['Awards_Won'] = newDataFrame['Awards_Won']+newDataFrame['Prime_Awards_Won']+newDataFrame['Bafta_Awards_Won']+newDataFrame['Oscar_Awards_Won']+newDataFrame['GoldenGlobe_Awards_Won']


# In[22]:

newDataFrame['Awards_Nominated']=newDataFrame['Awards_Nominated']+newDataFrame['Prime_Awards_Nominated']+newDataFrame['Bafta_Awards_Nominated']+newDataFrame['Oscar_Awards_Nominated']+newDataFrame['GoldenGlobe_Awards_Nominated']


# In[30]:

newDataFrame = newDataFrame.fillna(0)
newDataFrame['Awards_Won'] =newDataFrame['Awards_Won'].astype(str).astype(int)
newDataFrame['Awards_Nominated'] =newDataFrame['Awards_Nominated'].astype(str).astype(int) 
newDataFrame['Prime_Awards_Won']=newDataFrame['Prime_Awards_Won'].astype(str).astype(int)
newDataFrame['Prime_Awards_Nominated']=newDataFrame['Prime_Awards_Nominated'].astype(str).astype(int)
newDataFrame['Bafta_Awards_Won']=newDataFrame['Bafta_Awards_Won'].astype(str).astype(int) 
newDataFrame['Bafta_Awards_Nominated']=newDataFrame['Bafta_Awards_Nominated'].astype(str).astype(int)
newDataFrame['Oscar_Awards_Won']=newDataFrame['Oscar_Awards_Won'].astype(str).astype(int) 
newDataFrame['Oscar_Awards_Nominated']=newDataFrame['Oscar_Awards_Nominated'].astype(str).astype(int) 
newDataFrame['GoldenGlobe_Awards_Won']=newDataFrame['GoldenGlobe_Awards_Won'].astype(str).astype(int) 
newDataFrame['GoldenGlobe_Awards_Nominated']=newDataFrame['GoldenGlobe_Awards_Nominated'].astype(str).astype(int)


# In[31]:

newDataFrame.to_csv('D:/Users/vin/Desktop/Rohini/Q4_Part1.csv')


# In[ ]:




# In[ ]:




# In[ ]:



