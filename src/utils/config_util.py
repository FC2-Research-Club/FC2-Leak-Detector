"""
本地配置工具类

提供给本地配置的工具方法
"""

import json
import os

from config_ext import config as config_ext

class ConfigConst:
    _instance = None
    def __new__(cls, *args):
        """单例模式"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    @classmethod
    def freeze(cls):
        cls.__frozen = True

    ProxyIP = "proxy_host"
    ProxyPort = "proxy_port"
    EnableProxy = "enable_proxy"
    MaxWorkers = "max_workers"

config_const = ConfigConst()


def load_local_config():
    """读取本地配置"""

    if not os.path.exists(config_ext.config_dir):
        os.mkdir(config_ext.config_dir)
        return

    if not os.path.exists(config_ext.config_file):
        return

    try:
        with (open(config_ext.config_file, 'rb') as f):
            if f.read().strip() is (None or b''):
                return
            f.seek(0)
            return json.load(f)
    except FileNotFoundError as e:
        # 没发现配置则无视
        pass



