# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: weekly.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 9月 14, 2020
# ---

import pandas as pd
import numpy as np
import pymysql

path = 'project_data.xlsx'


def problem_tracking():
    df = pd.ExcelFile(path)
    sheet_name = df.sheet_names
    # print(sheet_name)
    data = pd.read_excel(path, sheet_name='Sheet2')
    # print(data)
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                           port=3306, database='chart_demo')
    cursor = conn.cursor()
    for i in range(len(data['datetime'])):
        time = data['datetime'][i]
        # print(time)
        TS_expected = data['TS预计残留'][i]
        # print(TS_expected)
        TS_real = data['TS实际残留'][i]
        # print(TS_real)
        YF_expected = data['YF预计残留'][i]
        # print(YF_expected)
        YF_real = data['YF实际残留'][i]
        # print(YF_real)
        MX_expected = data['美行预计残留'][i]
        # print(MX_expected)
        MX_real = data['美行实际残留'][i]
        # print(MX_real)
        print(time, TS_expected, TS_real, YF_expected, YF_real, MX_expected, MX_real)
        sql = "insert into supplier_problem_tracking(time, TS_expected, TS_real, YF_expected, YF_real, MX_expected, MX_real) " \
              "values('%s',%d,%d,%d,%d,%d,%d)" % (
                  time, TS_expected, TS_real, YF_expected, YF_real, MX_expected, MX_real)
        try:
            cursor.execute(sql)
            conn.commit()
            print(sql)
            print('....................')

        except:
            conn.rollback()
            print('=====================')

    cursor.close()
    conn.close()


def Bug_trend():
    df = pd.ExcelFile(path)
    sheet_name = df.sheet_names
    # print(sheet_name)
    data = pd.read_excel(path, sheet_name='Sheet4')
    # print(data)
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                           port=3306, database='chart_demo')
    cursor = conn.cursor()
    print(len(data['每周解决']))
    for i in range(len(data['每周解决'])):
        time = data['datetime'][i]
        print(time)
        newly_add = int(data['每周新增'][i])
        print(newly_add)
        fix = int(data['每周解决'][i])
        print(fix)
        sql = "insert into Bug_trend (time, added, fix) values('%s',%d,%d)" % (time, newly_add, fix)
        try:
            cursor.execute(sql)
            conn.commit()
            print(sql)
            print('....................')

        except:
            conn.rollback()
            print('=====================')

    cursor.close()
    conn.close()


def team_issues():
    df = pd.ExcelFile(path)
    sheet_name = df.sheet_names
    # print(sheet_name)
    data = pd.read_excel(path, sheet_name='Sheet3')
    # print(data)
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                           port=3306, database='chart_demo')
    cursor = conn.cursor()
    print(len(data['本周解决']))
    for i in range(len(data['本周解决'])):
        teams = data['组名'][i]
        print(teams)
        issues = int(data['现存'][i])
        print(issues)
        fix = int(data['本周解决'][i])
        print(fix)
        time = data['日期'][i]
        print(time)
        sql = "insert into team_issues(team, issues, fix, time) values('%s', %d, %d,'%s')" % (teams, issues, fix, time)
        print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            print(sql)
            print('....................')

        except:
            conn.rollback()
            print('=====================')

    cursor.close()
    conn.close()


def work_of_tester_group():
    df = pd.ExcelFile(path)
    sheet_name = df.sheet_names
    # print(sheet_name)
    data = pd.read_excel(path, sheet_name='Sheet5')
    # print(data)
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                           port=3306, database='chart_demo')
    cursor = conn.cursor()
    print(len(data['IOV测试提交bug']))
    for i in range(len(data['IOV测试提交bug'])):
        time = data['datetime'][i]
        IOV = int(data['IOV测试提交bug'][i])
        EE = int(data['EE提交bug'][i])
        DRE = int(data['DRE提交bug'][i])
        DEV = int(data['开发提交bug'][i])
        sql = "insert into work_of_tester_group(time, IOV, EE, DRE, DEV) values('%s', %d, %d, %d, %d)" % (time, IOV, EE, DRE, DEV)
        print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            print('....................')

        except:
            conn.rollback()
            print('=====================')

    cursor.close()
    conn.close()

def Bug_total_trend():
    df = pd.ExcelFile(path)
    sheet_name = df.sheet_names
    # print(sheet_name)
    data = pd.read_excel(path, sheet_name='Sheet6')
    # print(data)
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                           port=3306, database='chart_demo')
    cursor = conn.cursor()
    for i in range(len(data['datetime'])):
        time = data['datetime'][i]
        real = int(data['实际Bug数'][i])
        expected = int(data['预测Bug数'][i])
        sql = "insert into Bug_total_trend(time, real_bug, expected) values('%s', %d, %d)" % (time, real, expected)
        print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            print('....................')

        except:
            conn.rollback()
            print('=====================')

    cursor.close()
    conn.close()

def ABbug_trend():
    df = pd.ExcelFile(path)
    sheet_name = df.sheet_names
    # print(sheet_name)
    data = pd.read_excel(path, sheet_name='Sheet7')
    # print(data)
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                           port=3306, database='chart_demo')
    cursor = conn.cursor()
    for i in range(len(data['datetime'])):
        time = data['datetime'][i]
        expected = int(data['AB预测量'][i])
        real = int(data['AB实际量'][i])
        sql = "insert into ABbug_trend(time, ABexpected, ABreal) values('%s', %d, %d)" % (time, expected, real)
        print(sql)
        try:
            cursor.execute(sql)
            conn.commit()
            print('....................')

        except:
            conn.rollback()
            print('=====================')

    cursor.close()
    conn.close()

if __name__ == '__main__':
    # problem_tracking()
    # Bug_trend()
    # team_issues()
    # work_of_tester_group()
    # Bug_total_trend()
    ABbug_trend()