import requests
import json

#  爆米花搞笑视频
#  以下这种类型是抓包获得的，因为得到的地址全是一个json格式的文本，里面包含视频具体所在的地址等。
base_url='https://push-common.baomihua.com:8081/api/cds/getVideoPageList'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'  
}
# 发送请求
#  pagesize是一次请求多少份
#  pageindex应该可以实现翻页
post_form={
    'appKey': 'B2A9505CBF4D4E5091DF054C1F490980',
    'pageSize': '4',
    'pageIndex': '1',
    'channelId': '05e80f97-93bd-427f-9958-aebd13b30500',
    'ts': '1612350762',
    'rd': '45',
    'tk': '7468EE08C923AB6317F520FBAFFB56D8'
}
response = requests.post(base_url, data=post_form,headers=headers) # 这里没有用代理
data = response.text
# print(data)
# 数据转换 把json字符串转换为python可以交换的类型
import json
json_data = json.loads(data)

# print(json_data) 
# 数据解析  看你需要什么数据
# 一层层获得数据 网站json.cn可视化json
#  解析title，视频数据url类型（猜测）
# 这里data_list是一个数组
data_list = json_data['data']
# 遍历列表
for data_item in data_list:
    # print(data_item)
    #  视频文件名字 需要自己加尾缀
    video_title=data_item['Title']+'.mp4' 
    #  视频存在位置,这里还需要跳转
    video_Url = data_item['Link']
    video_Playid = data_item['PlayId']
    # print(video_title)
    print('解析link',video_title)
    second_url='https://push-common.baomihua.com:8081/api/play/getVideoDetailP'
    second_form={
        'playId':video_Playid,
        'cId': '1'
    }
    finall_data = requests.post(second_url,data=second_form,headers=headers).text
    # print('finall_data',finall_data)
    # 转换为可操作的python实体，然后后面解析json得到mp4地址
    json_finall_url = json.loads(finall_data)['data']['PlayUrl']
    print('正在下载',video_title)
    #  再次发送具体视频URL地址 得到的是二进制数据，需要后面加上一个content
    video_data = requests.get(json_finall_url,headers=headers).content
    # print(finall_data.text)
    #  再次发送具体视频URL地址 得到的是二进制数据，需要后面加上一个content
    #  保存在文件夹videos,wb方式写入，二进制方式
    #  因为vscode终端运行的原因，目前视频还是保存在python里面的
    with open('videos\\'+video_title,'wb') as f:
        f.write(video_data)
        print('下载完成...\n')

