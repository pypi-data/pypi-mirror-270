# _*_ coding : utf-8 _*_
# @Time: 2024/4/24 16:34
# @Author : ZhiBoYuan
# @File : cipher
# @Project : upload
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad


class CipherCalculate:

    def aes_encrypt_message(self, message, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(message, AES.block_size))
        return ciphertext

    def aes_ecrypt_message(self, ciphertext, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_message

# 加密函数
    def des_encrypt(self, data, key):
        """
        使用 DES 加密数据。

        参数:
            data (str): 要加密的明文
            key (str): 8 位长的密钥

        返回值:
            bytes: 密文
        """
        des_encryptor = DES.new(key, DES.MODE_ECB)
        # 填充数据到 8 位的倍数
        pad = len(data) % 8
        data = data + pad * chr(pad)
        # 加密数据
        ciphertext = des_encryptor.encrypt(data.encode('utf-8'))
        return ciphertext

    def des_decrypt(self, ciphertext, key):
        """
        使用 DES 解密密文。

        参数:
            ciphertext (bytes): 密文
            key (str): 8 位长的密钥

        返回值:
            str: 明文
        """
        des_decryptor = DES.new(key, DES.MODE_ECB)
        # 解密数据
        data = des_decryptor.decrypt(ciphertext)
        # 去除填充
        data = data.decode('utf-8').rstrip(chr(data[-1]))
        return data


if __name__ == '__main__':
    cipher_calculate = CipherCalculate()

    # 测试代码
    data = "Hello, World!"
    key = "12345678"

    # 加密
    ciphertext = cipher_calculate.des_encrypt(data, key)
    print("密文:", ciphertext.hex())

    # 解密
    decrypted_data = cipher_calculate.des_decrypt(ciphertext, key)
    print("明文:", decrypted_data)




