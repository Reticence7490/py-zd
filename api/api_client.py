# api/api_client.py
from api.request_utils import RequestUtils
from utils.config_loader import load_api_config


class APIClient:
    def __init__(self):
        config = load_api_config()  # 从 config/api_config.yaml 读取配置
        self.base_url = config["base_url"]
        self.login_endpoint = config["login_endpoint"]
        self.headers = config.get("headers", {})
        self.utils = RequestUtils()

    def login(self, payload):
        """
        发送登录请求
        :param payload: 登录参数（如 username, password）
        :return: 接口响应内容（JSON 格式）
        """
        url = f"{self.base_url}{self.login_endpoint}"
        return self.utils.send_request("POST", url, json=payload, headers=self.headers)