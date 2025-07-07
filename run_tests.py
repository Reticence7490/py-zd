if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    os.makedirs("reports/allure-results", exist_ok=True)

    pytest.main([
        "--alluredir=./reports/allure-results/",
        "testcases/"
    ])