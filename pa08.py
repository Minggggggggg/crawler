#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:49:25 2017

@author: chenming
"""

############ 提取时间
import requests
r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":1,"just_comment":1}')
html_text=r.content
import json 
htlm01=html_text[49:len(html_text)-3]
#decoded = json.loads(htlm01)
dd0=str(htlm01, encoding = "utf-8") 
d3=json.loads(dd0) 
dd=str(d3)
# 第一条评论 时间
import re
pattern02 = '<span class="time">(.*?)<\/span>'
re1=re.search(pattern02,dd)
a=re1.start()
b=re1.end()
c=19
d=7
ww=dd[a+c:b-d]
print(ww)
#/<span oncopy="setClipBoardData\(\)">(［\s\S]*?)<\/span>/
#<span[^>]*>([\s\S]*?)</span
#/<span class="green">([^<]+)<\/span>/



############ 提取姓名
import requests
r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":1,"just_comment":1}')
html_text=r.content
import json 
htlm01=html_text[49:len(html_text)-3]
#decoded = json.loads(htlm01)
dd0=str(htlm01, encoding = "utf-8") 
d3=json.loads(dd0) 
dd=str(d3)
# 第一条评论 姓名
import re
#pattern02 = '<textarea class="comment_reply"[^>]*>(.*?)<\/textarea>'
pattern02 = '<textarea class="comment_reply"[^>](.*?)<\/textarea>'
re1=re.search(pattern02,dd)
a=re1.start()
b=re1.end()
c=0
d=0
cc=dd[a+c:b-d]
pattern03='data-comment_username="(.*?)\"'
re2=re.search(pattern03,cc)
a2=re2.start()
b2=re2.end()
ee=cc[a2+23:b2-1]
print(ee)



### 提取评论
import requests
r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":1,"just_comment":1}')
html_text=r.content
import json 
htlm01=html_text[49:len(html_text)-3]
#decoded = json.loads(htlm01)
dd0=str(htlm01, encoding = "utf-8") 
d3=json.loads(dd0) 
dd=str(d3)
# 第一条评论
import re
pattern = '</?[p][^>]*>(.*?)<\/p>'
re1=re.search(pattern,dd)
a=re1.start()
b=re1.end()
c=19
d=4
ss=dd[a+c:b-d]
print(ss)


import re
pattern = '<\?\\/[p][^>]*>(.*?)<\?\\/p>'
htlm001=html_text[49:len(html_text)-3]
#decoded = json.loads(htlm01)
dd00=str(htlm001, encoding = "utf-8") 
re001=re.search(pattern,dd00)
print(re001)

'<span class="time">(.*?)<\*\/span>'

