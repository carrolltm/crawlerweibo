import requests
import json

#  以下这种类型是抓包获得的，因为得到的地址全是一个json格式的文本，里面包含视频具体所在的地址等。
base_url='https://haokan.baidu.com/videoui/api/videorec?tab=gaoxiao&act=pcFeed&pd=pc&num=20&shuaxin_id=1612276740204'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Cookie': 'BIDUPSID=8303CDB62079598D55280B09241EC6A5; PSTM=1609205633; BAIDUID=8303CDB62079598D785D47E1C310AF5F:FG=1; ab_jid=e8f37dcb0d84ebde578eaeb4c81de8c0ef8e; ab_jid_BFESS=e8f37dcb0d84ebde578eaeb4c81de8c0ef8e; BAIDUID_BFESS=8303CDB62079598D785D47E1C310AF5F:FG=1; BDUSS=VkM29seVBtNW9BY35hdk80YzV4MXIyaS1UOWJPMnFnU2lmZ0tjak05TlZreDVnRVFBQUFBJCQAAAAAAAAAAAEAAADGgNJFysXLrsH3xOqy0NK5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFUG919VBvdfTE; BDUSS_BFESS=VkM29seVBtNW9BY35hdk80YzV4MXIyaS1UOWJPMnFnU2lmZ0tjak05TlZreDVnRVFBQUFBJCQAAAAAAAAAAAEAAADGgNJFysXLrsH3xOqy0NK5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFUG919VBvdfTE; H_PS_PSSID=33425_33581_33257_33273_31660_33594_33339_26350_33264; BA_HECTOR=85010120a4058h81331g1ilep0r; __yjs_duid=1_f17eb43300edc3f1cb0b26e84be486ad1612274351261; ab_sr=1.0.0_M2NkNDA5MTRmZWM0MDlmMzczMmQ2MmNiM2QxZGE2ZDcwYWE1MWE5MmM5YmY1YTc5YTFmYWMxYjdlNzNiM2MzYmRhYjg4M2MzMjM4ZTc1YjQ0NGFmYjliMjk4ZDU0YWM4'
}
# 发送请求
response = requests.get(base_url, headers=headers)
data = response.text
# print(data)
# 数据转换 把json字符串转换为python可以交换的类型
import json
json_data = json.loads(data)

# 数据解析  看你需要什么数据
# 一层层获得数据 网站json.cn可视化json
#  解析title，视频数据url类型（猜测）
data_list = json_data['data']['response']['videos']
# 遍历列表
for data_item in data_list:
    # print(data_item)
    #  视频文件名字 需要自己加尾缀
    video_title=data_item['title']+'.mp4' 
    #  视频存在位置
    video_Url = data_item['play_url']
    # print(video_title)
    print('正在下载',video_title)
    #  再次发送具体视频URL地址 得到的是二进制数据，需要后面加上一个content
    video_data = requests.get(video_Url,headers=headers).content

    #  保存在文件夹videos,wb方式写入，二进制方式
    #  这边可以
    with open('videos\\'+video_title+'***'+base_url,'wb') as f:
        f.write(video_data)
        print('下载完成...\n')

