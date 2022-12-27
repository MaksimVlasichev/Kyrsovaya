import wx
import random
class TaskWindow(wx.Frame):
    def __init__(self, name, discriprion):
        wx.Frame.__init__(self, None, title=name)#окно задания
        self.name = name
        self.discription = discriprion
        self.Status = random.randint(1,5)
        self.remove = random.randint(0,1)
        
