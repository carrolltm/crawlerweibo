from selenium import webdriver
import time
chromeOptions = webdriver.ChromeOptions()
 
# 设置代理
chromeOptions.add_argument("--proxy-server=http://12.243.13.94:9939")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152



#  这是绝对路径
exe_local =r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'

dirver = webdriver.Chrome(executable_path=exe_local, chrome_options=chromeOptions)



# 查看本机ip，查看代理是否起作用
dirver.get("http://httpbin.org/ip")

print(dirver.page_source)
time.sleep(6)
# 最大化浏览器
""" dirver.maximize_window()
dirver.get('https://weibo.com/?category=10011')


dirver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/input[1]').send_keys('1234')

        

  


# 截屏
# dirver.save_screenshot('./baidu.png')
# 睡眠1秒钟
time.sleep(6)
# 退出
dirver.quit() """