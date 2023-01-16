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
    code = '011113,003095'
    url = 'https://api.doctorxiong.club/v1/fund?code='+code


    content = requests.get(url)

    if (content):
        try:
            result = json.loads(content.text)
            error_code = result['code']
            if (error_code == 200):
                data = result['data']
                for i in data:
                    # 更多字段可参考接口文档
                    contentText = "基金代码：" + i['code'] + "\n基金名称：" + i['name'] + "\n净值估算日涨幅：" + i[
                        'expectGrowth'] + "\n"
                    text = {"msg_type": "text", "content": {"text": contentText}}
                    zxurl = 'https://open.feishu.cn/open-apis/bot/v2/hook/4d368042-8410-4132-ae7b-58a241999c99'
                    # print(text)
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

