import requests
import pandas as pd 
from fake_useragent import UserAgent
import json
import random
import time  
import os
import random
import re # 正则表达式模块
from urllib.parse import unquote  # Url解码模块
from fake_useragent import UserAgent  #UserAgent 是随机产生 ‘User-Agent’
df = pd.read_csv("ip_pool.csv")
#  这里直接变成数组格式
# 一:proxies 1.2版本
df_list=df.values.tolist()

# 这个索引是从0开始
# 我们从列表长度中获取随机IP
list_ip_len = len(df_list)
if(list_ip_len):
    csv_ip_local = random.randint(0,list_ip_len-1) # csv中用到第几个Ip了
else:
    csv_ip_local = 0      # 如果ip数目没有的话，其实这个判断没有用，只是方便后面功能留的坑
proxies = {
        # type :ip   行列定位
        df_list[csv_ip_local][0]: df_list[csv_ip_local][1]
    }
# 重新获得随机IP    
def get_randon_ip():
    print(list_ip_len)
    if(list_ip_len):
        csv_ip_local = random.randint(0,list_ip_len-1) # csv中用到第几个Ip了
    else:
        print('已经没有可用的IP地址了')  # 后面可以在这里选择是否重新爬取IP形成代理池

    proxies = {
        # type :ip   行列定位
        df_list[csv_ip_local][0]: df_list[csv_ip_local][1]
    }
    return proxies
print(proxies)
proxies=get_randon_ip()
print(proxies)
