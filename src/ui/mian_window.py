"""
UI界面的主窗口

主要是提供原命令窗口功能的一个中转UI,通过UI发送cmd指令给cmd窗口,实现一定的图形界面功能
"""

import os
import sys

from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog

from config_ext import config as config_ext
from src.ui.setting_window import SettingWindow
from src.utils import config_util
from src.utils.config_util import config_const

class MainWindow:

    def __init__(self):

        self.qsubmit_thread_call = None

        # ----------------
        # 加载配置ui
        # ----------------
        q_file = QFile(config_ext.ui_mian_window)
        q_file.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(q_file)
        q_file.close()

        #绑定事件
        self.ui.qsubmit_button.clicked.connect(self.qsubmit)
        self.ui.setting_button.clicked.connect(self.open_setting_window)
        self.ui.sites_button.clicked.connect(self.check_sites)
        self.ui.extract_button.clicked.connect(self.check_extract)
        self.ui.config_button.clicked.connect(self.check_config)
        self.ui.command_button.clicked.connect(self.check_command)

    def show(self):
        # 如有数据绑定逻辑可以放在此方法内
        self.ui.show()

    def check_sites(self):
        cmd_arg = f"start cmd /k python {config_ext.run_file} -s"
        os.system(cmd_arg)
    def check_extract(self):
        local_config = config_util.load_local_config()
        self.set_proxy(local_config)
        cmd_arg = f"start cmd /k python {config_ext.run_file} -e"
        os.system(cmd_arg)
    def check_config(self):
        cmd_arg = f"start cmd /k python {config_ext.run_file} -c"
        os.system(cmd_arg)
    def check_command(self):
        cmd_arg = f"start cmd /k python {config_ext.run_file} -h"
        os.system(cmd_arg)

    def qsubmit(self):
        """调用cmd窗口查询"""
        # 获取输入
        target_id = self.ui.qvalue_input.toPlainText()
        type_index = self.ui.qtype_box.currentIndex()
        batch_check = self.ui.batch_box.isChecked()
        no_image = self.ui.no_image_box.isChecked()
        no_magnet = self.ui.no_magnet_box.isChecked()

        #加载配置
        local_config = config_util.load_local_config()
        max_workers = self.get_max_thread(local_config)
        self.set_proxy(local_config)

        #设定参数映射
        check_dict = {
            0 : {0 : "-w", 1: "b"},     #作者ID
            1 : { 0: "-a", 1: "-ba" },  #女优ID
            2 : { 0: "-v", 1: "-v"} }   #视频ID

        #拼接参数
        cmd_args = [
            "start cmd /k",
            "python", config_ext.run_file,
            check_dict[type_index][batch_check],
            target_id,
        ]

        if no_image:
            cmd_args.append("--no-image")
        if no_magnet:
            cmd_args.append("--no-magnet")
        if max_workers > 0:
            cmd_args.append(f"-t {max_workers}")

        os.system(" ".join(map(str, cmd_args)))

    # def start_single_cmd(self, cmd_args):
    #     try:
    #         subprocess.run(
    #             cmd_args,
    #             shell=True,
    #             creationflags=subprocess.CREATE_NEW_CONSOLE,
    #             cwd=config.root_dir, #运行路径
    #             capture_output=True, #捕获子进程输出
    #             text=True, #以文本模式处理
    #             check=True,  # 非零状态码时抛出异常
    #             # encoding="utf-8"
    #         )
    #     except subprocess.CalledProcessError as e:
    #         print(f"命令执行失败！错误信息：\n{e.stderr}")

    def set_proxy(self, local_config):
        """设置代理"""
        if local_config is None or not local_config[config_const.EnableProxy]:
            os.environ["HTTP_PROXY"] = ""
            os.environ["HTTPS_PROXY"] = ""
        else:
            try:
                proxy_adr = f"http://{local_config[config_const.ProxyIP]}:{local_config[config_const.ProxyPort]}"
                os.environ["HTTP_PROXY"] = proxy_adr
                os.environ["HTTPS_PROXY"] = proxy_adr
            except KeyError:
                #读取配置失败,就不设置配置了
                pass

    def get_max_thread(self, local_config):
        if local_config is None:
            return 0
        try:
            return int(local_config[config_const.MaxWorkers])
        except KeyError:
            return 0

    def open_setting_window(self):
        """打开子窗口并处理返回数据"""
        setting_window = SettingWindow(self.ui)
        setting_window.show()
        if setting_window.ui.exec_() != QDialog.Accepted:
            print("子窗口取消操作")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
