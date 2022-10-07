# 北航健康填报自动脚本
# blacklerwin@gmail.com


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os
import time


# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 访问res文件夹下a.txt的内容
filename = resource_path(os.path.join("res", "info.txt"))
infofile = open(filename, "r")
info = infofile.readlines()
username = info[0]
password = info[1]


# 设置webdriver
option = webdriver.ChromeOptions()
option.add_argument("--auto-open-devtools-for-tabs")
driver = webdriver.Chrome(chrome_options=option)  # Optional argument, if not specified will search path.
driver.execute_cdp_cmd("Browser.grantPermissions",
    {
        "origin": "https://app.buaa.edu.cn/",
        "permissions": ["geolocation"]
    },
)
# 打卡点经纬度
geo = {
    "latitude": float(info[3]),
    "longitude": float(info[4]),
    "accuracy": 100
}
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", geo) # 设置经纬度
# 打开url
driver.get("https://app.buaa.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.buaa.edu.cn%2Fsite%2FbuaaStudentNcov%2Findex")
driver.implicitly_wait(2)
now_handle = driver.current_window_handle
driver.switch_to.window(now_handle)
# 清除输入框内容、输入账号密码，需自行修改
driver.find_element("xpath", "//input[@type='text']").clear()
driver.find_element("xpath", "//input[@type='password']").clear()
driver.find_element("xpath", "//input[@type='text']").send_keys(username)	# 账号
driver.find_element("xpath", "//input[@type='password']").send_keys(password)	# 密码
# 点击登陆按钮
driver.find_element("xpath", "//div[@class='btn']").click()
#WebDriverWait(driver, timeout=10).until(lambda d: d.find_element("xpath", "//div[@class='sub-info']"))

driver.implicitly_wait(10)
time.sleep(2)
# 至多等待10秒

# error的自动处理


# 校外打卡
position = int(info[2])
if position == 1:
    driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/span[1]").click()
    driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/span[1]").click()
    driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/div[5]/span[1]").click()
# 获取地理位置
driver.find_element("xpath", "//input[@type='text']").click()
driver.implicitly_wait(5)
time.sleep(3)
# 提交
driver.find_element("xpath", "//div[@class='sub-info']").click()
driver.find_element("xpath", "//div[@class='wapcf-btn wapcf-btn-ok']").click()
# 退出
driver.quit()
print("打卡成功")

