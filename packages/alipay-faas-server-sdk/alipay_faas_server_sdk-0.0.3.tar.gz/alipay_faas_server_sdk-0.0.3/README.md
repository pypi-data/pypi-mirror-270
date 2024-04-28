## 支付宝云开发服务端SDK

### 安装

在云函数的requirements.txt中添加依赖：

```txt
alipay-faas-server-sdk
```

### 使用

在云函数中引用SDK，示例代码如下：

```python
from alipay_faas_server_sdk import Cloud


def main(event, context):
    cloud = Cloud(context)
    context['logger'].info("function start ...")

    # call function test-sum
    response = cloud.callFunction("test-sum", {'x': 1, 'y': 2})
    return response.data
```
