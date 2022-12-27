import wx
class TaskWindow(wx.Frame):
    def __init__(self, name, discriprion):
        wx.Frame.__init__(self, None, title=name)#окно задания
        self.name = name
        self.discription = discriprion
        
