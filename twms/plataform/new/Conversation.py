from time import sleep
class Conversation():
    def __init__(self,twms,Contact,Message):
        self.twms = twms
        self.Contact = Contact
        self.Message = Message
        try:
            enter_conversation = self.twms.find_element_by_css_selector("[class=_1eNef]").find_elements_by_css_selector("[class=_2wfYK]")[-2].click()
            sleep(1)
            click_conversation = self.twms.find_element_by_css_selector("[class=_2Evw0]").click()
            sleep(1)
            contact_conversation = self.twms.find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.Contact)
            sleep(1)
            click_user = self.twms.find_element_by_css_selector("[class=_3Tw1q]").click()
            sleep(1)
            send_message = self.twms.find_elements_by_css_selector("._1awRl.copyable-text.selectable-text")[-1].send_keys(self.Message)
            sleep(1)
            send = self.twms.find_element_by_css_selector("[class=_2Ujuu]").click()
            sleep(1)
        except:
            self.twms.refresh()
            sleep(10)