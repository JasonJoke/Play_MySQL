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
        xl =pd.ExcelFile(new_path)
        sheet_names = xl.sheet_names
        # print(sheet_names)
        if len(sheet_names) > 3:
            try:

                if sheet_names[-3]=='index':
                    continue
                else:
                    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                                           port=3306,database = 'chart_demo')
                    cursor = conn.cursor()

                    # # name = '09-02','09-03','09-04'
                    # for name in sheetname:
                    #     for j in range(-3,len(sheetname)):

                    data = pd.read_excel(new_path, sheet_name=sheet_names[-3])
                    # print(data)
                    for k in range(len(data['TIME'])):
                        timstr = '2020-' + str(sheet_names[-3]) + ' ' + str(data['TIME'][k])
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

                        sql = "insert into daily_data " \
                              "(package_name,dalvik,native,cpu,time) " \
                              "values('%s','%d','%d','%d','%s')" \
                              % (new_name, dalvik, native, cpu, create_time)
                        try:
                            # values = (dalvik_max,dalvik_min,dalvik_avg,native_max,native_min,native_avg,cpu_max,cpu_min,cpu_avg,crash)
                            cursor.execute(sql)
                            conn.commit()
                            print(sql)
                            print('....................')

                        except:
                            conn.rollback()
                            print('=====================')

                    cursor.close()
                    conn.close()
            except Exception:
                continue
