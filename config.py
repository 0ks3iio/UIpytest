

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_case/"

    # 配置浏览器驱动类型(chrome/firefox)。
    driver_type = "chrome"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "1"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
