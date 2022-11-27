from time import sleep
from selenium.webdriver.common.keys import Keys
class ClearMessage():
    def __init__(self,twms,Contact,DeleteMessage):
        self.twms = twms
        self.Contact = Contact
        self.DeleteMessage = DeleteMessage
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.Contact)
            sleep(1.5)
            mains = self.twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").text  # CONTACT
            if mains.lower() in self.Contact.lower():
                mains = self.twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").click()  # CONTACT
                print(mains)
            else:
                mains = self.twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").click()  # CONTACT
                print("ESLE")
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
            if self.DeleteMessage.lower() == "YES".lower() or self.DeleteMessage.lower() == "DeleteMessage".lower() or self.DeleteMessage.lower() == "DELETE".lower():
                sleep(0.5)
                main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.Contact)
                sleep(1.5)
                mains = self.twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").text  # CONTACT
                if mains.lower() in self.Contact.lower():
                    mains = self.twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").click()  # CONTACT
                else:
                    mains = self.twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").click()  # CONTACT
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
                exits = twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("._14VsQ._23HdX").click()
        except:
            self.twms.refresh()
            sleep(10)