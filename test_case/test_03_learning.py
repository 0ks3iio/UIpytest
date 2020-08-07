from page.learning_page import LearningPage

class TestLearning:

    def test_learning_skip(self, browser):
        page = LearningPage(browser)
        browser.switch_to.default_content()
        page.skip.click()

    def test_learning_close_exam(self, browser):
        page = LearningPage(browser)
        page.close_exam.click()

    def test_learning_display(self, browser):
        page = LearningPage(browser)
        page.display.click()

    def test_learning_enter_ust(self, browser):
        page = LearningPage(browser)
        page.enter_ust.click()



