import requests
import json
#  基于控制台获取输入-待翻译词语
content='欢迎'
# 设定待请求的Url
url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# 建立post的表单
post_form = { 
    'i': content,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16123517871849',
    'sign': 'a766e838d2bcdf8cf191dc08d02ec300',
    'lts': '1612351787184',
    'bv': 'e65e8e5642f3c2d719d32db0b5eff1f9',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}

#  提交post请求
reponse = requests.post(url,data=post_form)


# 接收响应结果，并解析提取
tran_dict=json.loads(reponse.text)
print(tran_dict)
# 打印响应结果
