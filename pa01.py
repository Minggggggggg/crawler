#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:33:35 2017

@author: chenming
"""

# 1. 请求
import requests
r = requests.get('http://www.mafengwo.cn/poi/28961.html')
html=r.content

#view-source:http://www.mafengwo.cn/poi/28961.html
    
    
# 2. 解析
#首先还是导入package：
from bs4 import BeautifulSoup
#然后创建一个BeautifulSoup对象：
soup = BeautifulSoup(html,'html.parser')    #html.parser是解析器
#下面我们根据我们看到的网页提取。首先提取我复制的这部分的代码的第一行，先定位到这部分代码：
div_people_list = soup.find('li', attrs={'data-scroll': 'commentlist'})
#这里我们使用了BeautifulSoup对象的find方法。这个方法的意思是找到带有‘div’这个标签并且
#参数包含" class = 'people_list' "的HTML代码。如果有多个的话，find方法就取第一个。
#那么如果有多个呢？正好我们后面就遇到了，现在我们要取出所有的“a”标签里面的内容：
a_s = div_people_list.find_all('a', attrs={'title': '蜂蜂点评'})
#这里我们使用find_all方法取出所有标签为“a”并且参数包含“ target = ‘_blank‘ ”的代码，
#返回一个列表。“a”标签里面的“href”参数是我们需要的老师个人主页的信息，而标签里面的文字是
#老师的姓名。我们继续：
for a in a_s:
    url = a['href']
    name = a.get_text()
    
    
# 3. 储存
for a in a_s:
    url = a['href']
    name = a.get_text()
    print (name,url)
    
