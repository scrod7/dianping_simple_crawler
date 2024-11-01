from tqdm import tqdm
from function.search import Search
from function.detail import Detail

d = Detail()
s=Search()
CHANNEL_ID=0
need_pages=1
keyword='炸鸡'
city_id="1"
def get_search_url(cur_page, city_id, keyword='炸鸡'):
    """
    获取搜索链接
    @param cur_page: 当前页码
    @param city_id: 城市ID
    @param channel_id: 频道ID
    @param keyword: 搜索关键字
    @return: 拼接好的搜索URL和一些需要的选项
    """
    # 使用简单的字符串拼接构建URL
    base_url = 'http://www.dianping.com/search/keyword/' + city_id + '/0_' + keyword + '/p'

    # 根据页码构建搜索URL
    if cur_page == 1:
        return base_url + "1", 'proxy, cookie'
    else:
        return base_url + str(cur_page), 'proxy, cookie'

for page in tqdm(range(1, need_pages+1), desc='搜索页数'):
    search_url, request_type = get_search_url(page, city_id)
    print(search_url, city_id)
    search_res = s.search(search_url, request_type)
    if not search_res:
        break
    print(search_res)
    for each_search_res in tqdm(search_res, desc='详细爬取'):
        # 爬取推荐菜
        shop_id = each_search_res['店铺id']
        each_detail_res = d.get_detail(shop_id)
        each_search_res.update(each_detail_res)
        print(each_search_res)

    if len(search_res) < 15:
        break