import wx
from person import newUser
from firstWindow import firstWindow
from secondWindow import secondWindow
class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="Login")
        self.logged_in = False#больше не нужно, но вдруг пригодится
        
        
        # user info
        user_sizer = wx.BoxSizer(wx.HORIZONTAL)#хз но походу окно авторизации 

        user_lbl = wx.StaticText(self, label="Username:")
        user_sizer.Add(user_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.user = wx.TextCtrl(self)#вводится имя пользователя
        
        user_sizer.Add(self.user, 0, wx.ALL, 5)

        # pass info
        p_sizer = wx.BoxSizer(wx.HORIZONTAL)

        p_lbl = wx.StaticText(self, label="Password:")
        p_sizer.Add(p_lbl, 0, wx.ALL|wx.CENTER, 5)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)#вводится пароль пользователя

        self.password.Bind(wx.EVT_TEXT_ENTER, self.onLogin)#бинд на энтер входза пускающая ивент входа
        p_sizer.Add(self.password, 0, wx.ALL, 5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(user_sizer, 0, wx.ALL, 5)
        main_sizer.Add(p_sizer, 0, wx.ALL, 5)

        btn = wx.Button(self, label="Login")#кнопка входа запускающая ивент входа
        btn.Bind(wx.EVT_BUTTON, self.onLogin)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def onLogin(self, event):#собсна сам ивент входа
        """
        Check credentials and login
        """
        user_name = str(self.user.GetValue()).strip() #имя пользователя
        user_password = int(self.password.GetValue())#пароль пользователя
        if user_name == newUser.userName and user_password == newUser.pssword:#сравниваем с данными чипиздрика
            print("You are now logged in!")
            if newUser.perm == 1:
                fw = firstWindow()
                fw.Show()
            else: 
                sw = secondWindow()
                sw.Show()
                
            self.Close()
        else:
            print("Username or password is incorrect!")
