"""
@Author: kang.yang
@Date: 2024/4/29 14:16
"""
import adbutils

from kytest.utils.log import logger
from kytest.utils.exceptions import KError


class AdrUtil:
    """后续封装一下adb命令进来"""

    def __init__(self, device_id):
        self.device_id = device_id

    @staticmethod
    def get_connected():
        """获取当前连接的手机列表"""
        device_list = adbutils.adb.device_list()
        if device_list:
            device_id_list = [device.serial for device in device_list]
        else:
            device_id_list = []
        if len(device_id_list) > 0:
            logger.info(f"已连接设备列表: {device_id_list}")
            return device_id_list
        else:
            raise KError(msg=f"无已连接设备")
