import os
import codecs
import csv

"""

初始化文件


"""


def init_moment_info():
    csv_dir = os.path.join(os.getcwd(), 'out', 'moments_info.csv')
    csv_file = codecs.open(csv_dir, 'w+', 'utf-8')
    try:
        writer = csv.writer(csv_file)
        writer.writerow(('pub_time', 'like_cnt', 'content_o', 'content_f', 'img_list'))
    finally:
        csv_file.close()
        print("\n*** csv file initialized: moments_info.csv ***\n")


"""

保存说说信息列表到文件

:param arr 结构化信息列表

"""


def save_moment_info(arr):
    csv_dir = os.path.join(os.getcwd(), 'out', 'moments_info.csv')
    csv_file = codecs.open(csv_dir, 'a', 'utf-8')
    try:
        writer = csv.writer(csv_file)
        for moment in arr:
            writer.writerow((moment['pub_time'], moment['like_cnt'], moment['content_o'], moment['content_f'],
                             str(moment['img_list'])))
    finally:
        csv_file.close()
        print("\n*** csv file saved: moments_info.csv ***\n")
