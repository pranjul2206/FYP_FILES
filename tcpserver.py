import pandas as pd
import numpy
import os
import socket
import win32com.client
import pickle
import statistics


#root_path
dir=os.path.dirname(os.path.realpath('__file__'))
#data_collect dictionary
gesture_dict={'left':os.path.join(dir, 'ANDROID','gestures','left'),
         "right":os.path.join(dir, 'ANDROID','gestures','right'),
        "top":os.path.join(dir, 'ANDROID','gestures','top'),
        "bottom":os.path.join(dir, 'ANDROID','gestures','bottom')}

def predict(data_predict):
    print("in predict")
    print(data_predict)
    with open("SVM_pickle",'rb') as f: #loading most recent model
        svc=pickle.load(f)

    dfm=pd.DataFrame(columns=["x","y","z"])
    df_ans=pd.DataFrame(columns=["x","y","z"])
    for i in data_predict:
        arr=i.split()
        b={"x":float(arr[0]),"y":float(arr[1]),"z":float(arr[2])}
        dfm=dfm.append(b,ignore_index=True)
    df_ans=df_ans.append({"x":(statistics.pstdev(dfm["x"])),
        "y":(statistics.pstdev(dfm["y"])),
        "z":(statistics.pstdev(dfm["z"])),},ignore_index=True)
    print(df_ans)
    pred=svc.predict(df_ans)
    print(pred)
    controll=pred.astype(numpy.int64)
    print("predictions=",controll[0]) #prediction gesture1
    if controll[0]==3:
        presentation.SlideShowWindow.View.Next()
    elif controll[0]==1:
        presentation.SlideShowWindow.View.Previous()
    else:
        presentation.SlideShowWindow.View.Exit()
        app.Quit()


def CaptureData(gesture,datas):
    dirname=gesture_dict[gesture]
    l = len(os.listdir(dirname))
    with open(dirname+"\\"+str(l)+".txt",'a') as f: #loading most recent model
        for data in datas:
            f.write(data+"\n")
    print("gesture",gesture,"\ndatas",datas)
    
    
PORT = 7800
app = win32com.client.Dispatch("PowerPoint.Application")
presentation = app.Presentations.Open(FileName=u'C:\\Users\\PRANJUL\\Desktop\\FYP\\controlling_ppt\\test.pptx', ReadOnly=1)
presentation.SlideShowSettings.Run()

while(True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creating socket with ipv4 and port
        s.bind((socket.gethostname(), PORT))
        s.listen(5)
        conn, addr = s.accept() #conn having data and addr having ip
        with conn:
            print('Connected by', addr)
            while True:
                datatemp = conn.recv(1024) #recieving data
                data=datatemp.decode("utf-8") #b to charater utf-8 encoding
                finaldata=data.split('\n')
                if not datatemp:
                    break
                elif finaldata=="forward":
                    # app = win32com.client.Dispatch("PowerPoint.Application")
                    # presentation = app.Presentations.Open(FileName=u'C:\\Users\\PRANJUL\\Desktop\\FYP\\controlling_ppt\\test.pptx', ReadOnly=1)
                    # presentation.SlideShowSettings.Run()
                    # presentation.SlideShowWindow.View.Next()
                    print("commented hai, hatane se pehle global lines ko upar le jaana mat bhoolna")
                elif finaldata=="backward":
                    # app = win32com.client.Dispatch("PowerPoint.Application")
                    # presentation = app.Presentations.Open(FileName=u'C:\\Users\\PRANJUL\\Desktop\\FYP\\controlling_ppt\\test.pptx', ReadOnly=1)
                    # presentation.SlideShowSettings.Run()
                    # presentation.SlideShowWindow.View.Previous()
                    print("commented hai, hatane se pehle global lines ko upar le jaana mat bhoolna")
                elif finaldata[0]=="Predicting":
                    predict(finaldata[1:-1])
                elif finaldata[0]=="CaptureData":
                    print("here")
                    CaptureData(finaldata[1],finaldata[2:-1])
#                 elif finaldata[0]=="train":
# #                     trainmodel()
                    
                    
                                            