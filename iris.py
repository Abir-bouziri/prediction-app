import pandas as pd 
import numpy as np 
data=pd.read_csv('C:/Users/bouzi/OneDrive/Documents/dataset/iris.csv')
print(data)
print(data.shape)
data1=data.drop("Species",axis=1)
data2=data1.drop("Id",axis=1)
#print(np.array(data2))
#print('le',np.array(data.Species))
#data processing 
b=np.array(data.Species)
c=np.array(data2)
l=data.Species[data.Species =="Iris-setosa"].count()
m=data.Species[data.Species =="Iris-virginica"].count()
r=data.Species[data.Species =="Iris-versicolor"].count()
print(l)  
print(m)
print(r)
tab=np.array([l,m,r])
label=["Iris-setosa","Iris-virginica","Iris-versicolor"]
print((tab))
#data visualization
import matplotlib.pyplot as plt
p=np.array(data.Species)
print(p.shape)
plt.pie(tab,labels=label)
plt.show() 
#normalization 
from sklearn. preprocessing import MinMaxScaler
scaler=MinMaxScaler()
normdata=scaler.fit_transform(c)
#print("data",normdata.shape)
#print(normdata)
#data split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(normdata,b,test_size=0.2)
#print("traing data",x_train)
#print('test',y_train)
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)
test=model.predict(x_test)
print("x_test",x_test)
#print(test)
#evaluation
from sklearn.metrics import accuracy_score,confusion_matrix
print('Accurancy',accuracy_score(y_test,test))
print(confusion_matrix(y_test,test))
import pickle
pickle.dump(model,open('iris.pkl','wb'))


