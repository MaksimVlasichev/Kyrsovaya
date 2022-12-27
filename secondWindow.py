import wx
from MyPanel import *
from LoginDialog import *
from person import newUser
class secondWindow(wx.Frame):
    """"""

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="second Window", size = (1000,750))#пока пустое окно одного из сотрудников
        panel = MyPanel(self)

        # Ask user to login
        # self.Show()
