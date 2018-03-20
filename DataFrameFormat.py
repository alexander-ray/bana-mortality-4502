
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import glob

local_path = "mortality"
pd.set_option('display.max_columns',500)

#Load all .csv files in the mortality directory
all_files = glob.glob(local_path + "/*.csv")
dataframe = pd.DataFrame()
file_list = []

for file in all_files:
    df = pd.read_csv(file, index_col = None, header = 0, low_memory = False)
    dfInterest = df[['sex','detail_age','month_of_death','education_2003_revision','39_cause_recode']] #Isolate columns we need
    dfInterest['binary_suicide'] = np.where(dfInterest['39_cause_recode']==40, '1','0') #create the binary suicide column
    file_list.append(dfInterest) #add the new dataframe to the list

dataframe = pd.concat(file_list) #concat the whole list to the final dataframe
dataframe.drop('39_cause_recode',1)

dataframe.head()

#File loading method stack overflow link: https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
#All dataframe methods learned from pandas documentation
#np.where learned form numpy documentation

