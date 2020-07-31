from poium import Page, NewPageElement

class LearningPage(Page):

    skip = NewPageElement(xpath="//div[@class='jump']", describe="跳过")
    close_exam = NewPageElement(xpath="//div[@class='closebtn whiteBgImg']", describe="关闭测评")
    display = NewPageElement(xpath="//div[@class='entrance-item animated zoomIn'][4]/img", describe="进入课后小剧场")
    enter_ust = NewPageElement(xpath="//div[@class='card-box vertical bg2']/div/div[1]", describe="进入ust列表页")

