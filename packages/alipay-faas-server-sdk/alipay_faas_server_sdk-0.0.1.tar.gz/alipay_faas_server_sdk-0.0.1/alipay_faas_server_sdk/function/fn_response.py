from alipay_faas_server_sdk.http.http_response import HttpResponse


class CallFunctionResult:
    def __init__(self, response: HttpResponse):
        self.status = response.status_code
        self.data = response.body
        self.err_msg = response.body.get("errMsg", "")
        self.err_code = response.body.get("errCode", "")
