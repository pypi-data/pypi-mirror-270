# _*_ coding : utf-8 _*_
# @Time: 2024/4/26 14:47
# @Author : ZhiBoYuan
# @File : bloom_check
# @Project : upload
from redisbloom.client import Client


class BloomCheck:
    def __init__(self, host, port, db):
        self.rb = Client(host=host, port=port, db=db)


    def bloom_create(self, key, error_rate, capacity):
        self.rb.bfCreate(key, error_rate, capacity)

    def bloom_add(self, key, value):
        return self.rb.bfAdd(key, value)

    def bloom_exists(self, key, value):
        return self.rb.bfExists(key, value)