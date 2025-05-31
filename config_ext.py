"""
拓展的配置模块

主要为ui部分提供一些配置的设置
"""


import os

# 获取项目根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class ConfigExt:
    """配置类，用于管理所有配置项"""

    _instance = None

    def __new__(cls):
        """单例模式，确保全局只有一个Config实例"""
        if cls._instance is None:
            cls._instance = super(ConfigExt, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """初始化配置项，只在第一次创建实例时执行"""
        if self._initialized:
            return

        self._initialized = True

        # -------------------------
        # 路径配置
        # -------------------------
        self.root_dir = ROOT_DIR
        self.config_dir = os.path.join(self.root_dir, "config")
        self.config_file = os.path.join(self.config_dir, "config.json")
        self.ui_dir = os.path.join(self.root_dir, "ui")
        self.ui_mian_window = os.path.join(self.ui_dir, "mian_window.ui")
        self.ui_setting_window = os.path.join(self.ui_dir, "setting_window.ui")
        self.run_file = os.path.join(self.root_dir, "run.py")

# 创建全局配置实例
config = ConfigExt()
