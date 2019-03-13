from DataTools.tools import MysqlHelper

from sendMsg_script import sendMessageWeb
import time

# 设置关键词
kw = '创始人'

# 链接数据库
mysqlHelper = MysqlHelper('localhost', 'root', '123456', 'weibo_userinfo')
mysqlHelper.connect()

params = kw
sql = 'select nickname,uid from User where kw=%s and is_send=0'
data = mysqlHelper.fetchall(sql, params)  # tuple
for userinfo in data:
    # sendMessageWeb(userinfo)
    nickname, uid = userinfo
    result = sendMessageWeb(uid=uid, content='have a good time!')
    if result['ok']:
        print('发送消息成功---------')
        params = [uid, kw]
        sql = 'update User set is_send=1 where uid=%s and kw=%s'
        count = mysqlHelper.update(sql, params)

        if count > 0:
            print('更新数据库---------')
    else:
        print('发现错误！：')
        print(result['msg'])
        mysqlHelper.close()
    time.sleep(5)










