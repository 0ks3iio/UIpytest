from time import sleep

from page.parent_page import ParentPage


class TestParent:
    def test_parent_change_child(self, browser):
        page = ParentPage(browser)
        browser.switch_to.default_content()
        page.change_child.click()

    def test_parent_choose_child(self, browser):
        page = ParentPage(browser)
        page.choose_child.click()

    def test_parent_child_confirm(self, browser):
        page = ParentPage(browser)
        page.child_confirm.click()

    def test_parent_enter_center(self, browser):
        page = ParentPage(browser)
        now_handle = browser.current_window_handle  # 获取当前窗口句柄
        page.enter_center.click()
        all_handles = browser.window_handles
        for handle in all_handles:
            if handle != now_handle:
                browser.close()
                browser.switch_to.window(handle)
        sleep(8)



