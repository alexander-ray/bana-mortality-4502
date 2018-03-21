
# coding: utf-8

# In[26]:


#File loading method stack overflow link: https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
#All dataframe methods learned from pandas documentation
#np.where learned from numpy documentation

import numpy as np
import pandas as pd
import glob
import os
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, precision_score
from sklearn import preprocessing

filename = 'MortalityCondensed.csv'
pd.set_option('display.max_columns',500)
pd.options.mode.chained_assignment = None 

def process_files(local_path):
    #Load all .csv files in the mortality directory
    all_files = glob.glob(local_path + "/*.csv")
    dataframe = pd.DataFrame()
    file_list = []

    for file in all_files:
        
        df = pd.read_csv(file, index_col = None, header = 0, low_memory = False)
        dfInterest = df[['sex','race','detail_age','month_of_death','education_2003_revision','education_1989_revision','39_cause_recode']] #Isolate columns we need
        dfInterest['male'] = np.where(dfInterest['sex']=='M', 1, 0)
        dfInterest['binary_suicide'] = np.where(dfInterest['39_cause_recode']==40, 1, 0) #create the binary suicide column
        
        #Recode education to get rid of NaNs. Code 18 represents where we have no data.
        dfInterest['education_1989_revision'] = np.where(dfInterest['education_1989_revision'] <= 8, 1, dfInterest['education_1989_revision'])
        dfInterest['education_recode'] = np.where(type(dfInterest['education_2003_revision'])==str, dfInterest['education_1989_revision'], dfInterest['education_2003_revision'])
        dfInterest['education_recode'] = np.where(type(dfInterest['education_recode'])==str, 18, dfInterest['education_recode'])
        
        #Recode race to give us more meaningful categories 0 hispanic, 1 white, 2 black, 3 asian
        dfInterest['race_recode'] = np.where(dfInterest['race'] > 2, 3, dfInterest['race'])
        
        file_list.append(dfInterest) #add the new dataframe to the list

    dataframe = pd.concat(file_list) #concat the whole list to the final dataframe
    finaldf = dataframe.drop(columns=['39_cause_recode', 'sex','education_2003_revision','education_1989_revision'])

    finaldf.to_csv(filename)
    finaldf.head()

# To be expanded on later
def sample_classification():
    #alpha_arr = [0.0001,0.001,0.01,0.1,1.0,10.0,100.0]
    alpha_arr = [0.01]
    train_acc = []
    test_acc = []
    for a in alpha_arr:    
        classifier = SGDClassifier(loss='log', max_iter=1000, tol=1.0e-12, random_state=123, alpha=a)
        classifier.fit(X_train, Y_train)
        # Add to accuracy lists
        train_acc.append(accuracy_score(Y_train, classifier.predict(X_train)))
        test_acc.append(accuracy_score(Y_test, classifier.predict(X_test)))

    print(train_acc)
    print(test_acc)
    
def main():
    # Check if base_file exists
    # If not, create it
    if not os.path.isfile(filename):
        process_files("mortality")
    df = pd.read_csv(filename, header=0, encoding='ISO-8859-1')
    print(df.head())
    
    # Split into training and test
    # https://stackoverflow.com/questions/24147278/how-do-i-create-test-and-train-samples-from-one-dataframe-with-pandas
    msk = np.random.rand(len(df)) < 0.8
    train = df[msk]
    test = df[~msk]

    Y_train = train.iloc[:,len(train.columns)-1]
    X_train = train.iloc[:,1:(len(train.columns)-1)]
    Y_test = test.iloc[:,len(test.columns)-1]
    X_test = test.iloc[:,1:(len(test.columns)-1)]
    #sample_classification()
    
if __name__ == '__main__':
    main()

