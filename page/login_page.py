from poium import Page, NewPageElement


# 登录页面
class LoginPage(Page):

    password_login = NewPageElement(xpath="//div[@class='sms-password-title']/span[2]", describe="密码登录")
    username = NewPageElement(xpath="//div[@class='username-text-panel']/input", describe="账号")
    password = NewPageElement(xpath="//div[@class='username-password-panel']/input", describe="密码")
    login = NewPageElement(xpath="//div[@class='login-btn-panel']/span", describe="登录")


