import wx
import json

class RegisterFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(RegisterFrame, self).__init__(*args, **kw) 
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        username_label = wx.StaticText(panel, label="Username:")
        self.username_text = wx.TextCtrl(panel)

        password_label = wx.StaticText(panel, label="Password:")
        self.password_text = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        register_button = wx.Button(panel, label="Register")
        register_button.Bind(wx.EVT_BUTTON, self.OnRegister)

        vbox.Add(username_label, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(self.username_text, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(password_label, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(self.password_text, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(register_button, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        panel.SetSizer(vbox)

    def OnRegister(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()

        if username and password:
            try:
                with open('users.json', 'r+') as f:
                    users = json.load(f)
                    if username in users:
                        wx.MessageBox('Username already exists', 'Error', wx.OK | wx.ICON_ERROR)
                    else:
                        users[username] = password
                        f.seek(0)
                        json.dump(users, f)
                        wx.MessageBox('Registration successful', 'Info', wx.OK | wx.ICON_INFORMATION)
            except FileNotFoundError:
                with open('users.json', 'w') as f:
                    users = {username: password}
                    json.dump(users, f)
                    wx.MessageBox('Registration successful', 'Info', wx.OK | wx.ICON_INFORMATION)

def main():
    app = wx.App()
    RegisterFrame(None, title='Registration').Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
