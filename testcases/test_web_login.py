# testcases/test_web_login.py
import pytest
from utils.excel_reader import ExcelReader

@pytest.mark.parametrize("username, password, expected", ExcelReader.read_excel("data/web_login_data.xlsx"))
def test_web_login(username, password, expected):
    # 登录并验证
    assert expected in page.get_page_source()