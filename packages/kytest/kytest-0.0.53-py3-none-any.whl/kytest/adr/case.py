"""
@Author: kang.yang
@Date: 2023/10/26 09:48
"""
import time

import allure

from .driver import AdrDriver
from .element import AdrElem
from kytest.utils.log import logger
from kytest.utils.config import kconfig
from kytest.api.request import HttpReq
from kytest.running.conf import App


class TestCase(HttpReq):
    """
    测试用例基类，所有测试用例需要继承该类
    """

    driver: AdrDriver = None
    auto_start: bool = True

    # ---------------------初始化-------------------------------
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        try:
            cls().start_class()
        except BaseException as e:
            logger.error(f"start_class Exception: {e}")

    @classmethod
    def teardown_class(cls):
        try:
            cls().end_class()
        except BaseException as e:
            logger.error(f"end_class Exception: {e}")

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def config(self):
        """
        目前就是用来设置是否自动启动应用
        @return:
        """
        pass

    def setup_method(self):
        # 设置调整
        self.config()

        # 设置默认feature
        project_name = kconfig['project']
        if project_name:
            allure.dynamic.feature(project_name)

        # 记录用例执行开始时间
        self.start_time = time.time()

        # 驱动初始化
        self.driver = AdrDriver(App.did, App.pkg)

        # 启动应用
        if self.auto_start is True:
            self.driver.start_app()

        self.start()

    def teardown_method(self):
        self.end()

        # 停止应用
        if self.auto_start is True:
            self.driver.stop_app()

        take_time = time.time() - self.start_time
        logger.info("用例耗时: {:.2f} s".format(take_time))

    # 公共方法
    @staticmethod
    def sleep(n: float):
        """休眠"""
        logger.info(f"暂停: {n}s")
        time.sleep(n)

    def screenshot(self, name: str):
        """截图"""
        self.driver.screenshot(name)

    # UI方法
    def elem(self, *args, **kwargs):
        return AdrElem(self.driver, *args, **kwargs)

    # 安卓方法
    def assert_act(self, activity_name: str, timeout=5):
        """断言当前页面的activity"""
        self.driver.assert_act(activity_name, timeout)
