import requests
import parsel
from lxml import etree
import time
# 导入CSV安装包
import csv
import random
headers={
    'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
base_url = 'https://www.kuaidaili.com/free/inha/{}/'




test_url = 'http://httpbin.org/get'
def send_request(url_data):
    reponse = requests.get(url_data,headers=headers)
    # print(reponse)
    #  以二进制的方式获得数据
    data = reponse.text
    return data
    # with open('块代理.html','wb') as f:
    #     f.write(data)
    



def parse_data(url_data):
    html =send_request(url_data)
    # 数据转换
    elemt = etree.HTML(html)
    
    ips_list = elemt.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[1]/text()')
    ports_list = elemt.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[2]/text()')
    Type_list = elemt.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr/td[4]/text()')
    # print(Type_list)
    # 该数组保存格式 {'HTTP': '110.243.13.94:9999'} 
    proxies_list = []
    for ip, port,http_type in zip(ips_list, ports_list,Type_list):
        proxies_dict = {}
        # 拼接ip与port
        proxy = ip.strip() + ":" + port.strip()
        
        proxies_dict[http_type]=proxy
        #  保存在数组中
        proxies_list.append(proxies_dict)
        # print(proxies_dict)
    return test_proxy(proxies_list)


    
#  上面得到的数据是否可用 一整页数据一起测试ip是否有效
def test_proxy(proxies_list):
    '''测试代理IP是否可用'''
    # 参数类型
    # proxies
    # proxies = {'协议': '协议://IP:端口号'}
    # timeout 超时设置 网页响应时间3秒 超过时间会抛出异常
    use_ip =[]
    for proies in proxies_list:
        try:
            resp = requests.get(url=test_url, proxies=proies, headers=headers)
            # 获取 状态码为200 
            # self.file.write(proxy)
            # self.file.flush()
            if resp.status_code == 200:
                print(proies, '\033[31m可用\033[0m')
                # 可以的IP 写入文本以便后续使用
                use_ip.append(proies)
              
            else:
                print(proies, '不可用')

        except Exception as e:
            print(proies, '：抛出错误的不可用')
    return use_ip

def crawl():
    '''执行函数'''
    # 快代理每页url 的区别
    # https://www.kuaidaili.com/free/inha/1/
    # https://www.kuaidaili.com/free/inha/2/
    # .......
    # 提供的免费ip太多
    # 这里只获取前100页提供的免费代理IP测试
    # https://www.kuaidaili.com/free/inha/1/
    # 下面是存入txt文件做法，测试有效
    
    # file=open('data.txt','w') 
    
    # for i in range(1, 2):
    #     print("======================正在获取第{}页可用的ip===========".format(i))
    #     # 拼接完整的url
    #     get_url=base_url.format(i)

    #     # 注意抓取控制频率
    #     time.sleep(random.randint(1, 4))
    #     #  该页有用的ip ，格式：{'HTTP': '58.22.177.69:9999'}
    #     use_ip = parse_data(get_url)
    #     file.write(str(use_ip)); 
    #     file.flush()
    # file.close() 
    # 下面是存入csv文件中
    for i in range(1, 10):
        print("======================正在获取第{}页可用的ip===========".format(i))
        # 拼接完整的url
        get_url=base_url.format(i)

        # 注意抓取控制频率
        time.sleep(random.randint(1, 4))
        #  该页有用的ip ，格式：{'HTTP': '58.22.177.69:9999'} use_ip是一个存对象的数组
        use_ip = parse_data(get_url)
        
        store_csv(use_ip)
        print("======================csv存储第{}页可用的ip成功===========".format(i))




#  数组，里面格式：{'HTTP': '58.22.177.69:9999'}
def store_csv(data):
    for item in data:
        for key,value in item.items():
            # 4. 写入csv文件内容
            csv_writer.writerow([key,value])
           


    
  

if __name__=='__main__':


    # 1. 创建文件对象
    csv_obj = open('ip_pool.csv','w',encoding='utf-8',newline='' "")
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(csv_obj)
    # 3. 构建列表头
    csv_writer.writerow(["type","IP"])


    crawl()

    # 5. 关闭文件
    csv_obj.close()
    

    


    