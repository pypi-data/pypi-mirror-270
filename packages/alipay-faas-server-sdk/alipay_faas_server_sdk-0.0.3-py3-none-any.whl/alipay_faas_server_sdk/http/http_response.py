import requests


class HttpResponse:
    def __init__(self, response: requests.Response):
        self.status_code = response.status_code
        self.headers = {}
        for key, value in response.headers.items():
            self.headers[key] = value
        self.raw_body = response.text
        try:
            # 判断返回体是否可以转换为JSON
            self.body = response.json()
        except ValueError:
            self.body = {}
