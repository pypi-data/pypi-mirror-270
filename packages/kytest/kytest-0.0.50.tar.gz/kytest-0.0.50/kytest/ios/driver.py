import os
import shutil
import subprocess
import time

import allure
import wda

from kytest.utils.log import logger
# from kytest.utils.common import retry, \
#     general_file_path, cut_and_upload
from kytest.utils.exceptions import KError
from kytest.ios.util import IosUtil


class IosDriver(object):

    def __init__(self, udid: str = None, bundle_id: str = None):
        """device_id可以是udid，也可以是wda服务url"""
        logger.info(f"初始化ios驱动: {udid}")

        self.pkg_name = bundle_id
        self.device_id = udid

        # 未传入设备id，默认获取usb连接的第一个设备
        if self.device_id is None:
            self.device_id = IosUtil.get_connected()[0]

        if 'http' in self.device_id:
            self.wda_url = self.device_id
        else:
            self.port = self.device_id.split("-")[0][-4:]
            self.wda_url = f"http://localhost:{self.port}"

        self.d = wda.Client(self.wda_url)

        # check if wda is ready
        if self.d.is_ready():
            logger.info('wda已就绪')
        else:
            if 'http' in self.device_id:
                raise KError("wda异常，请确认服务已正常启动！！！")
            else:
                logger.info('wda未就绪, 现在启动')
                for i in range(5):
                    try:
                        IosUtil(self.device_id).start_wda(port=self.port)
                        break
                    except Exception as e:
                        logger.info("启动wda异常，重试!!!")
                        logger.info(str(e))
                        continue
                if self.d.is_ready():
                    logger.info('wda启动成功')
                else:
                    raise KError('wda启动失败，可能是WebDriverAgent APP端证书失效!')

    def install_app(self, ipa_url, new=True, pkg_name=None):
        """安装应用
        @param pkg_name:
        @param ipa_url: ipa链接
        @param new: 是否先卸载
        @return:
        """
        logger.info(f"安装应用: {ipa_url}")
        if new is True:
            if pkg_name is not None:
                self.pkg_name = pkg_name
            if self.pkg_name is None:
                raise KError('应用bundle_id不能为空')
            self.uninstall_app()

        IosUtil(self.device_id).install_app(ipa_url)

    def uninstall_app(self, pkg_name=None):
        logger.info(f"卸载应用: {self.pkg_name}")
        if pkg_name is not None:
            self.pkg_name = pkg_name
        if self.pkg_name is None:
            raise KError('应用bundle_id不能为空')
        IosUtil(self.device_id).uninstall_app(self.pkg_name)

    def start_app(self, pkg_name=None, stop=True):
        """启动应用
        @param pkg_name:
        @param stop: 是否先停止应用
        """
        logger.info(f"启动应用: {self.pkg_name}")
        if pkg_name is not None:
            self.pkg_name = pkg_name
        if self.pkg_name is None:
            raise KError('应用bundle_id不能为空')

        if stop is True:
            self.d.app_terminate(self.pkg_name)
        self.d.app_start(self.pkg_name)

    def stop_app(self, pkg_name=None):
        logger.info(f"停止应用: {self.pkg_name}")
        if pkg_name is not None:
            self.pkg_name = pkg_name
        if self.pkg_name is None:
            raise KError('应用bundle_id不能为空')

        self.d.app_terminate(self.pkg_name)

    def back(self):
        """返回上一页"""
        logger.info("返回上一页")
        time.sleep(1)
        self.d.swipe(0, 100, 100, 100)

    def enter(self):
        logger.info("点击回车")
        self.d.send_keys("\n")

    def input(self, text: str, clear=False, enter=False):
        logger.info(f"输入文本: {text}")
        if clear is True:
            self.d.send_keys("")
        self.d.send_keys(text)
        if enter is True:
            self.enter()

    def click(self, x, y):
        logger.info(f"点击坐标: {x}, {y}")
        self.d.click(x, y)

    @staticmethod
    def general_file_path(file_name):
        logger.info("开始截图")
        if not file_name:
            raise ValueError("文件名不能为空")

        # 截图并保存到当前目录的image文件夹中
        relative_path = "screenshot"
        # 把文件名处理成test.png的样式
        if "." in file_name:
            file_name = file_name.split(r".")[0]
        if os.path.exists(relative_path) is False:
            os.mkdir(relative_path)

        time_str = time.strftime(f"%Y%m%d%H%M%S")
        file_name = f"{time_str}_{file_name}.jpg"
        file_path = os.path.join(relative_path, file_name)
        return file_path

    def screenshot(self, file_name=None):
        file_path = self.general_file_path(file_name)
        logger.info(f"保存至: {file_path}")
        self.d.screenshot(file_path)
        logger.info("截图上传allure报告")
        allure.attach.file(
            file_path,
            attachment_type=allure.attachment_type.PNG,
            name=f"{file_path}",
        )
        return file_path

    def click_alerts(self, alert_list: list):
        """点击弹窗"""
        logger.info(f"点击弹窗: {alert_list}")
        try:
            self.d.alert.click(alert_list)
        except:
            pass

    def swipe_up(self):
        self.d.swipe_up()

    def swipe_down(self):
        self.d.swipe_down()

    def swipe_left(self):
        self.d.swipe_left()

    def swipe_right(self):
        self.d.swipe_right()


if __name__ == '__main__':
    pass











