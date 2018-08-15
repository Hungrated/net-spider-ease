import cloudmusic

# 获取页面html
# html1 = get_page_content(BASE_URL)

# 获取页面中导航网址信息
# obj_arr1 = get_objective_set(html1, 'a', 'href', '^(/discover/)')

# print(obj_arr1)

# 获取二级页面中歌手链接信息
# html2 = get_page_content(BASE_URL + obj_arr1[3])
# obj_arr2 = get_objective_set(html2, 'a', 'href', '/artist\?id=[0-9]+')

# print(obj_arr2)

# artists = set(obj_arr2)

# print(artists)

# 获取歌手详细信息
# artist0 = get_artist_detailed_by_id(6452)
# print(artist0)

# 迭代获取id对应的歌手信息并存储到本地文件
# artists.save_artist_info(1870, 3000)

# 读取歌手信息
cloudmusic.artists.read_artist_info()
