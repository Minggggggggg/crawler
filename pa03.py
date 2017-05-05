#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 08:43:50 2017

@author: chenming
"""

# 1
import requests
r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery181047574512867892516_1492394283228&params={"poi_id":"5426285"}&_=1492394283454')
html_text=r.content



# 2
from bs4 import BeautifulSoup
bs=BeautifulSoup(html_text,'html.parser')
body=bs.body
#data=body.find('div', {'class': 'user'})
#p_data=data.find_all('p',{'class': 'rev-txt'})

#p_s=div_list.find_all('p', {'class': 'rev-txt'})
#p_s=div_list.find_all('p',attrs={'class','rev-txt'})
#import json
 
data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
#json_str = json.dumps(data)



#text= json.read(html_text)

#data_string = json.dumps(html_text)
#decoded = json.loads(html_text)

import json 
# Converting Python to JSON 
#  d1 = json.dumps(dd)
# Converting JSON to Python 
#  d2 = json.loads(d1) 



#import re
#data=str(html_text)

#pattern= "p class=\'rev-txt' (.*?) u3002<\/p>"
#res=re.search(pattern,data)
#print(res)





htlm01=html_text[50:89459]
#decoded = json.loads(htlm01)
dd=str(htlm01, encoding = "utf-8") 
d3=json.loads(dd) 


############

htlm02=html_text[42:89460]
dd=str(htlm02, encoding = "utf-8") 
import json 
d4=json.loads(dd) 


############
import re
#pattern= "<p class=\'rev-txt'>   <(\S*?)[^>]*>.*?</\1>|<.*? />   <\/p>"

htlm02=str(htlm01)

#p=re.compile(r'\w+')
#m= p.search("rev-txt")
re.search(r'\d+',htlm02)


pattern=re.compile(htlm02)
q="<p class=\'rev-txt'>"
m=pattern.search(q)

#i=[]
#for i in re.findall(r"<p class=\'rev-txt'> .+>(.*?) <\/p>",htlm02):
#    print (i)

t= re.findall('rev-txt',htlm02)
 
re.search("rev-txt",htlm02)

#p2 = re.compile(ur'[^\u4e00-\u9fa5]',htlm02)  

                  #中文的编码范围是：\u4e00到\u9fa5  
for i in re.findall('\<p * .+>(.+)  * \<\/p>', htlm02):
    print (i)


re.search("</p>",htlm02)

p=re.compile(r"</+p+>")
re.search(p,htlm02)


re.search('^<p class=\"rev-txt">  $',htlm02)

#!/usr/bin/env python
r1 = re.compile('([.*])')
print (re.findall(r1, "hello[hi]heldfsdsf[iwonder]lo"))
r1 = re.compile('([.*?])')
print (re.findall(r1, "hello[hi]heldfsdsf[iwonder]lo"))
print (re.findall('[0-9]{2}',"fdskfj1323jfkdj"))
print (re.findall('([0-9][a-z])',"fdskfj1323jfkdj"))
print (re.findall('(?=www)',"afdsfwwwfkdjfsdfsdwww"))
print (re.findall('(?<=www)',"afdsfwwwfkdjfsdfsdwww"))
#
if re.search(r'abc','helloaaabcdworldn'):
    print ('search succeeds')
else:
    print ('search fails' )
    
#!/usr/bin/env python
p = re.compile('(one|two|three)')
print (p.sub('num', 'one word two words three words apple', 2) )


re.findall(r'<p .+>(.+) </p>', htlm02)

re.search("<\(/p+)>",htlm02)
p3= '\b(</p>)'
re.search(p3,htlm02)


re.search('<p[^>]+>',htlm02)
htlm02[5358:5390]


#</?[p|P][^>]*> 
re.search('</?[p][^>]*>',htlm02)
htlm02[5358:5381]
tt=re.search('</?[p][^>]*>',htlm02)
d4[5358:5381]
dd=str(d3)
##### 1
ff=re.search('</?[p][^>]*>',dd)
# <_sre.SRE_Match object; span=(4200, 4219), match='<p class="rev-txt">'>
dd[4219:4255]
dd[4200:4219]
##### 2
p4='</?[p][^>]*>'
re.search(p4,dd)
##### 3
p5='</?[p][^>]>'
re.search(p5,dd)
# pattern = '/<p>[\s]*#{3}([\s\S]*?)#{3}[\s]*<\/p>/';
#'/<p>(.*?)<\/p>/'







######                          ######
######                          ######
######                          ######
######                          ######
import requests
r=requests.get('http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery181047574512867892516_1492394283228&params={"poi_id":"5426285"}&_=1492394283454')
html_text=r.content

import json 
htlm01=html_text[50:89460]
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


# 第二条评论
dd1=dd[4589:65594]
re.search(pattern,dd1)
dd1[3651+c: 4235-d]
#



######    循环
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
 a=data1.start()
 b=data1.end()
 text0=gg[a+c:b-d]
 print(text0)
 k=k+b
print('fin')
 





#print('This is a \033[1;35m test \033[0m!')
#print('This is a \033[1;32;43m test \033[0m!')
#print('\033[1;33;44mThis is a test !\033[0m')
 

######  单个
import re
pattern = '</?[p][^>]*>(.*?)<\/p>'
data=re.search(pattern,dd[0:len(dd)])
a=data.start()
b=data.end()
c=19
d=4
dd[a+c:b-d]
#
import re
pattern = '</?[p][^>]*>(.*?)<\/p>'
data=re.search(pattern,dd[61169:len(dd)])
a=data.start()
b=data.end()
c=19
d=4
dd[61169+a+c:61169+b-d]





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






