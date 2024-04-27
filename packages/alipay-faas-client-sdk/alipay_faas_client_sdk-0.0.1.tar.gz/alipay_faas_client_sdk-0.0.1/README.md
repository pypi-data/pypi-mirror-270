## 支付宝云开发ClientSDK

### 安装

```txt
pip install alipay-faas-client-sdk
```

### 使用

引用SDK，示例代码如下：

```python
import json
from alipay_faas_client_sdk import Cloud


def main(event, context):
    cloud = Cloud(
        app_id="2021001234567890",
        env_id="env-00xyzxyzxyz",
        access_key_id="ak_xxxxx",
        access_key_secret="sk_yyyyy",
    )
    data = {"name": "bob", "age": 23}
    result = cloud.callFunction("add-user", data)
    print(json.dumps(result, indent=4, default=vars))
```
