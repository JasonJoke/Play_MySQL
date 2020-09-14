import  pandas as pd
import pymysql
import datetime,time
import xlrd

#文件路径
file = './analysis_module/aasummary.xlsx'
#读取文件以及文件的所有sheetname
workbook = xlrd.open_workbook(file)
sheetname = workbook.sheet_names()

conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest', port=3306, database='chart_demo')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

def data(sheetname,tablename):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)
        sql = "insert into `%s` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (tablename,create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free, used_raw)
        # print(sql)
        try:
            # values = (dalvik_max,dalvik_min,dalvik_avg,native_max,native_min,native_avg,cpu_max,cpu_min,cpu_avg,crash)
            cursor.execute(sql)
            conn.commit()
            print(sql)
            print('....................')
        except:
            conn.rollback()
            print('=====================')


if __name__ == '__main__':
    dict = {}
    for i in range(len(sheetname) - 3):
        dict[sheetname[i]] = sheetname[i]
    print(dict)
    for key, value in dict.items():
        data(key,value)
    cursor.close()
    conn.close()












