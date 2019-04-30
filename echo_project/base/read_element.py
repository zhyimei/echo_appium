#coding=utf-8
import ConfigParser

class read_element_base():
    def __init__(self,filepath=None):
        if filepath==None:
            self.filepath="C:\Users\zhyimei\PycharmProjects\echo_project\config\element_base.ini"
        else:
            self.filepath=filepath
        self.data=self.read_login_element()
    def read_login_element(self):
        read_login_element=ConfigParser.ConfigParser()
        read_login_element.read(self.filepath)
        print read_login_element.get("login_element","wechat_loginbutton")
        return read_login_element
# a=read_element_base()
# a.read_login_element()