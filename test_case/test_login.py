from page.login_page import LoginPage
from time import sleep

class TestLogin:

    def test_login_accountlogin(self, browser, base_url):
        """
        检查点：
        * 检查页面是否包含密码登录按钮。
        """
        page = LoginPage(browser)
        page.get(base_url)
        browser.switch_to.frame(0)
        page.password_login.click()

    def test_login_username(self, browser):
        """
        检查点：
        * 检查页面用户名是否正确。
        """
        page = LoginPage(browser)
        page.username.send_keys("14411000023")

    def test_login_password(self, browser):
        """
        检查点：
        * 检查密码是否正确。
        """
        page = LoginPage(browser)
        page.password.send_keys("yesterday")

    def test_login_button(self, browser):
        page = LoginPage(browser)
        page.login.click()
        sleep(2)


# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "test_login.py"])


