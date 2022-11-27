from time import sleep
class SendLinkGroup():
    def __init__(self,twms,NameGroup,NameMember):
        self.twms = twms
        self.NameGroup = NameGroup
        self.NameMember = NameMember
        try:
            sleep(1.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
            sleep(1.5)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(1.5)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(1.5)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1.5)
            data = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-5].click()
            sleep(1.5)
            data_group = self.twms.find_elements_by_css_selector("._32vnm._2k4Ax")[4].find_elements_by_css_selector("._3Pwfx._2XSjg")   # LINK
            x = len(data_group)
            sleep(0.2)
            y = x - 1
            sleep(0.2)
            data_group = self.twms.find_elements_by_css_selector("._32vnm._2k4Ax")[4].find_elements_by_css_selector("._3Pwfx._2XSjg")[-y].click()
            sleep(1.5)
            send_link = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_1OZ02]").click()
            sleep(1.5)
            select_member = self.twms.find_element_by_css_selector("div[class=_3e9k9]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameMember)
            sleep(1.5)
            selects_member = self.twms.find_element_by_css_selector("[class=_3e9k9]").find_element_by_css_selector("[class=_2eV08]").click()
            sleep(1.5)
            selects_members = self.twms.find_element_by_css_selector("[class=_3e9k9]").find_element_by_css_selector("[class=_2O38h]").find_element_by_css_selector("[class=_1WOQe]").click()
            sleep(1.5)
            send = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U").find_element_by_css_selector("[class=_3qpzV]").click()
            sleep(1.5)
        except:
            self.twms.refresh()
            sleep(10)