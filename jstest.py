from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com")
time.sleep(3)
#通过执行js，获取当前窗口的url，并打印
print(driver.execute_script("return location.href"))
#通过执行js，获取url域名，并打印
print(driver.execute_script("return location.hostname"))
#通过执行js，获取当前页面路径，并打印
print(driver.execute_script("return location.pathname"))
#通过执行js，获取协议，并打印
print(driver.execute_script("return location.protocol"))
driver.quit()
