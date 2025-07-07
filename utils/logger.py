# utils/logger.py

import logging
import os
from datetime import datetime


class Logger:
    def __init__(self, log_file="logs/test.log"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # 文件日志处理器
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # 控制台日志处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 日志格式
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加处理器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger


# 全局单例，方便其他模块调用
logger = Logger().get_logger()