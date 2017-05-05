#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:52:50 2017

@author: chenming
"""





### 数据库连接
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()




### 创建数据库表
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

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
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
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





### 数据库查询操作
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \WHERE INCOME > '%d'" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" %\
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()




### 数据库更新操作
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()



### 删除操作
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()



### 查看数据库 2
import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.0.115',port=3306,user='root', passwd='oseasy@0333', db='crawler')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用预处理语句创建表
sql = """SELECT * FROM EMPLOYEE0"""
cursor.execute(sql)
results = cursor.fetchall()
# 打印结果
for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
# 关闭数据库连接
db.close()
