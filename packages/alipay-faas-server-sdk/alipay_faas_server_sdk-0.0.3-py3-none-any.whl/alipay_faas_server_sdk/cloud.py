#!/usr/bin/env python3
# coding: utf-8
import logging
from alipay_faas_server_sdk.config.cloud_config import CloudConfig
from alipay_faas_server_sdk.context.alipay_context import AlipayContext
from alipay_faas_server_sdk.function.fn_client import FunctionClient
from alipay_faas_server_sdk.function.fn_request import CallFunctionParam
from alipay_faas_server_sdk.function.fn_request import CallFunctionConfig
from alipay_faas_server_sdk.function.fn_response import CallFunctionResult


class Cloud:
    def __init__(self, context):
        self.logger = logging.getLogger("system")
        self.fn_config = CloudConfig("/dev/function/config")
        self.context = context
        self.alipay_context = AlipayContext(context["alipayContext"])
        self.fn_client = None

    def callFunction(
        self, name: str, data: dict, config: CallFunctionConfig = None
    ) -> CallFunctionResult:
        if not self.fn_client:
            self.fn_client = FunctionClient(
                self.logger, self.fn_config, self.alipay_context
            )
        request = CallFunctionParam(name, data, config)
        return self.fn_client.call_function(request)
