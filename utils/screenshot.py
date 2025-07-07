# utils/screenshot.py

import os
from datetime import datetime


class Screenshot:
    def __init__(self, driver):
        self.driver = driver
        self.screenshots_dir = "screenshots"
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def take_screenshot(self, filename=None):
        """
        截图并保存到本地
        :param filename: 文件名（可选），默认使用时间戳命名
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"error_{timestamp}.png"

        filepath = os.path.join(self.screenshots_dir, filename)
        self.driver.save_screenshot(filepath)
        logger.info(f"截图已保存至：{filepath}")