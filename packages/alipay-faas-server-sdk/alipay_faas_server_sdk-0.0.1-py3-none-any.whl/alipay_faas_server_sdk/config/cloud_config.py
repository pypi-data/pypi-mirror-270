class CloudConfig:
    """
    云函数配置
    """

    def __init__(self, config_file: str):
        # FIXME: runtime 没有传入，需要 sdk 自己从本地自行读取一遍
        configs = load_config_file(config_file)
        self.secret_id = configs.get("RUNTIME_ACCESS_KEY", "")
        self.secret_key = configs.get("RUNTIME_SECRET_KEY", "")
        self.function_env_id = configs.get("RUNTIME_ENV_ID", "")
        self.function_name = configs.get("RUNTIME_FUNCTION_NAME", "")
        self.function_gateway_endpoint = configs.get(
            "RUNTIME_FUNCTION_GATEWAY_ENDPOINT", ""
        )
        self.function_instance_id = configs.get("RUNTIME_FUNCTION_INSTANCE_ID", "")
        self.function_database_endpoint = configs.get(
            "RUNTIME_MONGO_CLUSTER_ENDPOINT", ""
        )
        self.function_database_name = configs.get("RUNTIME_MONGO_DATABASE_NAME", "")
        self.function_storage_endpoint = configs.get("RUNTIME_OSS_ENDPOINT", "")
        self.function_mysql_endpoint = configs.get("RUNTIME_MYSQL_ENDPOINT", "")
        self.function_redis_endpoint = configs.get("RUNTIME_REDIS_ENDPOINT", "")
        self.timeout = configs.get("max-req-timeout", "")
        self.runtime_version = configs.get("runtime-version", "")


def load_config_file(config_file: str) -> dict:
    """
    从本地文件中加载函数配置，加载失败会返回空数据
    """
    configs = {}
    with open(config_file, "r") as file:
        line = "start"
        while line:
            line = file.readline()
            items = line.split("=")
            if len(items) != 2:
                continue
            configs[items[0].strip("\r\n ")] = items[1].strip("\r\n ")
    return configs
