__version__ = "0.1.0"

import os
import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

__all__ = ["verify"]

# 公钥下载地址
AC_PUBLIC_KEY_URL = os.environ.get("AC_PUBLIC_KEY_URL", "keys/public_key.pem")


def verify(data: str, activation_code, public_key_path="keys/public_key.pem"):
    """
    验证激活码是否可用
    :param data:
    :param activation_code:
    :param public_key_path: 公钥路径
    :return:
    """
    public_key_path = os.path.expanduser(public_key_path)
    if not os.path.exists(public_key_path):
        os.makedirs(os.path.dirname(os.path.expanduser(public_key_path)), exist_ok=True)
        r = requests.get(AC_PUBLIC_KEY_URL)
        if r.ok:
            with open(public_key_path, 'wb') as f:
                f.write(r.content)
        else:
            raise Exception(f"public key fetch fail! {r.status_code}")

    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    try:
        public_key.verify(
            bytes.fromhex(activation_code),
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False


def node_verify(serial_number, node_id, activation_code):
    """
    节点级别激活码校验
    :param serial_number:
    :param node_id:
    :param activation_code:
    :return:
    """
    data = f"{serial_number}@node@{node_id}"
    return verify(data, activation_code=activation_code)


def device_verify(serial_number, activation_code):
    """
    设备级别激活码校验
    :param serial_number:
    :param activation_code:
    :return:
    """
    data = f"{serial_number}@device"
    return verify(data, activation_code=activation_code)


def server_verify(serial_number, activation_code):
    """
    服务器级别激活码校验
    :param serial_number:
    :param activation_code:
    :return:
    """
    data = f"{serial_number}@server"
    return verify(data, activation_code=activation_code)
