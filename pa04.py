#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:52:54 2017

@author: chenming
"""





### 第一页
import requests
r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":1,"just_comment":1}&_=1492393825950')
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
dd[a+c:b-d]

######    循环OK
dd=str(d3)
c=19
d=4
i=1
k=0
a=0
b=0
data1=0
#for k in 1:len(dd):
while (k<len(dd)):    
 import re
 pattern = '</?[p][^>]*>(.*?)<\/p>'
 gg=dd[k:len(dd)]
 data1=re.search(pattern,gg) 
 if (data1!= None):
      a=data1.start()
      b=data1.end()
      text0=gg[a+c:b-d]
      k=k+b
      print(text0)   
#print(text0)      
 else:
      k=2*len(dd)
      print('\033[1;35m 该页的提取已经结束。')



### 第二页
import requests
r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":2,"just_comment":1}&_=1492393825950')
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
dd[a+c:b-d]

######    循环OK
dd=str(d3)
c=19
d=4
i=1
k=0
a=0
b=0
data1=0
#for k in 1:len(dd):
while (k<len(dd)):    
 import re
 pattern = '</?[p][^>]*>(.*?)<\/p>'
 gg=dd[k:len(dd)]
 data1=re.search(pattern,gg) 
 if (data1!= None):
      a=data1.start()
      b=data1.end()
      text0=gg[a+c:b-d]
      k=k+b
      print(text0)   
#print(text0)      
 else:
      k=2*len(dd)
      print('\033[1;35m 该页的提取已经结束。')

