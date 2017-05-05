#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:25:45 2017

@author: chenming
"""

### 数据库建立
import pymysql
# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler', charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS Table04")
# 使用预处理语句创建表
sql = """CREATE TABLE Table04 (
         Title  VARCHAR(200) NOT NULL,
         Number   VARCHAR(200),
         Name   VARCHAR(500),
         Time   VARCHAR(200),
         Comment   VARCHAR(5000) )"""
cursor.execute(sql)
# 关闭数据库连接
db.close()






# 提取3个包
import requests
import json 
import re
j=0
title='黄鹤楼'
print(title)
# 循环
for i in range(1,4):
    # import requests
    # 文本连接
    b1='http://www.mafengwo.cn/poi/__pagelet__/pagelet/poiCommentListApi?callback=jQuery18108239282450208787_1492390399529&params={"poi_id":"5426285","page":'
    b2=i
    b3=',"just_comment":1} '
    htlm=b1+str(b2)+b3
    # print(b4)
    r=requests.get(htlm)
    html_text=r.content
    # import json 
    htlm_text_new=html_text[49:len(html_text)-3]
    htlm_text_new_str=str(htlm_text_new, encoding = "utf-8") 
    htlm_text_new_json=json.loads(htlm_text_new_str) #type(htlm_text_new_json)=dict
    # 转化字符（dict到str）
    dd=str(htlm_text_new_json) #type(dd)=str
    k=0
    data=0
    data01=0
    data02=0
    data03=0 
# 条件 while
    while (k<len(dd)):    
      #import re
      pattern01 = '</?[p][^>]*>(.*?)<\/p>'
      pattern02 = '<span class="time">(.*?)<\/span>'
      pattern03 = '<textarea class="comment_reply"[^>](.*?)<\/textarea>'
      data=dd[k:len(dd)]
      data01=re.search(pattern01,data) 
      data02=re.search(pattern02,data)
      data03=re.search(pattern03,data)
      # 条件 if
      if (data01!= None):
        # 评论
        a01=data01.start()
        b01=data01.end()
        c01=19
        d01=4
        comment=data[a01+c01:b01-d01]      
        print(comment) 
        # 第几条评论
        j=j+1  
        number=j
        print(j) 
        # 时间      
        a02=data02.start()
        b02=data02.end()
        c02=19
        d02=7
        time=data[a02+c02:b02-d02]
        print(time)
        # 姓名       
        a03=data03.start()
        b03=data03.end()
        c03=0
        d03=0
        cc=data[a03+c03:b03-d03]
        pattern04='data-comment_username="(.*?)\"' 
        data04=re.search(pattern04,cc)
        a04=data04.start()
        b04=data04.end()
        c04=23
        d04=1
        name1=cc[a04+c04:b04-d04]
        name=json.dumps(name1)
        name=name.replace('"','')  ### 去掉 “
        print(name)
        k=k+b03
        # 打开数据库连接
        db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler', charset='utf8')
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()
        # MYSQL 插入语句并执行
        try:
            cursor.execute('INSERT INTO Table04 VALUES(%s,%s,%s,%s,%s)',(title,number,name,time,comment))
        # 提交到数据库执行
            db.commit()
        except:      
            # 发生错误时回滚
            db.rollback() 
        db.close()        
      else:
        # 第几页
        k=2*len(dd)
        t1='\033[1;35m 第'
        t2=i
        t3='页结束. \033[0m'
        page=t1+str(t2)+t3
        j=j 
        print(page)
        

allaa=cursor.fetchall()

cursor.fetchall()
name.
name.find()

db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler', charset='utf8')
        # 使用cursor()方法获取操作游标 
cursor = db.cursor()
cursor.execute('INSERT INTO Table01 VALUES(%s,%s,%s,%s,%s)',(title,number,name,time,comment))
allfet=cursor.fetchall()
name.fetchall()