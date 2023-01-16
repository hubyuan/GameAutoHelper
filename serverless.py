# -*- coding: utf-8 -*-

import sys
import logging
import requests
import sys
import json
import time

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

logger.info('Loading function')


def sendMessage():
    url = 'http://v.juhe.cn/toutiao/index'

    params = {
        "type": "caijing",
        "page_size": 1,
        "is_filter": 1,
        # 头条类型,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
        "key": "c8014ca13c83b6b369d6a961798fb136",  # 您申请的接口API接口请求Key
    }

    content = requests.get(url, params=params)

    if (content):
        try:
            result = json.loads(content.text)
            error_code = result['error_code']
            if (error_code == 0):
                data = result['result']['data']
                for i in data:
                    # 更多字段可参考接口文档
                    contentText = "新闻标题：" + i['title'] + "\n新闻时间：" + i['date'] + "\n新闻链接：" + i[
                        'url'] + "\n\n"
                    text = {"msg_type": "text", "content": {"text": contentText}}
                    zxurl = 'https://open.feishu.cn/open-apis/bot/v2/hook/4d368042-8410-4132-ae7b-58a241999c99'
                    requests.post(zxurl, data=json.dumps(text))

            else:
                print("请求失败:%s %s" % (result['error_code'], result['reason']))
        except Exception as e:
            print("解析结果异常：%s" % e)
    else:
        # 可能网络异常等问题，无法获取返回内容，请求异常
        print("请求异常")


def main_handler(event, content):
    # def main_handler():
    logger.info('start main_handler')

    sendMessage()
