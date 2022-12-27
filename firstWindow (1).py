import wx
import wx.lib.scrolledpanel
from MyPanel import *
from LoginDialog import *
from TaskWindow import TaskWindow
from person import newUser
class firstWindow(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="first Window")#пока пустое окно одного из сотрудников
        self.panel = MyPanel(self)
        self.Maximize(True)
        buttons = []
        buttons_ID = []
        for i in range(10):
            buttons.append(i)
            buttons_ID.append(wx.NewId())
        self.button = []
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(1000,750), pos=(300,0), style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        bSizer = wx.BoxSizer(wx.VERTICAL)


        for i in range(10):
            buttons[i] = wx.Button(panel2, label=("Task №"+ str(buttons[i])),pos=(0,0),size=(950,100))
            buttons[i].Bind(wx.EVT_BUTTON, self.OnButton)
            bSizer.Add(buttons[i], 0, wx.ALL, 5)
        panel2.SetSizer(bSizer)
        
    def OnButton(self, event):
        Id = event.GetId()
        Obj = event.GetEventObject()
        taskWindow = TaskWindow(Obj.GetLabelText(), "same discription")
        taskWindow.Show(True)
        print ("Button Id",Id)
        print ("Button Pressed:",Obj.GetLabelText())
