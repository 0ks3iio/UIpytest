# 定义基本测试环境
import os

import pytest
from py.xml import html
from selenium import webdriver
from config import RunConfig
from utils.readconfig import ReadIni


# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"


def pytest_configure(config):
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
    config._metadata.pop("Packages")
    config._metadata.pop("Platform")
    config._metadata.pop("Plugins")
    config._metadata.pop("Python")
    config._metadata['接口地址'] = 'https://www.XXXX'
    config._metadata['项目名称'] = '自动化测试学习中心'

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("测试人员: wjw")])

# 定义基本测试环境地址
@pytest.fixture(scope='function')
def base_url():
    return ReadIni().get_value('url', 'url')

# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.pop()


# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            capture_screenshots(case_name)
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        # report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html

def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        RunConfig.driver.save_screenshot(image_dir)

# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
   全局定义浏览器驱动
   :return:
   """
    global driver
    web = ReadIni().get_value('browser', 'browser')

    if web == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif web == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver
    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close(browser):
    yield driver
    driver.quit()
    print("test end!")