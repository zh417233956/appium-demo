from appiumHelper import AppiumHelper
import time
import threading
import subprocess

apih = AppiumHelper()

def switch_and_start_user(user_id):
    # # 切换用户
    # switch_user_command = f"adb -s {deviceName} shell am switch-user {user_id}"
    # subprocess.run(switch_user_command, shell=True)
    # time.sleep(2)  # 等待一段时间确保用户切换完成

    # 启动应用程序
    start_app_command = f"adb -s {deviceName} shell am start -n com.f101.android/com.ss.android.article.lite.activity.SplashActivity --user {user_id}"
    subprocess.run(start_app_command, shell=True)
    time.sleep(2)  # 等待应用程序启动

deviceName = "127.0.0.1:16384"

def t1():
    try:
        apih.desired_caps = {
            "deviceName": deviceName,
            # "udid": "127.0.0.1:16384",
            "platformName": "Android",
            "appPackage": "com.f101.android",
            "noReset": True,
            "dontStopAppOnReset": True,
            "autoGrantPermissions": True,
            "appActivity": "com.ss.android.article.lite.activity.SplashActivity",
            "appium:automationName": "uiautomator2"
        }

        driver = apih.get_driver("http://127.0.0.1:4723")
        # driver = apih.get_driver("http://127.0.0.1:4724")
        
        while True:
            # switch_and_start_user(0)
            print(f"001")

            # //android.widget.EditText[@resource-id="com.f101.android:id/alq"]
            # apih.find_by_xpath(driver,'//android.widget.EditText[@resource-id="com.f101.android:id/alq"]').send_keys("130")
            # switch_and_start_user(10)  # 切换到用户 10 并启动应用
            # time.sleep(3)     
            apih.find_by_xpath(driver,'//android.widget.EditText[@resource-id="com.f101.android:id/alq"]').send_keys("188")       
            print(f"002")
            time.sleep(3) 
            # 你的其他操作
            # ...
            
    except Exception as e:
        print(f"Error: {e}")

print(f"000")
t1()
