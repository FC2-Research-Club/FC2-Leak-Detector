# -*- coding: utf-8 -*-
"""
FC2 流出检测器-UI - 启动脚本

此文件是程序的入口点，负责启动主程序并执行初始化工作
"""

import logging
import sys
from contextlib import contextmanager
from datetime import datetime

from PySide2.QtWidgets import QApplication

# 检查必要的依赖是否已安装
try:
    import bs4
    import requests
    import rich
except ImportError as e:
    missing_lib = str(e).split("'")[1]
    print(f"\n错误: 缺少必要的库 '{missing_lib}'")
    print("\n请使用以下命令安装所需依赖:")
    print("pip install -r requirements.txt")
    print("\n安装完成后再次运行程序。")
    sys.exit(1)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s: %(message)s", level=logging.INFO
)


@contextmanager
def time_tracker(description: str):
    start_time = datetime.now()
    print(f"\n=== {description} 启动于 {start_time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
    try:
        yield
    finally:
        end_time = datetime.now()
        duration = end_time - start_time
        duration_str = f"{duration.seconds // 60}分{duration.seconds % 60}秒"
        print(f"\n=== 程序运行结束，耗时: {duration_str} ===\n")


def main() -> int:
    try:
        # 检查Python版本
        if sys.version_info < (3, 8):
            print("错误: 需要Python 3.8或更高版本")
            sys.exit(1)

        # 初始化配置（会自动创建必要的目录）
        from config import config

        # 显示启动信息
        with time_tracker("FC2流出检测器"):
            # 导入并启动主程序
            from src.ui.mian_window import MainWindow
            app = QApplication([])
            main_window = MainWindow()
            main_window.show()
            app.exec_()

    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
        return 130  # SIGINT标准退出码
    except Exception as e:
        print(f"\n程序启动错误: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
