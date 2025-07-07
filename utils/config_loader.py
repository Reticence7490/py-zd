# utils/config_loader.py

import os
import yaml


class ConfigLoader:
    @staticmethod
    def load_config(config_type="web"):
        """
        加载 YAML 格式的配置文件
        :param config_type: "web" 或 "api"，对应 config.yaml 或 api_config.yaml
        :return: 配置字典
        """
        config_path = {
            "web": "config/config.yaml",
            "api": "config/api_config.yaml"
        }

        path = config_path.get(config_type)
        if not os.path.exists(path):
            logger.error(f"配置文件 {path} 不存在")
            raise FileNotFoundError(f"配置文件 {path} 不存在")

        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)