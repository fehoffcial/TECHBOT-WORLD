from time import sleep
class AddMemberGroup():
    def __init__(self,twms,NameGroup,NameMember):
        self.twms = twms
        self.NameGroup = NameGroup
        self.NameMember = NameMember
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
            sleep(1)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(0.5)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(0.5)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(0.5)
            setups = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-5].click()
            sleep(0.5)
            addmember = self.twms.find_element_by_css_selector(".i5ly3._299go").find_element_by_css_selector("[class=_LNcL]").find_element_by_css_selector("._3Pwfx._2XSjg").click()
            sleep(1)
            addmembers = self.twms.find_element_by_css_selector("label[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameMember)
            sleep(2)
            addsmembers = self.twms.find_element_by_css_selector("[class=_2fuxX]").find_element_by_css_selector("._3Pwfx._3qF0b").click()
            sleep(1)
            click = self.twms.find_element_by_css_selector("[class=_2fuxX]").find_element_by_css_selector("[class=_1WOQe]").click()
            sleep(1)
            clicks = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_element_by_css_selector("._30EVj.gMRg5").click()
            sleep(0.9)
            exit = self.twms.find_element_by_css_selector("button[class=hYtwT]").click()
        except:
            self.twms.refresh()