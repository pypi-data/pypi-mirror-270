import json
import time

from alipay_faas_server_sdk.http.http_constants import HttpHeader, HttpPrefix
from alipay_faas_server_sdk.utils.hash_util import sha256_hash, encrypted_sha256_hash


class HttpRequest:
    # 签名算法
    ALGORITHM = "HMAC-SHA256"

    def __init__(
        self,
        secret_id: str,
        secret_key: str,
        signed_headers: list,
        headers: dict,
        method: str,
        host: str,
        path: str,
        query: str = "",
        body=None,
        is_mysql: bool = False,
    ):
        self.timestamp = str(int(time.time() * 1000))
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.method = method
        self.host = host
        self.path = path if not is_mysql else ""
        self.query = query if not is_mysql else ""
        self.body = body or {}
        self.signed_headers = signed_headers
        self.headers = headers

        # 必要的头
        headers[HttpHeader.CLIENT_TIMESTAMP] = self.timestamp
        # if host:
        #     headers[HttpHeader.HOST] = host.removeprefix(HttpPrefix.HTTP).removeprefix(HttpPrefix.HTTPS)
        # if body:
        #     headers[HttpHeader.CONTENT_TYPE] = 'application/json'
        # headers[HttpHeader.CONTENT_LENGTH] = str(len(body))

        # 生成签名头
        self.headers[HttpHeader.AUTHORIZATION] = self.sign()

    def sign(self):
        """
        生成请求签名
        """
        signed_header_names = ";".join(self.signed_headers)
        canonical_signed_headers = ""
        for header_name in self.signed_headers:
            header_value = self.headers[header_name]
            canonical_signed_headers = (
                f"{canonical_signed_headers}{header_name}:{header_value}\n"
            )

        canonical_request = f"{self.method.upper()}\n{self.path}\n{self.query}\n{canonical_signed_headers}\n{signed_header_names}\n{sha256_hash(json.dumps(self.body, default=vars))}\n"
        string_to_sign = (
            f"{self.ALGORITHM}\n{self.timestamp}\n{sha256_hash(canonical_request)}\n"
        )
        # 私钥加密
        signature = encrypted_sha256_hash(string_to_sign, self.secret_key)
        # 提供公钥用于解密
        auth = f"{self.ALGORITHM} Credential={self.secret_id}, SignedHeaders={signed_header_names}, Signature={signature}"
        return auth
