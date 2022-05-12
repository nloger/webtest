# webtest
auto test

## 开发环境说明
windows平台
Python 3.10.4
Chrome	101.0.4951.54
chromedriver.exe需放在webtest目录下

## 运行说明
cmd命令行进入webtest目录，执行python report.py, 运行结束后，生成report.html


## 结果说明
report1.html 单独测试步骤1生成的表结果
report.html 步骤1，2，3，4，5连起来测试结果

## report.py代码说明
test_get_url的get_limit参数，可根据in_url页面对应的items数量修改， 比如get_limit = 2000
