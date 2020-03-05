import pandas as pd
import os
from sklearn.utils import shuffle
dir=os.path.dirname(os.path.realpath('__file__')) #getting relative path
dirname = os.path.join(dir, 'ANDROID','android_training') #moving to training dataset for all gestures
list = os.listdir(dirname) #refrencing all files of dir into list
print(list)
number_files = len(list) #checking content length of list
print (number_files,list)
df=pd.DataFrame(columns=["x","y","z"]) #dataframe which will have x,y,z variance of all gestures
for i in range(len(list)): #looping the training data
    file=os.path.join(dirname, list[i])
    data = pd.read_csv(file, sep=" ", names=['x','y','z'],header=None) #reading traing data txt file: values seperated by space->dataframe
    target = [i]*len(data)
    data["target"]=target
    df=df.append(data,ignore_index=True)
print(df)
df=shuffle(df)
from sklearn.model_selection import train_test_split 
X=df.drop(columns="target",axis=1) #seperating variance and target
Y=df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2) #splitting 80% to train and 2% to test
from sklearn.svm import SVC
svc=SVC()
svc.fit(X_train,y_train) #training
pred=svc.predict(X_test) #predict
print(pred)
from sklearn.metrics import accuracy_score
print (accuracy_score(y_test, pred)) #i dont know how 100% acc. , it changes with train_test_split
dir=os.path.dirname(os.path.realpath('__file__')) #getting relative path
dirname = os.path.join(dir, 'ANDROID','models')
list = os.listdir(dirname)
print(list)
max=0
for i in list:
    if int(i[12:])>max:
        max=int(i[12:])
max+=1
import pickle
with open(dirname+'/model_pickle'+str(max),'wb') as f:
    pickle.dump(svc,f)