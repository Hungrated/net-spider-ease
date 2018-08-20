import os
import codecs
import xlwt
import csv
import re
import time
from itertools import islice
from .account import USER_NAME
from .encrypt import *

"""

二维数组去重

"""


def dereplicate(arr_2d):
    arr_1d = []
    arr_dereplicated = []
    for item in islice(arr_2d, 1, None):
        arr_1d.append(str(item))
    arr_1d = list(set(arr_1d))
    arr_1d.sort()
    for item in arr_1d:
        arr_dereplicated.append(eval(item))
    return arr_dereplicated


"""

解析发布时间

"""


def parse_pub_time(pub_time_str):
    digit_arr_raw = re.findall('[0-9]+', pub_time_str)
    digit_arr = [1980, 1, 1, 0, 0, 0, 0, 0, 0]
    for i in range(len(digit_arr_raw)):
        digit_arr[i] = int(digit_arr_raw[i])
    time_obj = time.struct_time(tuple(digit_arr))

    timestamp = int(time.mktime(time_obj))
    date_str = time.strftime('%Y-%m-%d', time_obj)
    time_str = time.strftime('%H:%M', time_obj)

    return timestamp, date_str, time_str


"""

再加工说说信息

"""


def rebuild_moment_info(info_lines):
    parsed_info_arr = [
        ['moment_id', 'date', 'time', 'like_cnt', 'content_o', 'is_original', 'content_f', 'has_img', 'img_list']]
    for info in info_lines:
        pub_time_str = info[0]
        timestamp, date_str, time_str = parse_pub_time(pub_time_str)
        like_cnt = int(info[1])
        content_o = info[2]
        content_f = info[3]
        is_original = content_f == ''
        img_list_str = info[4]
        has_img = img_list_str != '[]'
        parsed_info_arr.append(
            [timestamp, date_str, time_str, like_cnt, content_o, is_original, content_f, has_img, img_list_str])
    return parsed_info_arr


"""

读取说说信息列表到文件

"""


def read_moment_info():
    csv_dir = os.path.join(os.getcwd(), 'out', 'moments_info.csv')
    info_arr = []
    info_lines = csv.reader(codecs.open(csv_dir, 'r', 'utf-8'))
    info_lines_dereplicated = dereplicate(list(info_lines))
    info_arr = rebuild_moment_info(info_lines_dereplicated)
    print('\n*** all info are read. ***')
    return info_arr


"""

将加工后的说说信息保存到excel文件

"""


def export_to_excel():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(decrypt_str(USER_NAME), cell_overwrite_ok=True)
    info_arr = read_moment_info()
    info_cnt = len(info_arr)
    print('total count: ' + str(info_cnt))
    for i in range(info_cnt):
        info = info_arr[i]
        for j in range(len(info)):
            sheet.write(i, j, info[j])

    xls_dir = os.path.join(os.getcwd(), 'out', 'moments_info.xls')
    book.save(xls_dir)
    print('\n*** all info written in moments_info.xls. ***')
