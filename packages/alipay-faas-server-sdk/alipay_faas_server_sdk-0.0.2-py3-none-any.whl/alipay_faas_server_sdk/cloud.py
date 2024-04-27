#!/usr/bin/env python3
# coding: utf-8
from alipay_faas_server_sdk.config.cloud_config import CloudConfig
from alipay_faas_server_sdk.context.alipay_context import AlipayContext
from alipay_faas_server_sdk.function.fn_client import FunctionClient
from alipay_faas_server_sdk.function.fn_request import CallFunctionParam
from alipay_faas_server_sdk.function.fn_request import CallFunctionConfig
from alipay_faas_server_sdk.function.fn_response import CallFunctionResult


class Cloud:
    def __init__(self, context):
        self.logger = context["logger"]
        self.fn_config = CloudConfig("/dev/function/config")
        self.context = context
        self.alipay_context = AlipayContext(context["alipayContext"])
        self.fn_client = None
        # self.logger.info(f'got alipayContext={json.dumps(self.alipay_context, default=vars)}')
        # self.logger.info(f'got fn_config={json.dumps(self.fn_config, default=vars)}')

    def callFunction(
        self, name: str, data: dict, config: CallFunctionConfig = None
    ) -> CallFunctionResult:
        if not self.fn_client:
            self.fn_client = FunctionClient(
                self.logger, self.fn_config, self.alipay_context
            )
        request = CallFunctionParam(name, data, config)
        return self.fn_client.call_function(request)
