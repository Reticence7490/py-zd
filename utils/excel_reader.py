# utils/excel_reader.py

import pandas as pd


class ExcelReader:
    @staticmethod
    def read_excel(file_path):
        """
        读取 Excel 文件中的测试数据
        :param file_path: Excel 文件路径（如 data/web_login_data.xlsx）
        :return: 二维列表 [[username, password, expected], ...]
        """
        try:
            df = pd.read_excel(file_path)
            return [tuple(row) for row in df.to_numpy()]
        except Exception as e:
            logger.error(f"读取 Excel 失败: {e}")
            raise