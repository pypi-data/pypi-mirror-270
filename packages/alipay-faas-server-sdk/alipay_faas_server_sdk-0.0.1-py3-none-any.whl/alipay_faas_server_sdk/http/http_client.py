import requests

from alipay_faas_server_sdk.http.http_request import HttpRequest
from alipay_faas_server_sdk.http.http_response import HttpResponse


class HttpClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def post(self, request: HttpRequest) -> HttpResponse:
        response = requests.post(
            self.endpoint + request.path, headers=request.headers, json=request.body
        )
        return HttpResponse(response)
