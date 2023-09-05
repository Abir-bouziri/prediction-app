import pickle
import pandas as pd 
import numpy as np

def prediction(l):
 data=np.array(l).reshape(1,4)
 print(data)
 pickle_model=pickle.load(open('iris.pkl','rb'))
 result=pickle_model.predict(data)
 return result




