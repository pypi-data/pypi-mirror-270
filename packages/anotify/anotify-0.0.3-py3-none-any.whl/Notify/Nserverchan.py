import requests
import json

class ServerChanNotify:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://sctapi.ftqq.com/{token}.send'

    # https://sct.ftqq.com/sendkey
    def send_msg(self, msg_title, msg_text):
        """发送消息
        :msg_title: 主题
        :msg_text:  正文
        :return:    发送是否成功
        """

        data = {
            "text": msg_title,
            "desp": msg_text,
        }

        request_url = f"{self.base_url}?title={msg_title}&desp={msg_text}"

        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    url = 'https://devapi.qweather.com/v7/weather/3d?location=101210111&key=8f7753973dfb4fac8ca5d008417d380f'
    response = requests.get(url).json()
    token = 'SCT34026T9J1u1Xsecbz8djhLKfJT1PgV'
    print(ServerChanNotify(token).send_msg("测试标题", "测试正文"))

