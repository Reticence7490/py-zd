# base_page.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class BasePage:
    def __init__(self, driver=None):
        """
        初始化浏览器驱动。
        如果没有传入 driver，则默认启动一个新的 Chrome 浏览器实例。
        """
        if driver is None:
            self.driver = webdriver.Chrome()  # 可替换为 Firefox、Edge 等
        else:
            self.driver = driver

    def open(self, url):
        """
        打开指定网页
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, *locator):
        """
        查找单个元素
        :param locator: 定位方式，例如 (By.ID, "username")
        :return: WebElement
        """
        return self.driver.find_element(*locator)

    def click(self, *locator):
        """
        点击元素
        """
        element = self.find_element(*locator)
        element.click()

    def input_text(self, text, *locator):
        """
        在输入框中输入文本
        """
        element = self.find_element(*locator)
        element.send_keys(text)

    def get_title(self):
        """
        获取当前页面的标题
        """
        return self.driver.title

    def get_page_source(self):
        """
        获取当前页面的 HTML 源码
        """
        return self.driver.page_source

    def wait_for_element(self, *locator, timeout=10):
        """
        显式等待某个元素出现
        """
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def take_screenshot(self, filename="screenshot.png"):
        """
        截图并保存到本地
        """
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        filepath = os.path.join(screenshots_dir, filename)
        self.driver.save_screenshot(filepath)
        print(f"截图已保存至：{filepath}")

    def close(self):
        """
        关闭浏览器
        """
        self.driver.quit()