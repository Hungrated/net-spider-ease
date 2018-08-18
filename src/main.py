from qzone import *

arr = browse.browse_qzone_moments(75, 255)
print('count: ', len(arr))
for i in range(len(arr)):
    print(str(i+1), ': \t', arr[i]['pub_time'], '\t\t', arr[i]['like_cnt'], '\t\t', arr[i]['content_o'])
