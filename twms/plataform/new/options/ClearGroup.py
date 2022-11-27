from time import sleep
class ClearGroup():
    def __init__(self,twms,NameGroup):
        self.twms = twms
        self.NameGroup = NameGroup
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
            sleep(1.5)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(0.5)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(0.5)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(0.5)
            cleangroup = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-2].click()
            sleep(0.5)
            cleangroups = self.twms.find_element_by_css_selector("[class=sWE2H]").find_element_by_css_selector("[class=_2SGGH]").find_element_by_css_selector("._30EVj.gMRg5").click()
            sleep(0.5)
            exit = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("._14VsQ._23HdX").click()

        except:
            self.twms.refresh()
            sleep(10)