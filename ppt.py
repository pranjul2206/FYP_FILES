import win32com.client
app = win32com.client.Dispatch("PowerPoint.Application")
presentation = app.Presentations.Open(FileName=u'C:\\Users\\PRANJUL\\Desktop\\FYP\\controlling_ppt\\test.pptx', ReadOnly=1)

presentation.SlideShowSettings.Run()
while(True):
    num=int(input("enter command"))
    if num==1:
        presentation.SlideShowWindow.View.Next()
    elif num==2:
        presentation.SlideShowWindow.View.Previous()
    else:
        presentation.SlideShowWindow.View.Exit()
        app.Quit()
