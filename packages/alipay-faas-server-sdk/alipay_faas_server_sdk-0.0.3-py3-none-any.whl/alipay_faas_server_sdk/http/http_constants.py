class HttpHeader:
    # Http 必须请求头
    HOST = "Host"
    CONTENT_TYPE = "Content-Type"
    CONTENT_LENGTH = "Content-Length"
    AUTHORIZATION = "Authorization"

    # 需要参与签名的头
    CLIENT_TIMESTAMP = "x-client-timestamp"
    FROM_ENV_ID = "x-from-env-id"
    TO_ENV_ID = "x-to-env-id"
    FROM_INSTANCE_ID = "x-from-instance-id"
    FROM_FUNCTION_NAME = "x-from-function-name"
    TO_FUNCTION_NAME = "x-to-function-name"

    # 函数节点网关返回的响应头
    FROM_APP_ID = "x-from-app-id"
    TRACE_ID = "x-trace-id"
    REQUEST_ID = "x-request-id"
    REAL_IP = "x-real-ip"
    SOAF_TRACE_ID = "sofa-traceid"
    SOAF_RPC_ID = "sofa-rpcid"
    ALIPAY_UNION_ID = "alipay-unionid"
    ALIPAY_OPEN_ID = "x-alipay-openid"
    ALIPAY_SOURCE = "x-alipay-source"
    ALIPAY_CALL_ID = "x-alipay-callid"

    USER_AGENT = "user-agent"


class HttpMethod:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class HttpPrefix:
    HTTP = "http://"
    HTTPS = "https://"
