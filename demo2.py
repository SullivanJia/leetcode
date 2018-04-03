from selenium import webdriver

driver=webdriver.Chrome()
#调用chrome浏览器
print("打开教务系统...")
driver.get('http://gsdb.bjtu.edu.cn/client/login/')
print("已打开...OK")
driver.maximize_window()
print("正在填入账号密码...")
driver.find_element_by_name('u').send_keys('17126164')
driver.find_element_by_name('p').send_keys('Jiaguanyi001')
print("已填写...OK")
driver.find_element_by_tag_name('button').click()
print("进入选课界面....OK")
driver.get('https://gsdb.bjtu.edu.cn/course_selection/select/')
# print(content)
# driver.quit()