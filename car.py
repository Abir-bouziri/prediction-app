import pandas as pd 
import numpy as np 
import seaborn as sbn
data=pd.read_csv('C:/Users/bouzi/OneDrive/Documents/dataset/CarPrice_Assignment.csv')
#print(data)
# the first row in data set 
#print(data.head())
#data processing 
#print(data.describe())
# show all the unique value each columns 
#print(data.CarName.value_counts() )
#This function also gives a boolean value if 
# any null value is present or not, but it 
# gives results column-wise, not in tabular 
# format.
#print(data.isna().any())
#la sum des valeurs null  ;combien de valeur null 
#print(data.isna().sum())
#effacer les valeurs  dupliquée
#print(data.drop_duplicates() )
import matplotlib.pyplot as plt
#data visualisation 
#print(data.enginelocation.value_counts())
#print(data.symboling.value_counts() )
data=data.drop('car_ID',axis=1)
print(data.drop('symboling',axis=1))
# nuumber des marque
plt.figure()
sbn.countplot(y= data.CarName,size=15)
plt.title("Car companies with their cars", fontsize = 20)
plt.show()