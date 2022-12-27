import wx
from LoginDialog import LoginDialog
from MyPanel import MyPanel

if __name__ == "__main__":
    app = wx.App(False)#создаём само приложение
    dlg = LoginDialog()#окно логина
    dlg.ShowModal()#показываем статично(не заменяемое) окно логина
    dlg.Destroy()#закрываем окно логина
    app.MainLoop()#ну тип работу приложения делаем постоянную