#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pip install openpyxl
import openpyxl
from VAR.VAR import *

# 读取excel内容，实现文件驱动自动化执行
def read_excel():
    excel = openpyxl.load_workbook(EXCEL_PATH)
    # excel = openpyxl.load_workbook('../data/api_cases_V4.xlsx')
    sheet = excel['Sheet1']
    # 创建装载Excel数据的变量
    tulpe_list = []
    # 逐行循环读取Excel数据
    for value in sheet.values:
        # 判断当前行的第一列的值，是否是数字编号
        if type(value[0]) is int:
            # 将元祖装进List
            tulpe_list.append(value)
    return tulpe_list

if __name__ == '__main__':
    print(read_excel())