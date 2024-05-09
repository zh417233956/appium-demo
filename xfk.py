from appiumHelper import AppiumHelper
import time
import threading
from appium.options.android import UiAutomator2Options
from appium.webdriver.extensions.android.activity_start import start_activity
apih = AppiumHelper()



def t1():
    try:
        apih.desired_caps = {
                "deviceName": "127.0.0.1:16384",
                "udid": "127.0.0.1:16384",
                "platformName": "Android",
                "appPackage": "com.f101.android",
                "noReset": True,
                "dontStopAppOnReset": True,
                "autoGrantPermissions": True,
                "appActivity": "com.ss.android.article.lite.activity.SplashActivity",
                "appium:automationName": "uiautomator2"
                }

        driver= apih.get_driver("http://127.0.0.1:4723")
        while True:
            print(f"001")
            driver.activate_app('com.f101.android/com.ss.android.article.lite.activity.SplashActivity')
            time.sleep(2)            
            print(f"002")
           
            # driver.activate_app('com.f101.android/com.ss.android.article.lite.activity.SplashActivity --user 11')
            
            # 启动另一个用户下的应用程序
            driver.start_activity(app_package='com.f101.android', app_activity='com.ss.android.article.lite.activity.SplashActivity', user_id=11)
      
            time.sleep(2)            
            print(f"003")
            apih.find_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView").click()
            # apih.find_by_xpath(driver,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[5]/android.widget.ImageView").click()
    except  Exception as e:
        print(f"1111 - {e}")
print(f"000")
t1()