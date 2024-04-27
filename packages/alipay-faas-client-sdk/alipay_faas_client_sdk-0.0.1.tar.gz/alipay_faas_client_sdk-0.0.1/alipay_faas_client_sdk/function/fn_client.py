import uuid
import json
import logging

from alipay_faas_client_sdk.function.fn_request import CallFunctionParam
from alipay_faas_client_sdk.function.fn_response import CallFunctionResult
from alipay_faas_client_sdk.http.http_client import HttpClient
from alipay_faas_client_sdk.http.http_constants import HttpHeader, HttpMethod
from alipay_faas_client_sdk.http.http_request import HttpRequest


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
        app_id: str,
        env_id: str,
        access_key_id: str,
        access_key_secret: str,
        endpoint: str,
    ):
        super().__init__(endpoint)
        self.app_id = app_id
        self.env_id = env_id
        self.secret_id = access_key_id
        self.secret_key = access_key_secret
        self.from_instance_id = "processId"

    def call_function(self, request: CallFunctionParam) -> CallFunctionResult:
        to_env_id = request.config.env or self.env_id
        trace_id = str(uuid.uuid4())

        headers = {
            # 参与鉴权的头
            HttpHeader.X_ALIPAY_APP_ID: self.app_id,
            HttpHeader.FROM_ENV_ID: self.env_id,
            HttpHeader.TO_ENV_ID: to_env_id,
            HttpHeader.FROM_INSTANCE_ID: self.from_instance_id,
            HttpHeader.FROM_APP_ID: self.app_id,
            HttpHeader.FROM_FUNCTION_NAME: request.name,
            HttpHeader.TO_FUNCTION_NAME: request.name,
            HttpHeader.TRACE_ID: trace_id,
            HttpHeader.ALIPAY_CALL_ID: trace_id,
            HttpHeader.REQUEST_ID: trace_id,
            # HttpHeader.SOAF_RPC_ID: f"{self.alipay_context.rpc_id}.{++self.alipay_context.rpc_count}",
            # TODO: 后续确认
            # HttpHeader.ALIPAY_SOURCE: f"{self.alipay_context.source if self.alipay_context.source else 'alipay_unknown'},alipay_unknown",
            HttpHeader.USER_AGENT: "WEB_SDK_USER_AGENT",
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
        logging.info(f"got http_request={json.dumps(http_request, default=vars)}")
        http_response = self.post(http_request)
        logging.info(f"got http_response={json.dumps(http_response, default=vars)}")
        result = CallFunctionResult(http_response)
        return result
