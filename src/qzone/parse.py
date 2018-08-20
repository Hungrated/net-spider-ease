import os
import codecs
import xlwt
from .account import USER_NAME
from .encrypt import *

"""

读取说说信息列表到文件

"""


def read_moment_info():
    csv_dir = os.path.join(os.getcwd(), 'out', 'moments_info.csv')
    info_lines = []
    try:
        file = codecs.open(csv_dir, 'r', 'utf-8')
        info_lines = file.readlines()
    finally:
        print('\n*** all info are read. ***')
        return info_lines


def export_to_excel():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(decrypt_str(USER_NAME), cell_overwrite_ok=True)
    info_lines = read_moment_info()
    for i in range(len(info_lines)):
        line = info_lines[i].split(',')
        for j in range(len(line)):
            sheet.write(i, j, line[j])
    xls_dir = os.path.join(os.getcwd(), 'out', 'moments_info.xls')
    book.save(xls_dir)
    print('\n*** all info written in moments_info.xls. ***')
