import uuid

from alipay_faas_server_sdk.config.cloud_config import CloudConfig
from alipay_faas_server_sdk.context.alipay_context import AlipayContext
from alipay_faas_server_sdk.function.fn_request import CallFunctionParam
from alipay_faas_server_sdk.function.fn_response import CallFunctionResult
from alipay_faas_server_sdk.http.http_client import HttpClient
from alipay_faas_server_sdk.http.http_constants import HttpHeader, HttpMethod
from alipay_faas_server_sdk.http.http_request import HttpRequest


class FunctionClient(HttpClient):
    SIGNED_HEADER_NAMES = [
        HttpHeader.CLIENT_TIMESTAMP,
        HttpHeader.FROM_ENV_ID,
        HttpHeader.TO_ENV_ID,
        HttpHeader.FROM_INSTANCE_ID,
        HttpHeader.FROM_APP_ID,
        HttpHeader.FROM_FUNCTION_NAME,
        HttpHeader.TO_FUNCTION_NAME,
    ]

    def __init__(
        self,
        logger,
        cloud_config: CloudConfig,
        alipay_context: AlipayContext,
        to_env_id: str = "",
    ):
        super().__init__(cloud_config.function_gateway_endpoint)
        self.alipay_context = alipay_context
        self.secret_id = cloud_config.secret_id
        self.secret_key = cloud_config.secret_key
        self.from_instance_id = cloud_config.function_instance_id
        self.from_function_name = cloud_config.function_name
        self.from_env_id = cloud_config.function_env_id
        self.to_env_id = to_env_id or cloud_config.function_env_id
        self.logger = logger

    def call_function(self, request: CallFunctionParam) -> CallFunctionResult:
        to_env_id = request.config.env or self.to_env_id
        trace_id = self.alipay_context.trace_id or str(uuid.uuid4())

        headers = {
            # 参与鉴权的头
            HttpHeader.FROM_ENV_ID: self.from_env_id,
            HttpHeader.TO_ENV_ID: to_env_id,
            HttpHeader.FROM_INSTANCE_ID: self.from_instance_id,
            HttpHeader.FROM_APP_ID: self.alipay_context.from_app_id,
            HttpHeader.FROM_FUNCTION_NAME: self.from_function_name,
            HttpHeader.TO_FUNCTION_NAME: request.name,
            HttpHeader.TRACE_ID: trace_id,
            HttpHeader.ALIPAY_CALL_ID: trace_id,
            HttpHeader.REQUEST_ID: trace_id,
            HttpHeader.SOAF_RPC_ID: f"{self.alipay_context.rpc_id}.{++self.alipay_context.rpc_count}",
            # TODO: 后续确认
            HttpHeader.ALIPAY_SOURCE: f"{self.alipay_context.source if self.alipay_context.source else 'alipay_unknown'},alipay_unknown",
            HttpHeader.USER_AGENT: "SDK_USER_AGENT",
        }

        http_request = HttpRequest(
            self.secret_id,
            self.secret_key,
            self.SIGNED_HEADER_NAMES,
            headers,
            HttpMethod.POST,
            self.endpoint,
            "/functions/invokeFunction",
            "",
            request.data,
        )
        # self.logger.info(f'got http_request={json.dumps(http_request, default=vars)}')
        http_response = self.post(http_request)
        # self.logger.info(f'got http_response={json.dumps(http_response, default=vars)}')
        result = CallFunctionResult(http_response)
        return result
