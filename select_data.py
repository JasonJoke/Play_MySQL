# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: select_data.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 8月 27, 2020
# ---

import pymysql


def select_data():
    # 建立数据库连接
    conn = pymysql.connect(host="10.16.31.77",
                           user="root",
                           password="AutoTest",
                           port=3306,  # 端口
                           database="chart_demo",
                           charset='utf8')

    # 获取游标
    cursor = conn.cursor()

    # SQL 查询语句
    # fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    # fetchone(): 该收全部的返回结果行.
    # rowcount: 这是方法获取下一个查询结果集。结果集是一个对象
    # fetchall():接一个只读属性，并返回执行execute()方法后影响的行数
    # sql = "SELECT * FROM package ".format(1000)
    sql = "SELECT * FROM package WHERE package_name = 'zzz'".format(1000)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            packagename = row[1]
            # 打印结果
            print("id={},packagename={}".format(id, packagename))

    except:
        print("Error: unable to fecth data")

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()


if __name__ == '__main__':
    select_data()
