import requests

class IyuuNotify:
    def __init__(self, token):
        self.token = token

    def send_msg(self, title, content):
        url = "https://iyuu.cn/" + self.token + '.send?text=' + title + '&desp=' + content
        response = requests.get(url)
        return response.text




if __name__ == "__main__":
    iyuu = IyuuNotify("IYUU26149Td97113d936c006fa0ce9022ce771d54da1727aaa")
    print(iyuu.send_msg("title", "content"))
