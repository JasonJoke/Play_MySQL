# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: test.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 8月 28, 2020
# ---
import os

path = './analysis_module/'
all_file = os.listdir(path)
for name in all_file:
    if name.startswith('com.') or name.startswith('surface') or name.startswith('system'):
        # 找到符合条件的文件名
        new_name = os.path.splitext(name)[0]

        print(type(new_name))
        print(new_name)