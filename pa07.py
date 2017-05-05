#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:20:57 2017

@author: chenming
"""

### 数据库建立
import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS Pachong")

# 使用预处理语句创建表
sql = """CREATE TABLE Pachong (
         DATA_NAME  VARCHAR(100) NOT NULL,
         DATA_DETAIL   VARCHAR(2180) )"""
cursor.execute(sql)

# 关闭数据库连接
db.close()






### 数据库插入操作
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO Pachong(DATA_NAME,DATA_DETAIL) VALUES ('dian nao1', 'wo de dian nao1')"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()




### 数据库插入操作   02 中文

import pymysql


# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler',charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
text1='ssssssss'
sql = """INSERT INTO Pachong(DATA_NAME,DATA_DETAIL) VALUES ('法国收到', 'text1')"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()




### 数据库插入操作   03 中文

import pymysql
# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler',charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
t1='湖北'
t2='我们的大学'
#sql = """INSERT INTO Pachong(DATA_NAME,DATA_DETAIL) VALUES ('法国收到', 'text1')"""
cursor.execute('INSERT INTO Pachong VALUES(%s,%s)',(t1,t2))
   # 提交到数据库执行
db.commit()


