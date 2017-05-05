#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:36:15 2017

@author: chenming
"""

### 第一页 第一条
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
dd[a+c:b-d]



######    第一页 
dd=str(d3)
c=19
d=4
i=1
k=0
a=0
b=0
data1=0
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
      
      
  
    
      
###   提取总的评论  ？？？ 草稿
import requests 
import json
import re    
for i in range(5):
    #import requests
    r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":1,"just_comment":1}')
    html_text=r.content
    #import json 
    htlm01=html_text[49:len(html_text)-3]
    #decoded = json.loads(htlm01)
    dd0=str(htlm01, encoding = "utf-8") 
    d3=json.loads(dd0) 
    dd=str(d3)
    # 第一条评论
    #import re
    pattern = '</?[p][^>]*>(.*?)<\/p>'
    re1=re.search(pattern,dd)
    a=re1.start()
    b=re1.end()
    c=19
    d=4
    ok=dd[a+c:b-d]
    print(ok)
#    
a1='ok'
a2='hg'
k=2
a3=a1+str(k)+a2
print(a3)
#   
b1='http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":'
b2=1
b3=',"just_comment":1} '
b4=b1+str(b2)+b3
print(b4)
#####
import requests
r=requests.get(b4)
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
##################### 草稿










############ 285页中每一页的第一条评论
import requests
import json 
import re
for i in range(1,285):
    # import requests
    #
    b1='http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":'
    b2=i
    b3=',"just_comment":1} '
    b4=b1+str(b2)+b3
    #print(b4)
    r=requests.get(b4)
    html_text=r.content
    # import json 
    htlm01=html_text[49:len(html_text)-3]
    dd0=str(htlm01, encoding = "utf-8") 
    d3=json.loads(dd0) 
    dd=str(d3)
    # import re
    pattern = '</?[p][^>]*>(.*?)<\/p>'
    re1=re.search(pattern,dd)
    a=re1.start()
    b=re1.end()
    c=19
    d=4
    jj=dd[a+c:b-d]
    print(jj)


############ 285页中的所有评论
import requests
import json 
import re
for i in range(1,4):
    # import requests
    # 文本连接
    b1='http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":'
    b2=i
    b3=',"just_comment":1} '
    b4=b1+str(b2)+b3
    #print(b4)
    r=requests.get(b4)
    html_text=r.content
    # import json 
    htlm01=html_text[49:len(html_text)-3]
    dd0=str(htlm01, encoding = "utf-8") 
    d3=json.loads(dd0) 
    ######    循环OK
    dd=str(d3)
    c=19
    d=4
    k=0
    a=0
    b=0
    data1=0
    #for k in 1:len(dd):
    while (k<len(dd)):    
      #import re
      pattern = '</?[p][^>]*>(.*?)<\/p>'
      gg=dd[k:len(dd)]
      data1=re.search(pattern,gg) 
      if (data1!= None):
        a=data1.start()
        b=data1.end()
        text0=gg[a+c:b-d]
        k=k+b
        print(text0)        
      else:
        k=2*len(dd)
        t1='\033[1;35m 第'
        t2=i
        t3='页的评论提取结束. \033[0m'
        t4=t1+str(t2)+t3
        print(t4)


        
        
        
 

       
#import codecs
f = open('/Users/chenming/Desktop/黄鹤楼.txt')
f.write(text0)

fh = open('/Users/chenming/Desktop/黄鹤楼.txt', 'w') 
fh.write(text0) 
fh.close()

	
def save(filename, contents): 
  fh = open(filename, 'w') 
  fh.write(contents) 
  fh.close() 
save('file.name', 'some stuff') 

save('/Users/chenming/Desktop/黄鹤楼.txt',text0)

with open("dodo.txt","w") as f:
        f.write("这是个测试！")
  
f = open('/Users/chenming/Desktop/黄鹤楼.txt', encoding='GB2312')
f.read()
filecontent = f.read()
print(filecontent)
'hello python!\nhello world!\n'
>>> f
<open file '/tmp/test.txt', mode 'r' at 0x7fb2255efc00>


import codecs
content = u'你好，脚本之家 jb51.net 在没有什么更开心的了。'
f = codecs.open('/Users/chenming/Desktop/dodo.txt','w','utf-8')
f.write(content)









