import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
import pickle


data=pd.read_csv('cardio_train.csv',sep=';')
# data clean
data=data.dropna()
data = data.drop((data.query('height < 75 or height > 200')).index,axis=0)

# data normalize
data['year']=data['age']/365
data['year']=data['year'].round(0)
x=data.iloc[:,1:-2]

y=data['cardio']

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.3,random_state=1)

from sklearn.ensemble import RandomForestClassifier

model_random_forest=RandomForestClassifier()

model_random_forest.fit(xtrain,ytrain)

# model_random_forest.score(xtest,ytest)
with open('model_pickle','wb') as f:
    pickle.dump(model_random_forest,f)
with open('model_pickle','rb') as f:
    mp=pickle.load(f) 


def func(ZZZ):
    prediction=mp.predict(ZZZ)[0]
    return prediction
