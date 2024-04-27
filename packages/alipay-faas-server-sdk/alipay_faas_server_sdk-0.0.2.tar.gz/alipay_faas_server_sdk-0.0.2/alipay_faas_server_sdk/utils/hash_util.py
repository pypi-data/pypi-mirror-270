import hashlib
import hmac


def sha256_hash(message: str) -> str:
    """
    计算 Sha256 哈希值
    """
    # 创建SHA-256哈希对象
    sha256 = hashlib.sha256()
    # 更新哈希对象的输入
    sha256.update(message.encode("utf-8"))
    # 获取哈希值（十六进制格式）
    return sha256.hexdigest()


def encrypted_sha256_hash(message: str, secret: str) -> str:
    """
    计算带有密钥的 SHA256 HMAC 哈希值
    """
    # 使用HMAC-SHA256算法创建哈希对象
    hmac_sha256_hash = hmac.new(
        secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256
    )
    # 获取哈希值（十六进制格式）
    return hmac_sha256_hash.hexdigest()
