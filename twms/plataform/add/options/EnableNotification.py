from time import sleep
class EnableNotification:
    def __init__(self,twms,Contact):
        self.twms = twms
        self.Contact = Contact
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.Contact)
            sleep(1.5)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(1)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(0.5)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            notification = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-3].click()
            sleep(1)
        except:
            self.twms.refresh()
            sleep(10)
