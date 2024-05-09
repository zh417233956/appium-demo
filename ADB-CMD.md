> 安装如下：
```
安装包：pip install virtualenv
创建沙箱：virtualenv venv
linux系统：. venv/bin/activate / 
windows系统：venv\Scripts\activate 
关闭：deactivate

> pip安装 install
导出包依赖表：pip freeze > requirements.txt

安装requirements.txt依赖
pip install -r requirements.txt




# Install an official plugin from npm (see documentation for a list of such plugins)
appium plugin install <plugin-name>
# Install any plugin from npm
appium plugin install --source=npm <plugin-name>
# See documentation for installation from other sources

appium driver list --installed

# List already installed plugins
appium plugin list --installed
# Update a plugin (it must be already installed)
# This will NOT update the major version, in order to prevent breaking changes
appium plugin update <plugin-name>
# Update a plugin to the most recent version (may include breaking changes)
appium plugin update <plugin-name> --unsafe
# Uninstall a plugin
appium plugin uninstall <plugin-name>

# Start the server on the default host (0.0.0.0) and port (4723)
appium server
# You can also omit the 'server' subcommand
appium
# Start the server on the given host, port and use a custom base path prefix (the default prefix is '/')
appium --address 127.0.0.1 --port 9000 --base-path /wd/hub




adb shell getprop ro.build.version.release  # 获取PlatformVersion

adb devices -l  # 获取deviceName

# 获取activity
adb shell dumpsys activity | findstr "realActivity"|more
dumpsys package your.package.name|grep Activity|more

adb shell dumpsys activity | findstr "mResume"  # 获取appPackage和appActivity 
# 或  # 获取appPackage和appActivity   
adb  -s 127.0.0.1:16384 shell dumpsys activity | findstr "mFocusedWindow"

# 切换用户
adb shell am switch-user {user_id}
# 切换应用
adb shell am start -n com.f101.android/com.ss.android.article.lite.activity.SplashActivity
# 强制停止当前应用程序实例
adb shell am force-stop com.f101.android


adb shell input keyevent KEYCODE_APP_SWITCH

adb shell input keyevent KEYCODE_HOME

```
# Appium Inspector 配置
```
{
  "appium:deviceName": "127.0.0.1:16384",
  "appium:udid": "127.0.0.1:16384",
  "platformName": "Android",
  "appium:appPackage": "com.f101.android",
  "appium:noReset": true,
  "appium:dontStopAppOnReset": true,
  "appium:autoGrantPermissions": true,
  "appium:appActivity": "com.ss.android.article.lite.activity.SplashActivity",
  "appium:automationName": "uiautomator2",
  "appium:newCommandTimeout": "360000"
}
```
```
查看用户列表  
adb shell pm list users

查看用户信息：
adb shell dumpsys user

创建新用户  
adb shell pm create-user [–profileOf userId] [–managed] USER_NAME
例：adb shell pm create-user 10 user2

–profileOf userId：可选参数，用于指定新用户的配置文件。新用户将会继承指定用户的配置文件。如果不提供此参数，则新用户将拥有默认的配置文件。
–managed：可选参数，指定新用户是否是受管理的。如果提供了此参数，则新用户将是受管理的，否则将是普通用户。

启动和切换用户
adb shell am switch-user userId
adb shell am start-user userId

安装应用到某个用户下
adb install --user userId xxx.apk

删除用户
adb shell pm remove-user userId

为特定用户卸载软件包
adb uninstall --user <userId> <Pckage>

获取当前（前台）用户 ID
adb shell am get-current-user

为特定用户列出软件包（-e 可列出已启用的软件包，-d 可列出已停用的软件包）。
默认情况下，此命令始终为系统用户列出软件包。
adb shell pm list packages --user <userId>
————————————————
                        
原文链接：https://blog.csdn.net/qq_45649553/article/details/135110663
```
# 滑动
```
滑动

1.命令：adb input swipe 600 800 300 800（向右滑动）

2.命令：adb input swipe 300 800 600 800（向左滑动）

3.命令：adb input swipe 300 80 300 800（向下滑动）

4.命令：adb input swipe 300 800 300 80（向上滑动）

5.命令：adb input swipe 300 800 300 80 1000（向上滑动1000）

点击

此x、y坐标对应的是真实的屏幕分辨率，所以要根据具体手机具体看，比如你想点击屏幕(x, y) = (250, 250)位置：

adb shell input tap 250 250

adb shell input tap 600 600  点击位置（mt）

adb shell input keyevent 4    返回键

最后一个是事件参数，以下是对照表:

0 --> "KEYCODE_UNKNOWN"
1 --> "KEYCODE_MENU"
2 --> "KEYCODE_SOFT_RIGHT"
3 --> "KEYCODE_HOME"
4 --> "KEYCODE_BACK"
5 --> "KEYCODE_CALL"
6 --> "KEYCODE_ENDCALL"
7 --> "KEYCODE_0"
8 --> "KEYCODE_1"
9 --> "KEYCODE_2"
10 --> "KEYCODE_3"
11 --> "KEYCODE_4"
12 --> "KEYCODE_5"
13 --> "KEYCODE_6"
14 --> "KEYCODE_7"
15 --> "KEYCODE_8"
16 --> "KEYCODE_9"
17 --> "KEYCODE_STAR"
18 --> "KEYCODE_POUND"
19 --> "KEYCODE_DPAD_UP"
20 --> "KEYCODE_DPAD_DOWN"
21 --> "KEYCODE_DPAD_LEFT"
22 --> "KEYCODE_DPAD_RIGHT"
23 --> "KEYCODE_DPAD_CENTER"
24 --> "KEYCODE_VOLUME_UP"
25 --> "KEYCODE_VOLUME_DOWN"
26 --> "KEYCODE_POWER"
27 --> "KEYCODE_CAMERA"
28 --> "KEYCODE_CLEAR"
29 --> "KEYCODE_A"
30 --> "KEYCODE_B"
31 --> "KEYCODE_C"
32 --> "KEYCODE_D"
33 --> "KEYCODE_E"
34 --> "KEYCODE_F"
35 --> "KEYCODE_G"
36 --> "KEYCODE_H"
37 --> "KEYCODE_I"
38 --> "KEYCODE_J"
39 --> "KEYCODE_K"
40 --> "KEYCODE_L"
41 --> "KEYCODE_M"
42 --> "KEYCODE_N"
43 --> "KEYCODE_O"
44 --> "KEYCODE_P"
45 --> "KEYCODE_Q"
46 --> "KEYCODE_R"
47 --> "KEYCODE_S"
48 --> "KEYCODE_T"
49 --> "KEYCODE_U"
50 --> "KEYCODE_V"
51 --> "KEYCODE_W"
52 --> "KEYCODE_X"
53 --> "KEYCODE_Y"
54 --> "KEYCODE_Z"
55 --> "KEYCODE_COMMA"
56 --> "KEYCODE_PERIOD"
57 --> "KEYCODE_ALT_LEFT"
58 --> "KEYCODE_ALT_RIGHT"
59 --> "KEYCODE_SHIFT_LEFT"
60 --> "KEYCODE_SHIFT_RIGHT"
61 --> "KEYCODE_TAB"
62 --> "KEYCODE_SPACE"
63 --> "KEYCODE_SYM"
64 --> "KEYCODE_EXPLORER"
65 --> "KEYCODE_ENVELOPE"
66 --> "KEYCODE_ENTER"
67 --> "KEYCODE_DEL"
68 --> "KEYCODE_GRAVE"
69 --> "KEYCODE_MINUS"
70 --> "KEYCODE_EQUALS"
71 --> "KEYCODE_LEFT_BRACKET"
72 --> "KEYCODE_RIGHT_BRACKET"
73 --> "KEYCODE_BACKSLASH"
74 --> "KEYCODE_SEMICOLON"
75 --> "KEYCODE_APOSTROPHE"
76 --> "KEYCODE_SLASH"
77 --> "KEYCODE_AT"
78 --> "KEYCODE_NUM"
79 --> "KEYCODE_HEADSETHOOK"
80 --> "KEYCODE_FOCUS"
81 --> "KEYCODE_PLUS"
82 --> "KEYCODE_MENU"
83 --> "KEYCODE_NOTIFICATION"
84 --> "KEYCODE_SEARCH"
85 --> "TAG_LAST_KEYCODE"

cmd /c  f:\\adb\\adb.exe shell input tap 500 500  运行cmd 执行指定文件夹下的命令
```
