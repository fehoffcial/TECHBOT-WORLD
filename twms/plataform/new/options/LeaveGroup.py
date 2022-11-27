from time import sleep
class LeaveGroup():
    def __init__(self,twms,NameGroup,DELETE):
        self.twms = twms
        self.NameGroup = NameGroup
        self.DELETE = DELETE
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
            sleep(2)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(2)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(1)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            leave = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-1].click()
            sleep(0.5)
            exit = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_element_by_css_selector("[class=_2SGGH]").find_element_by_css_selector("._30EVj.gMRg5").click()
            if "DELETE".lower() in self.DELETE.lower():
                sleep(0.5)
                main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
                sleep(2)
                mains = self.twms.find_element_by_css_selector("[class=_2aA2V]").click()
                sleep(2)
                clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
                sleep(1)
                setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
                sleep(1)
                leave = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-1].click()
                sleep(0.5)
                exit = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_element_by_css_selector("[class=_2SGGH]").find_element_by_css_selector("._30EVj.gMRg5").click()

        except:
            self.twms.refresh()
