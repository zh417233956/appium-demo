from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

"""
    谢恩
    2023-08-21
    封装一些用到的Appium方法
"""
class AppiumHelper:

    def __init__(self):

        """
            deviceName 设备名
            platformName 系统
            platformVersion 版本
            appPackage 包名
            noReset 保持session
            dontStopAppOnReset 不关闭应用
            autoGrantPermissions 自动获取权限
            appActivity 主启动函数

        """
        self.desired_caps = {
            'deviceName'    :'127.0.0.1:21503',
            # "udid": '127.0.0.1:21503',
            'platformName'  :'Android',
            'appPackage'    : 'com.tencent.mm',
            'noReset'       : True,
            'dontStopAppOnReset':True,
            'autoGrantPermissions':True,
            'appActivity':'com.tencent.mm.ui.LauncherUI'
            }
        
    def  get_driver(self,url):
        try:
            #'http://127.0.0.1:4723/wd/hub'
            # url = url + "/wd/hub"
            # url = url + "/"
            options = UiAutomator2Options().load_capabilities(self.desired_caps)
            return  webdriver.Remote(url, options=options)
        except Exception as e:
            raise Exception(f"get_driver - {e} ")

    def find_by_id(self,dirver,id):
        try:
            return  dirver.find_element(dirver,By.ID,id)
        except Exception as e:
            raise Exception(f"find_by_id - {e.args} ")
        

    def find_by_ids(self,dirver,id):
        try:
            return dirver.find_elements(By.ID,id)
        except Exception as e:
            raise Exception(f"find_by_ids - {e.args} ")
        

    def find_by_xpath(self,dirver,xpath):
        try:
            return dirver.find_element(By.XPATH,xpath)
        except Exception as e:
            raise Exception(f"find_by_xpath - {e.args} ")
        

    def find_by_xpaths(self,dirver,xpath):
        try:
            return dirver.find_elements(By.XPATH,xpath)
        except Exception as e:
            raise Exception(f"find_by_xpaths - {e.args} ")

    def find_by_class(self,dirver,name):
        try:
            return dirver.find_element(By.CLASS_NAME,name)
        except Exception as e:
            raise Exception(f"find_by_class - {e.args} ")
        

    def find_by_classs(self,dirver,name):
        try:
            return dirver.find_elements(By.CLASS_NAME,name)
        except Exception as e:
            raise Exception(f"find_by_classs - {e.args} ")

    def element_find_by_xpaths(self,element,xpath):
        try:
            return element.find_elements(By.XPATH,xpath)
        except Exception as e:
            raise Exception(f"element_find_by_xpaths - {e.args} ")

    def element_find_by_clsname(self,element,name):
        try:
            return element.find_elements(By.CLASS_NAME,name)
        except Exception as e:
            raise Exception(f"element_find_by_clsname - {e.args} ")
            
    def ec_find_xpah(self,driver,xpath):
        try:
            return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            raise Exception(f"ec_find_xpah - {e.args} ")
        
    def ec_find_id(self,driver,xpath):
        try:
            return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, xpath)))
        except Exception as e:
            raise Exception(f"ec_find_xpah - {e.args} ")
        
    def get_current_activity(self,driver):
        try:
            return driver.current_activity
        except Exception as e:
            raise Exception(f"get_current_activity - {e.args} ")