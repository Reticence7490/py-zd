import pytest
from api.api_client import APIClient
from utils.excel_reader import ExcelReader


# 从 Excel 读取测试数据（需提前准备好 api_login_data.xlsx）
@pytest.mark.parametrize("username, password, expected", ExcelReader.read_excel("data/api_login_data.xlsx"))
def test_api_login(username, password, expected):
    """
    测试登录接口功能
    - 发送 POST 请求到登录接口
    - 验证返回结果是否符合预期
    """
    client = APIClient()
    try:
        # 构造请求数据
        payload = {
            "username": username,
            "password": password
        }

        # 调用登录接口
        response = client.login(payload)
        print(f"响应内容: {response}")  # 可选：打印响应内容用于调试

        # 验证响应中是否包含预期字段（如 "token" 或 "error"）
        assert expected in str(response), f"期望包含 {expected}，实际响应为 {response}"

    except Exception as e:
        # 失败时记录日志（可扩展为截图）
        print(f"接口测试失败: {e}")
        raise e  # 抛出异常标记测试失败