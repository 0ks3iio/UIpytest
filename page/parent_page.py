from poium import Page, NewPageElement

class ParentPage(Page):

    change_child = NewPageElement(xpath="//*[@id='js-child-switcher-btn']", describe="切换孩子")
    choose_child = NewPageElement(xpath="//li[@class='child-avatar-item'][1]/div/img", describe="选择孩子")
    child_confirm = NewPageElement(xpath="//button[@id='js-child-switch-confirm']", describe="child确认按钮")
    enter_center = NewPageElement(xpath="//*[@id='js-side-learning-center-btn']", describe="进入学习中心")
