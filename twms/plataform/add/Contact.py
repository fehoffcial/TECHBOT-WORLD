from time import sleep
class Contact():
    def __init__(self,twms,NameContact):
        self.twms = twms
        self.NameContact = NameContact
        try:
            sleep(0.3)
            main = self.twms.find_element_by_css_selector("[class=_2ig1U]").find_element_by_css_selector("[class=_2wfYK]").click()
            sleep(0.3)
            mains = self.twms.find_element_by_css_selector("[class=eBZuM]").find_element_by_css_selector("[class=_2c4Sf]").find_element_by_css_selector("[data-icon=attach-contact]").click()
            sleep(0.3)
            contact = self.twms.find_element_by_css_selector("[class=_3e9k9]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys("Ariel")
            sleep(0.3)
            select_contact = self.twms.find_element_by_css_selector("[class=_3e9k9]").find_element_by_css_selector("._3soxC._2aY82").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()
            sleep(2)
            select_contacts = self.twms.find_element_by_css_selector("[class=_3e9k9]").find_element_by_css_selector("span[class=_2O38h]").find_element_by_css_selector("[role=button]").click()
            sleep(0.9)
            info_contact = self.twms.find_element_by_css_selector("[class=_3e9k9]").find_element_by_css_selector("[class=RgZeN]").text  # INFO SEND CONTACT
            sleep(0.5)
            send_contact = self.twms.find_element_by_css_selector("[class=_3e9k9]").find_element_by_css_selector("[class=_2VmYo]").find_element_by_css_selector("[role=button]").click()
            sleep(2)
        except:
            self.twms.refresh()