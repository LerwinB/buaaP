# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# driver = webdriver.ie()
# option = webdriver.ChromeOptions()
# option.add_argument("--auto-open-devtools-for-tabs")
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
#driver = webdriver. # Optional argument, if not specified will search path.
#driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)

'''
driver.get('http://www.baidu.com/');

time.sleep(5) # Let the user actually see something!'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',

search_box = driver.find_element("name","wd")

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(10) # Let the user actually see something
driver.quit()
'''

# 选择Chrome浏览器

# 这是我学校的打卡网页，需自行修改
driver.get("https://app.buaa.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.buaa.edu.cn%2Fsite%2FbuaaStudentNcov%2Findex")
time.sleep(2) # Let the user actually see something!
# 这两步把操作界面切换到新打开的浏览器页面
now_handle = driver.current_window_handle
driver.switch_to.window(now_handle)

# 清除输入框内容、输入账号密码，需自行修改
driver.find_element("xpath", "//input[@type='text']").clear()
driver.find_element("xpath", "//input[@type='password']").clear()
driver.find_element("xpath", "//input[@type='text']").send_keys("ZY2215129")	# 账号
driver.find_element("xpath", "//input[@type='password']").send_keys("z8223850")	# 密码
# 延时2秒
# 点击按钮
driver.find_element("xpath", "//div[@class='btn']").click()
time.sleep(5)
'''
#driver.find_element("xpath", "//input[@type='text']").clear()
#driver.find_element("xpath", "//input[@type='text']").get_attribute()
#driver.find_element("xpath", "//input[@type='text']").send_keys("37.3 97.8")	# 账号
driver.find_element("xpath", "//input[@type='text']").click()
time.sleep(2)
driver.find_element("xpath", "//div[@class='sub-info']").click()
driver.find_element("xpath", "//div[@class='wapcf-btn wapcf-btn-ok']").click()
#driver.quit()
'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
