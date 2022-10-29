# 北航校园网自动认证
# blacklerwin@gmail.com
# lerwinB

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os
import time


def isElementExist(driver1, element):
    flag = True
    driver1
    try:
        driver1.find_element("id", element)
        return flag
    except:
        flag = False
        return flag

username = "zy2215129"
password = "z8223850"


# 设置webdriver
option = webdriver.ChromeOptions()
option.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(chrome_options=option)  # Optional argument, if not specified will search path.
wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
# 打开url
driver.get("https://gw.buaa.edu.cn")
driver.implicitly_wait(2)
now_handle = driver.current_window_handle
driver.switch_to.window(now_handle)
# 清除输入框内容、输入账号密码，需自行修改

if isElementExist(driver, "logout-dm"):
    driver.quit()
    print("已登录")
else:
    driver.find_element("id", "username").clear()
    driver.find_element("id", "password").clear()
    driver.find_element("id", "username").send_keys(username)	# 账号
    driver.find_element("id", "password").send_keys(password)	# 密码
    # 点击登陆按钮
    driver.find_element("id", "login").click()
    #WebDriverWait(driver, timeout=10).until(lambda d: d.find_element("xpath", "//div[@class='sub-info']"))
    driver.implicitly_wait(10)
    time.sleep(4)
    # Store the alert text in a variable
    alert = driver.switch_to.alert #创建弹窗对象

    value = alert.text
    print(value)
    # Press the OK button
    alert.accept()
    driver.implicitly_wait(3)
    time.sleep(3)
    if isElementExist(driver, "logout-dm"):
        print("success")
        driver.quit()
    else:
        print("false")
        driver.quit()

