# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: insert_single_data.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 8月 27, 2020
# ---

import pymysql


def insert_single():
    # 建立数据库连接
    conn = pymysql.connect(host="10.16.31.77",
                           user="root",
                           password="AutoTest",
                           port=3306,  # 端口
                           database="chart_demo",
                           charset='utf8')

    # 获取游标
    cursor = conn.cursor()

    # 执行sql语句
    sql = 'insert into package(package_name) values(%s)'
    try:
        rows = cursor.execute(sql, ('qzcsbj4'))
        conn.commit()
    except:
        conn.rollback()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()


if __name__ == '__main__':
    insert_single()
