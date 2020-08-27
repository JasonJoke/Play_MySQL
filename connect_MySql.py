# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: connect_MySql.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 8月 27, 2020
# ---
import pymysql

db = pymysql.connect(host="10.16.31.77",
                     user="root",
                     password="AutoTest",
                     port=3306,  # 端口
                     database="chart_demo",
                     charset='utf8')
# 创建游标
cursor = db.cursor()

# 关闭游标
cursor.close()

# 关闭数据库连接
db.close()
