import  pandas as pd
import json
import pymysql
import datetime,time
import os
import xlrd
path = './analysis_module/'
all_file = os.listdir(path)

for name in all_file:
    if name.startswith('com.') or name.startswith('surface') or name.startswith('system'):
        #找到符合条件的文件名
        new_name = os.path.splitext(name)[0]
        #文件路径
        new_path = path+new_name+'.xlsx'
        #打开相应的文件
        workbook = xlrd.open_workbook(new_path)
        #文件所包含的所有sheetname
        sheetname = workbook.sheet_names()
        #sheetname的个数
        num = workbook.nsheets
        name = '09-02','09-03','09-04'
        if len(sheetname) > 3:
            # 写入数据库
            conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest', port=3306,db='chart_demo')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            try:
                if sheetname[-3] in name:
                    for j in range(-3, 0):
                            data = pd.read_excel(new_path, sheet_name=sheetname[j])
                            for k in range(len(data['TIME'])):
                                timstr = '2020-' + str(sheetname[j]) + ' ' + str(data['TIME'][k])
                                try:
                                    time.strptime(timstr, "%Y-%m-%d %H:%M:%S")
                                    create_time = datetime.datetime.fromtimestamp(
                                        time.mktime(time.strptime(timstr, "%Y-%m-%d %H:%M:%S")))

                                except Exception:
                                    continue
                                print(create_time)
                                dalvik = data['DALVIK'][k]
                                print(dalvik)
                                native = data['NATIVE'][k]
                                print(native)
                                cpu = data['CPU'][k]
                                print(cpu)

                                sql = "insert into `daily_data` " \
                                      "(package_name,dalvik,native,cpu,time) " \
                                      "values('%s','%d','%d','%d','%s')" \
                                      % (new_name, dalvik, native, cpu, create_time)
                                try:
                                    # values = (dalvik_max,dalvik_min,dalvik_avg,native_max,native_min,native_avg,cpu_max,cpu_min,cpu_avg,crash)
                                    cursor.execute(sql)
                                    conn.commit()
                                    print('....................')
                                except:
                                    conn.rollback()
                                    print('=====================')
                    cursor.close()
                    conn.close()
                else:
                    continue
            except Exception:
                continue


    #
    #
    #
    #
