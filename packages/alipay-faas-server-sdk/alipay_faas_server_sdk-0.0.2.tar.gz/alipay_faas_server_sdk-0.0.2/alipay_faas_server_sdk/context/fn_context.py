from alipay_faas_server_sdk.context.alipay_context import AlipayContext


class FnContext:
    """
    用户函数执行的入参 Context
    """

    def __init__(
        self,
        app_id: str,
        trace_id: str,
        request_id: str,
        rpc_id: str,
        alipay_context: AlipayContext,
        http_request,
        logger,
    ):
        self.app_id = app_id
        self.trace_id = trace_id
        self.request_id = request_id
        self.rpc_id = rpc_id
        self.alipay_context = alipay_context
        self.http_request = http_request
        self.logger = logger
