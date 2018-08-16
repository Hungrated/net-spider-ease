from Crypto import Random
from Crypto.Cipher import AES

KEY = '2018081620180816'

"""

将字符串加密

:param raw 原始字符串

"""


def encrypt_str(raw):
    iv = Random.new().read(AES.block_size)  # block_size = 16
    cipher = AES.new(KEY, AES.MODE_CFB, iv)
    return iv + cipher.encrypt(raw)


"""

将字符串解密

:param raw 加密后的字符串

"""


def decrypt_str(data):
    iv = data[:16]
    cipher = AES.new(KEY, AES.MODE_CFB, iv)
    return str(cipher.decrypt(data[16:]), 'utf-8')
