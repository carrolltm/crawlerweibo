import requests
import json
import re # 正则表达式模块
#  以下这种类型是抓包获得的，因为得到的地址全是一个json格式的文本，里面包含视频具体所在的地址等。
base_url='https://www.bilibili.com/video/BV1Fy4y1D7XS'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Cookie': "_uuid=5C8F462B-3F4E-C920-277E-2FF177073E6254582infoc; buvid3=57F8C6BF-B5A2-4F4D-A4C8-5474A4C4A84C95148infoc; sid=i45jzhbw; fingerprint=1893afc5f2cddacf1fa503891f3d2791; buivd_fp=57F8C6BF-B5A2-4F4D-A4C8-5474A4C4A84C95148infoc; buvid_fp_plain=089ED9E1-8943-40BE-BFF5-9A125F50DAED143107infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(mmRl~uk~u0J'uY|mkklRmJ; DedeUserID=317960038; DedeUserID__ckMd5=ddd1f2879d91a5c2; SESSDATA=804764f5%2C1624777951%2C6b2ed*c1; bili_jct=79593185def13840b5901ac5752825a5; LIVE_BUVID=AUTO2116097752837956; CURRENT_QUALITY=32; bsource=search_bing; _dfcaptcha=20d4079e24680e5e354e56a870247b25; PVID=4; bp_video_offset_317960038=487391763477278606; bp_t_offset_317960038=487392167197915090"
}
# 发送请求
response = requests.get(base_url, headers=headers)
data = response.text
# print(data)

# 正则表达式匹配
video_title=re.findall('<span class="tit">(.*?)</span>',data)[0]  # 返回得是一个列表
# print(video_title)

# 获得json数据
json_data=re.findall('<script>window\.__playinfo__=(.*?)</script>',data)[0]
# print(json_data)
import pprint
# pprint.pprint(json_data)

json_data=json.loads(json_data)
pprint.pprint(json_data)