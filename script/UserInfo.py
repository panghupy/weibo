import requests
from lxml import etree
from DataTools.tools import MysqlHelper


# 抓取微博找人下关键词搜索50页用户数据并存入数据库

def write_data(nickname, uid, kw):
    mysqlHelper = MysqlHelper('localhost', 'root', '123456', 'weibo_userinfo')
    mysqlHelper.connect()
    params = [nickname, uid, kw]
    sql = 'insert into User(nickname,uid,kw) values(%s,%s,%s) '
    count = mysqlHelper.insert(sql, params)
    if count > 0:
        print('成功写入数据库')


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
# 设置关键词
kw = '创始人'

for page in range(1, 51):
    url = 'https://s.weibo.com/user?q=' + kw + '&Refer=weibo_user&page=' + str(page)

    response = requests.get(url, headers=headers)
    html = etree.HTML(response.content)
    user_list = html.xpath('//div[@id="pl_user_feedList"]//div[@class="card card-user-b s-pg16 s-brt1"]')
    for userinfo in user_list:
        userName = userinfo.xpath('.//div[@class="info"]//a[@class="name"]')[0].xpath('string(.)')
        userId = userinfo.xpath('.//div[@class="info"]//a[@class="s-btn-c"]/@uid')[0]
        print('用户昵称：', userName, '用户ID：', userId)

        count = write_data(userName, userId, kw)
