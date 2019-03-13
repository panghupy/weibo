import requests
import json
import time


# 发送消息脚本
# m.weibo.com
def sendMessageWeb(uid='3866009452', content='hello'):
    sendMessageUrl = 'https://m.weibo.cn/api/chat/send'
    # 校验码
    st = '2926d6'

    headers = {
        'authority': 'm.weibo.cn',
        'method': 'POST',
        'path': '/api/chat/send',
        'scheme': 'https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': '34',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_T_WM=99f896e6d354eeebe1bae00460784d93; SUB=_2A25xjNpxDeRhGeVG7VQR8CfIzj6IHXVSjuY5rDV6PUJbkdAKLUTBkW1NT44gMDpCpsHe4JFsnvweR5AasyOaGm2v; SUHB=0y0Z7mTDE_ETpp; MLOGIN=1; XSRF-TOKEN=2926d6; WEIBOCN_FROM=1110105030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076036346456479%26uicode%3D20000174',
        'origin': 'https://m.weibo.cn',
        'mweibo-pwa': '1',
        'origin': 'https://m.weibo.cn',
        'referer': 'https://m.weibo.cn/message/chat?uid=3318777442&name=msgbox',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    formdata = {
        'uid': uid,
        'fileld': 'null',
        'content': content,
        'st': st

    }

    response = requests.post(url=sendMessageUrl, data=formdata, headers=headers)
    result = response.content.decode('gbk').encode('utf-8').decode('unicode_escape')
    return json.loads(result)


if __name__ == '__main__':
    result = sendMessageWeb()
    print(result)
