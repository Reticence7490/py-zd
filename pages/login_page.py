# login_page.py
from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")

    def input_username(self, username):
        self.input_text(username, *self.USERNAME_FIELD)

    def input_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()