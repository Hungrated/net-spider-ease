from .pages import *

"""

获取歌手信息列表

:param start id下限
:param end id上限

"""


def get_artist_info(start, end):
    artist_info_arr = []
    for i in range(start, end):
        artist_info_temp = get_artist_detailed_by_id(i)
        if artist_info_temp is not None:
            print('fetching artist info where id = ' + str(i))
            artist_info_arr.append(artist_info_temp)
    return artist_info_arr


"""

获取歌手详细信息

:param id 歌手编号

"""


def get_artist_detailed_by_id(artist_id):
    desc_page = get_desc_page(artist_id)
    desc_page_soup = BeautifulSoup(desc_page, 'lxml')
    tlt = desc_page_soup.title.text
    if tlt != "网易云音乐":
        avatar_raw = desc_page_soup.find('div', {'class': 'n-artist'})
        desc_raw = desc_page_soup.find('div', {'class': 'n-artdesc'})
        avatar = avatar_raw.find('img').get('src') if avatar_raw is not None else ''
        desc_list = desc_raw.findAll('p') if desc_raw is not None else []
        return {
            'artist_id': artist_id,
            'avatar': get_decoded_content(avatar),
            'name': get_decoded_content(tlt.replace(" - 网易云音乐", "")),
            'page': get_decoded_content(BASE_URL + '/artist/desc?id=' + str(artist_id)),
            'desc': get_decoded_content(desc_list[0].text) if len(desc_list) > 0 else ''
        }
    return None


"""

保存歌手信息列表到文件

:param start id下限
:param end id上限

"""


def save_artist_info(start, end):
    artist_info_arr = get_artist_info(start, end)
    csv_dir = os.path.join(os.getcwd(), 'out', 'artists_info.csv')
    csv_file = codecs.open(csv_dir, 'w+', 'utf-8')
    try:
        writer = csv.writer(csv_file)
        writer.writerow(('artist_id', 'avatar', 'name', 'page', 'desc'))
        for artist in artist_info_arr:
            writer.writerow(
                (artist['artist_id'], artist['avatar'], artist['name'], artist['page'], artist['desc']))
    finally:
        csv_file.close()
        print("\ncsv file saved: artists_info.csv")


"""

读取歌手信息列表到文件

"""


def read_artist_info():
    csv_dir = os.path.join(os.getcwd(), 'out', 'artists_info.csv')
    try:
        info_lines = csv.reader(codecs.open(csv_dir, 'r', 'utf-8'))
        for artist in info_lines:
            print(artist)
    finally:
        print('\nall info done.')
