import os


def get_env_or_default(env_name: str, default_value: str = ""):
    value = os.getenv(env_name)
    if value is None:
        value = default_value
    return value
