from qzone import *

html = browse.browse_qzone_moments()
raw_arr = pages.get_moment_set(html)
parsed_arr = pages.get_parsed_moment(raw_arr)
print(parsed_arr)
