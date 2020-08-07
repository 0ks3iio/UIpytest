# coding=utf-8
import os
import time
import logging
import pytest
import click
from conftest import REPORT_DIR
from config import RunConfig
from logs.log import Log
from utils.postemail import SendMail


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py  (回归模式，生成HTML报告)
  > python run_tests.py -m debug  (调试模式)
'''

@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        try:
            logger.info("回归模式，开始执行✈✈！")
            # now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
            now_time = time.strftime("%Y_%m_%d")
            RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)
            if not os.path.exists(RunConfig.NEW_REPORT):
                os.makedirs(RunConfig.NEW_REPORT)
                print("report文件新建成功：%s" % RunConfig.NEW_REPORT)
            else:
                print("report文件已存在！！！")
        except BaseException as msg:
            Log.getLog(RunConfig.NEW_REPORT).error("%s : 新建report文件失败" % msg)

        try:
            if not os.path.exists(RunConfig.NEW_REPORT + "/image"):
                os.mkdir(RunConfig.NEW_REPORT + "/image")
                print("image文件新建成功：%s" % RunConfig.NEW_REPORT)
            else:
                print("image文件已存在！！！")
        except BaseException as msg:
            Log.getLog(RunConfig.NEW_REPORT).error("%s : 新建image文件失败" % msg)

        html_report = os.path.join(RunConfig.NEW_REPORT, "report.html")
        xml_report = os.path.join(RunConfig.NEW_REPORT, "junit-xml.xml")
        pytest.main(["-s", "-v", RunConfig.cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
        Log.getLog(RunConfig.NEW_REPORT).info("运行结束，生成测试报告♥❤！")
        try:
            m = SendMail(
                # 遗留问题：下面注释的三行读出来是个tuple
                username=RunConfig.username,
                passwd=RunConfig.password,
                recv=RunConfig.recv,
                title=RunConfig.title,
                content=RunConfig.content,
                # # recv=['448112172@qq.com','yujingfeng@didiglobal.com', 'zhanglili8@100tal.com'],
                file=os.path.dirname(os.getcwd()) + '/UIpytest/test_report/' + time.strftime("%Y_%m_%d") + '/report.html',
                ssl=True
            )
            m.send_mail()
        except BaseException as msg:
            Log.getLog(RunConfig.NEW_REPORT).info("%s : report报告发送失败" % msg)

    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()




