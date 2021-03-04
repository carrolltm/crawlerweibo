video_title =['1','2','3']
# 一次写入字符串
# with open('最后视频Url.html','w',encoding='utf-8') as f:
#     # if(len(video_title)!=0):
#     f.write(video_title)

# 分别写入
import os
f = open('最后视频Url.html','w',encoding='utf-8')
for item in video_title:
    f.write(item+"\n")
f.close()