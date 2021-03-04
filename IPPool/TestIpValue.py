import requests
import pandas as pd 
from fake_useragent import UserAgent
# 目标网站
url='https://www.baidu.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'  
}
# 参数类型
# proxies
# proxies = {'协议': '协议://IP:端口号'}
proxies = {
            'HTTP': '12.243.13.94:9939'   
        }
#  这里使用读取csv来获得ip，不用以下方式就注释掉，直接用上面的就可以
# df = pd.read_csv("ip_pool.csv")
# #  这里直接变成数组格式
# df_list=df.values.tolist()
# proxies = {
#             df_list[1][0]: df_list[1][1]
#         }

# 测试ip是否可用
test_url = 'http://httpbin.org/get'

def test_proxy(proxy):
    '''测试代理IP是否可用'''
    # 参数类型
    # proxies
    # proxies = {'协议': '协议://IP:端口号'}
    # timeout 超时设置 网页响应时间3秒 超过时间会抛出异常
    try:
        resp = requests.get(url=test_url, proxies=proxy, headers=headers, timeout=3)
        
        # 查看状态码   
        if resp.status_code == 200:
            print(proxy, '\033[31m可用\033[0m')
            return True
            
        else:
            print(proxy, '不可用')
            return False


    except Exception as e:
        print(proxy, '抛出错误：不可用')

if test_proxy(proxies):

    # html=requests.get(url=url,headers=headers,proxies=proxies,verify=False)
    html=requests.get(url=url,headers=headers,proxies=proxies)
    print(html.text)