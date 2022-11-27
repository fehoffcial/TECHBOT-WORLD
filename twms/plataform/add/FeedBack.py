from time import sleep
class FeedBack():
    def __init__(self,twms,SendFeedBack):
        self.twms = twms
        self.SendFeedBack = SendFeedBack
        try:
            send = twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.SendFeedBack)
            send_msg = twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("[class=_3qpzV]").click()
            sleep(0.5)
        except:
            self.twms.refresh()
            sleep(10)