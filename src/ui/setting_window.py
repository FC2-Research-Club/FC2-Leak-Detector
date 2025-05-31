"""
UI界面的设置窗口

主要提供一些本地化配置,如代理设置,线程设置
"""

import json

from PySide2.QtCore import QFile, Qt
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import  QDialogButtonBox, QMessageBox

from config_ext import config as config_ext
from src.utils import config_util
from src.utils.config_util import config_const

class SettingWindow:

    _instance = None

    def __new__(cls, *args):
        """单例模式"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self,parent=None):
        #----------------
        # 加载配置ui
        # ----------------
        q_file = QFile(config_ext.ui_setting_window)
        q_file.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(q_file)
        q_file.close()

        # ----------------
        #设置为模态窗口
        # ----------------
        self.ui.parent = parent
        self.ui.setWindowModality(Qt.ApplicationModal)
        # self.ui.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Dialog)  # 置顶且为对话框

        # ----------------
        # 绑定事件
        # ----------------
        self.ui.button_box_yn.clicked.connect(self.save_or_cancel_event)
        self.ui.radio_button_proxy.clicked.connect(self.proxy_input_controller)
        self.ui.radio_button_no_proxy.clicked.connect(self.proxy_input_controller)

    def show(self):
        """展示配置页面"""
        self.ui.show()
        self.bind_data()

    def save_or_cancel_event(self, button):
        """关闭窗口的一些事件"""
        role = self.ui.button_box_yn.buttonRole(button)
        if role == QDialogButtonBox.AcceptRole:
            self.save_and_close()
        elif role == QDialogButtonBox.RejectRole:
            self.ui.reject()
        elif role == QDialogButtonBox.ActionRole:
            pass  # 自定义操作

    def bind_data(self):
        """打开配置界面时绑定数据"""
        local_config = config_util.load_local_config()
        if local_config is None:
            self.proxy_input_controller()#无配置文件时执行默认禁用
            return
        self.ui.input_thread.setValue(local_config[config_const.MaxWorkers])
        self.ui.input_ip.setText(local_config[config_const.ProxyIP])
        self.ui.input_port.setValue(local_config[config_const.ProxyPort])
        self.ui.radio_button_proxy.setChecked(local_config[config_const.EnableProxy])
        self.ui.radio_button_no_proxy.setChecked(not local_config[config_const.EnableProxy])
        self.proxy_input_controller()

    def proxy_input_controller(self):
        enable_flag = self.ui.radio_button_proxy.isChecked()
        self.ui.input_ip.setEnabled(enable_flag)
        self.ui.input_port.setEnabled(enable_flag)

    def save_and_close(self):
        """保存配置并关闭"""
        try:
            local_config = config_util.load_local_config() or {}
            with open(config_ext.config_file, 'w', encoding='utf-8') as f:
                local_config[config_const.MaxWorkers] = self.ui.input_thread.value()
                local_config[config_const.ProxyIP] = self.ui.input_ip.displayText()
                local_config[config_const.ProxyPort] = self.ui.input_port.value()
                local_config[config_const.EnableProxy] = self.ui.radio_button_proxy.isChecked()
                json.dump(local_config, f, ensure_ascii=False, indent=2)
        except json.decoder.JSONDecodeError as e:
            QMessageBox.warning(self.ui, '提示','配置失败')
        except FileNotFoundError as e:
            pass

        # 确认关闭
        self.ui.accept()

    # def closeEvent(self, event):
    #     """重写关闭事件，提示保存"""
    #     print(13123)
    #     if self.ui.text_input.document().isModified():
    #         # 弹出确认对话框（示例：自定义弹窗）
    #         from PySide2.QtWidgets import QMessageBox
    #         reply = QMessageBox.question(
    #             self.ui, '提示', '内容未保存，是否退出？',
    #             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
    #         )
    #         if reply == QMessageBox.Save:
    #             self.save_and_close()
    #             event.accept()
    #         elif reply == QMessageBox.Discard:
    #             event.accept()
    #         else:
    #             event.ignore()
    #     else:
    #         event.accept()

