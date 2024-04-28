class AlipayContext:
    """
    Alipay 环境，每个函数执行请求都不一样
    """

    def __init__(self, alipay_context: dict):
        self.union_id = alipay_context.get("unionId", "")
        self.client_ip = alipay_context.get("clientIp", "")
        self.client_ipv6 = alipay_context.get("clientIpv6", "")
        self.from_app_id = alipay_context.get("fromAppId", "")
        self.from_open_id = alipay_context.get("fromOpenId", "")
        self.from_union_id = alipay_context.get("fromUnionId", "")
        self.open_data_info = alipay_context.get("openDataInfo", "")
        self.app_id = alipay_context.get("appId", "")
        self.open_id = alipay_context.get("openId", "")
        self.env = alipay_context.get("env", "")
        self.source = alipay_context.get("source", "")
        self.trace_id = alipay_context.get("traceId", "")
        self.rpc_id = alipay_context.get("rpcId", "")
        self.request_id = alipay_context.get("requestId", "")
        self.rpc_count = alipay_context.get("rpcCount", "")
        self.user_agent = alipay_context.get("userAgent", "")
