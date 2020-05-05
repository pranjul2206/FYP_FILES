import pandas as pd
import numpy
import os
import socket
import win32com.client


#root_path
dir=os.path.dirname(os.path.realpath('__file__'))
#data_collect dictionary
gesture_dict={'left':os.path.join(dir, 'ANDROID','gestures','left'),
         "right":os.path.join(dir, 'ANDROID','gestures','right'),
        "top":os.path.join(dir, 'ANDROID','gestures','top'),
        "bottom":os.path.join(dir, 'ANDROID','gestures','bottom')}

def predict():
    dirname = os.path.join(dir, 'ANDROID','models') #getting path name for model
    list = os.listdir(dirname) #refrence of elemt is path
    print(list)
    max=0 #obtaining max amongt complete list[latest=max]
    #choosing most recent model,In future user can chossse their own model with their accuracy
    for i in list:
        if int(i[12:])>max:
            max=int(i[12:])
    import pickle
    with open(dirname+'/model_pickle'+str(max),'rb') as f: #loading most recent model
        svc=pickle.load(f)
    xyz=finaldata.split()
    print(xyz)
    df=pd.DataFrame(columns=["x","y","z"])
    b={"x":xyz[0],"y":xyz[1],"z":xyz[2]} #testing with my own variances
    df=df.append(b,ignore_index=True)
    pred=svc.predict(df)
    controll=pred.astype(numpy.int64)
    print("predictions=",controll[0]) #prediction gesture1
    if controll[0]==0:
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
                    app = win32com.client.Dispatch("PowerPoint.Application")
                    presentation = app.Presentations.Open(FileName=u'C:\\Users\\PRANJUL\\Desktop\\FYP\\controlling_ppt\\test.pptx', ReadOnly=1)
                    presentation.SlideShowSettings.Run()
                    presentation.SlideShowWindow.View.Next()
                elif finaldata=="backward":
                    app = win32com.client.Dispatch("PowerPoint.Application")
                    presentation = app.Presentations.Open(FileName=u'C:\\Users\\PRANJUL\\Desktop\\FYP\\controlling_ppt\\test.pptx', ReadOnly=1)
                    presentation.SlideShowSettings.Run()
                    presentation.SlideShowWindow.View.Previous()
                elif finaldata[0]=="predicting":
                    predict(finaldata[1])
                elif finaldata[0]=="CaptureData":
                    print("here")
                    CaptureData(finaldata[1],finaldata[2:-1])
#                 elif finaldata[0]=="train":
# #                     trainmodel()
                    
                    
                                            