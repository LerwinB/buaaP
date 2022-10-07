# buaaP
一、配置环境
1. 操作系统：win
2. 浏览器：Chrome
3. 插件：chrome-driver
	下载地址：https://chromedriver.storage.googleapis.com/index.html
	安装教程：https://blog.csdn.net/xwj2633673783/article/details/119932573
二、配置参数
info文件
	第1行：学号，第2行：密码
	第3行：是否在校（0默认是）
	第4、5行：纬度经度（沙河：40.153176，116.27064 学院路：39.981389，116.34811）
确保info.txt 与buaaP.exe处于同一文件夹下运行buaaP.exe即可实现打卡功能。
三、设置win定时任务
定时任务需将info文件打包在exe内才可运行。
pyi-makespec -F test.py
pyinstaller test.spec
可利用源码buaaP.py文件实现。参考教程：http://t.csdn.cn/lztK5
也可直接修改源码中用户信息从而弃用info文件。

http://www.lerwin.site/archives/2022/32/
# 作者：lerwin blacklerwin@gmail.com
