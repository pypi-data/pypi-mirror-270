#!/usr/bin/env python3
# coding: utf-8

# Alipay.com Inc.
# Copyright (c) 2004-2024 All Rights Reserved.
# @Filename: aa.py
# @Author:   齐渊
# @Time:     2024/4/26 17:47

"""
"""
from alipay_faas_client_sdk.function.fn_client import FunctionClient
from alipay_faas_client_sdk.function.fn_request import CallFunctionParam
from alipay_faas_client_sdk.function.fn_request import CallFunctionConfig
from alipay_faas_client_sdk.function.fn_response import CallFunctionResult


class Cloud:
    def __init__(
        self,
        app_id: str,
        env_id: str,
        access_key_id: str,
        access_key_secret: str,
        endpoint: str = "",
    ):
        self.app_id = app_id
        self.env_id = env_id
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint or f"https://{env_id}.api-hz.cloudbasefunction.cn"
        self.fn_client = None

    def callFunction(
        self, name: str, data: dict, config: CallFunctionConfig = None
    ) -> CallFunctionResult:
        if not self.fn_client:
            self.fn_client = FunctionClient(
                self.app_id,
                self.env_id,
                self.access_key_id,
                self.access_key_secret,
                self.endpoint,
            )
        request = CallFunctionParam(name, data, config)
        return self.fn_client.call_function(request)
