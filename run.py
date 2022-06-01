import requests
import json

url_min_home = 'https://api.caiyunapp.com/v2.6/BXXnwRilDNMnQVhD/120.2133,30.2597/minutely'
url_hou_home = 'https://api.caiyunapp.com/v2.6/BXXnwRilDNMnQVhD/120.2133,30.2597/hourly?hourlysteps=1'

url_min_work = 'https://api.caiyunapp.com/v2.6/BXXnwRilDNMnQVhD/120.1397,30.1847/minutely'
url_hou_work = 'https://api.caiyunapp.com/v2.6/BXXnwRilDNMnQVhD/120.1397,30.1847/hourly?hourlysteps=1'


# 2、钉钉机器人的调用
def dd_robot(msg):
    HEADERS = {"Content-Type": "application/json;charset=utf-8"}
    # 需要替换成自己的key
    key = "78cfa5b09eadf54212edc59302406b27e9c01e105cc002fa8f50463022b09ee8"
    # 签名
    sign = '天气'
    url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % key
    data_info = {
        "msgtype": "markdown",
        "markdown": {
            "title": "早晚天气提醒",
            "text": "\n" + msg
        },
        "isAtAll": True
    }
    value = json.dumps(data_info)
    response = requests.post(url, data=value, headers=HEADERS)


def search_weather_min(url):
    rep = requests.get(url, timeout=60)
    rep.encoding = 'utf-8'
    jsonText = json.loads(rep.text)
    result = jsonText['result']
    minutely = result['minutely']
    desc = minutely['description']
    return desc


def search_weather_hou(url):
    rep = requests.get(url, timeout=60)
    rep.encoding = 'utf-8'
    jsonText = json.loads(rep.text)
    result = jsonText['result']
    hourly = result['hourly']
    desc = hourly['description']
    return desc


if __name__ == '__main__':
    min_home = search_weather_min(url_min_home)
    hou_home = search_weather_hou(url_hou_home)
    min_work = search_weather_min(url_min_work)
    hou_work = search_weather_hou(url_hou_work)

    text = '## 钱江四苑\n' \
           '⏳ 分钟预报：' + min_home + "\
           ⏰ 小时预报：" + hou_home + '\n' \
                                 '## 海创基地\n' \
                                 '⏳ 分钟预报：' + min_work + "\
                                                         ⏰ 小时预报：" + hou_work
    dd_robot(text)
    print(text.replace(" ",""))
