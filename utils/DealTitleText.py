
# from urllib.parse import unquote
# text='https%3A%2F%2Ff.video.weibocdn.com%2FQ9fBi7UMlx07K3B0OMWI010412013yjx0E010.mp4%3Flabel%3Dmp4_hd%26template%3D480x720.25.0%26trans_finger%3Dd8257cc71422c9ad30fe69ce9523c87b%26ori%3D0%26ps%3D1EO8O2oFB1ePdo%26Expires%3D1612438106%26ssig%3Ds8dF79pY%252FR%26KID%3Dunistore%2Cvideo'
# text = unquote(text, 'utf-8')
# 真正url

import re
 
html='\"><a target=\"_blank\" render=\"ext\" suda-uatrack=\"key=topic_click&value=click_topic\" class=\"a_topic\" extra-data=\"type=topic\" href=\"\/\/s.weibo.com\/weibo?q=%23%E5%81%87%E5%A6%82%E8%BF%87%E5%B9%B4%E5%9B%9E%E5%AE%B6%E4%BA%B2%E6%88%9A%E9%83%BD%E8%AF%B4%E7%9C%9F%E8%AF%9D%23&from=default\">#假如过年回家亲戚都说真话#<\/a>哈哈哈内容过于真实了<img class=\"W_img_face\" render=\"ext\" src=\"\/\/img.t.sinajs.cn\/t4\/appstyle\/expression\/ext\/normal\/a1\/2018new_doge02_org.png\" title=\"[doge]\" alt=    \"[doge]\" type=\"face\" \/><br><a target=\"_blank\" render=\"ext\" suda-uatrack=\"key=topic_click&value=click_topic\" class=\"a_topic\" extra-data=\"type=topic\" href=\"\/\/s.weibo.com\/weibo?q=%23%E7%89%9B%E5%B9%B4%E5%90%90%E6%A7%BD%E4%BA%89%E9%9C%B8%E8%B5%9B%23&from=default\">#牛年吐槽争霸赛#<\/a> <a target=\"_blank\" render=\"ext\" suda-uatrack=\"key=topic_click&value=click_topic\" class=\"a_topic\" extra-data=\"type=topic\" href=\"\/\/s.weibo.com\/weibo?q=%23%E6%98%A5%E6%99%9A%23&from=default\">#春晚#<\/a> <a  suda-uatrack=\"key=tblog_card&value=click_title:4600997076538978:1034-video:1034%3A4600986279280651::5931462026:4600997076538978:5931462026\" title=\"土味说'

 
# 去掉html标签性质的，得到的是汉字
pre = re.compile('>(.*?)<')
text= ''.join(pre.findall(html))
# 删除这种格式的： #假如过年回家亲戚都说真话#
# 可以不断去match，然后删除 
# 匹配成功re.search方法返回一个匹配的对象，否则返回None。

get_search=re.search('#(.*?)#', text)

while(True):
    if get_search==None:
        break
    text=re.sub(get_search.group(), "",text)
    get_search=re.search('#(.*?)#', text)
print(text)





