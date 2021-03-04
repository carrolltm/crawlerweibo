import requests
import pandas as pd 
from fake_useragent import UserAgent
import json
import random
import time
import os
import re # 正则表达式模块
from urllib.parse import unquote  # Url解码模块
# 目标网站
url='https://www.weibo.com/?category=10011'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Cookie': 'SUB=_2AkMXRcC6f8NxqwJRmPAVym3haI5xyA3EieKhGTFhJRMxHRl-yT9jqlIftRB6PMXuVbUNvCj3bNrSTEheOHDC7H0XUmmS; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5-ssRgVEBU.1lrvZJBWo3W; SINAGLOBAL=7615478906614.841.1612271508793; _ga=GA1.2.841641562.1612407584; _gid=GA1.2.1251881638.1612407584; login_sid_t=cb224217a606160aff694fa08714261f; cross_origin_proto=SSL; _s_tentry=cn.bing.com; UOR=,,cn.bing.com; Apache=8003051486948.436.1612426028829; ULV=1612426028837:5:5:5:8003051486948.436.1612426028829:1612420903615' 
}
# 一:proxies 1.1版本
# 参数类型 proxies = {'协议': '协议://IP:端口号'}
# proxies = {
#             'HTTP': '12.243.13.94:9939'   
#         }
#  这里使用读取csv来获得ip，不用以下方式就注释掉，直接用上面的就可以
df = pd.read_csv("ip_pool.csv")
#  这里直接变成数组格式
# 一:proxies 1.2版本
df_list=df.values.tolist()
# proxies = {
#             # 暂时还是固定
#             df_list[0][0]: df_list[0][1]
#         }
# 一:proxies 1.3版本
# 我没有必要取随机数，如果这一个不行我直接取下一个
# 这个索引是从0开始
csv_ip_local = 0   # csv中用到第几个Ip了
proxies = {
        # type :ip   行列定位
        df_list[csv_ip_local][0]: df_list[csv_ip_local][1]
    }


def deal_proxes(csv_index):
    new_proxies = {
            # type :ip   行列定位
            df_list[csv_index][0]: df_list[csv_index][1]
        }
    return new_proxies

def test_proxy(proxy):
    # 测试ip是否可用
    test_url = 'http://httpbin.org/get'
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
    # 响应应该类似于没网这种吧，响应403好像也是响应
    except Exception as e:
        print(proxy, '抛出错误：不可用')


#  检测该IP是否有效 对http://httpbin.org/get 进行检测
if test_proxy(proxies):

    # 如果该ip地址被屏蔽，从csv文件中获得一个没有被微博屏蔽的IP
    html_data=requests.get(url=url,headers=headers,proxies=proxies)
    if(html_data.status_code!=200):
        proxies=deal_proxes(csv_ip_local+1)
        while(True):
            html_data=requests.get(url=url,headers=headers,proxies=proxies)
            if(html_data.status_code!=200):
                csv_ip_local=csv_ip_local+1
                proxies=deal_proxes(csv_ip_local)
                html_data=requests.get(url=url,headers=headers,proxies=proxies)
            else:
                break
    # 将获取到的Html网页源代码写到返回的html.html中
    # with代表着不使用该文件时就被自动关闭
    with open('返回的html.html','wb') as f:
        f.write(html_data.content)

    html_data =html_data.text

    # 正则表达式匹配
    # video_title= re.findall('<script charset="utf-8">FM.view\(([\d\D]*?)\)</script>',html_data)  # 返回得是一个列表
    # if(len(video_title)>=3):
    #     video_title = video_title[2]
    #     with open('第一次得到正则.html','w',encoding='utf-8') as f:
    #         # if(len(video_title)!=0):
    #         f.write(video_title)

    #     # 得到的是一个json格式的字符串
    #     json_scipt_data = json.loads(video_title)
    #     json_html_str= json_scipt_data['html']
    #     #  得到是html字符串
    #     # video\.weibocdn([\d\D]*?)unistore
    #     # https://f.video.weibocdn.com 参数  =unistore,video
    #     #  所以我们需要拼接一下然后转码，因为得到的字符串参数是没有编码的
    # else:
    #     print('没有匹配成功')


    # video\.weibocdn([\d\D]*?)unistore
    # https://f.video.weibocdn.com 参数  =unistore,video
    # 所以我们需要拼接一下然后转码，因为得到的字符串参数是没有编码的
    # 以下到'最后视频Url.html的输入之前都是获得视频最终地址并写入文件
    # ------------------------获得视频url地址
    Url_data=re.findall('video\.weibocdn([\d\D]*?)unistore',html_data)  # 这是一个列表: .com参数 unistore(结尾)
    final_url_data=[]
    print('最终解析到视频Url的个数',len(Url_data))
    index =1

    # -------------------------获得视频标题----------------
    # 去掉html标签性质的，得到的是汉字
    # list_title_s(.*?)的微博视频
    title_arr=[]
    title_data=re.findall('list_title_s(.*?)的微博视频',html_data)  # 这是一个列表: .com参数 unistore(结尾)
    for title_item in title_data:

        # 下面是对title数据进行格式处理，删掉一个没必要的文字
        pre = re.compile('>(.*?)<')
        origin_title= ''.join(pre.findall(title_item))
        # 删除这种格式的： 假如过年回家亲戚都说真话(左右两边带井号)
        # 可以不断去match，然后删除 
        # 匹配成功re.search方法返回一个匹配的对象，否则返回None。
        get_search=re.search('#(.*?)#', origin_title)
        while(True):
            if get_search==None:
                break
            origin_title=re.sub(get_search.group(), "",origin_title)
            get_search=re.search('#(.*?)#',origin_title)
        title_arr.append(origin_title)

    print('最终解析到视频标题的个数',len(title_arr))


    for url_item in Url_data:
        # 拼接字符串和编码
        # 是个完整的视频，但是好像少了点链接
        url_item = unquote(url_item, 'utf-8')
        url_item = 'https://f.video.weibocdn'+url_item+'unistore,video'
        final_url_data.append(url_item)  # 其实都可以不保存
        # 对上面的url数据进行获取和存储 
        # 发生异常: TypeError: a bytes-like object is required, not 'str'
        try:
            video_data = requests.get(url=url_item, proxies=proxies, headers=headers, timeout=3)
            
            # 查看状态码   
            if video_data.status_code == 200:
                print( '第{}个Url\033[31m可用\033[0m'.format(index))
                # 将获得到的视频存储到文件中
                with open('videos\\'+title_arr[index-1]+'.mp4','wb') as f:
                    f.write(video_data.content)
                    print('下载完成...\n')
            
            else:
                print('第{}个Url不可用'.format(index))
                
            index = index+1
        except Exception as e:
            print('第{}个Url不可用'.format(index))





    # 将解析到的视频Url保存起来
    f = open('最后视频Url.html','w',encoding='utf-8')
    for item in final_url_data:
        f.write(item+"\n")
    f.close()


        

    

