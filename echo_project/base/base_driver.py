#coding=utf-8
from appium import webdriver
import time
class make_driver():
    def Android_driver(self):
        desired_caps={
            "platformName":"Android",
            "deviceName":"dbfc611",
            "patformVerson":"8.1",
            "app":"D:\echo_1.11.1_201903251357_release.apk",
        }
        driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        time.sleep(2)
        return driver
