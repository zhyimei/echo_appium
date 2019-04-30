#coding=utf-8
from base.base_driver import make_driver
from appium import webdriver

class login():
    def __init__(self):
        basedriver=make_driver()
        self.driver=basedriver.Android_driver()

    def login_pass(self):
        self.driver.find_element_by_id("online.skyplan.echo:id/login_wechat_image").click()

    def check_useragreement(self):
        self.driver.find_element_by_id("online.skyplan.echo:id/login_protocol_agree").click()
if __name__ == '__main__':
    a=login()
    a.login_pass()