from time import sleep
class SendDocumentContact():
    def __init__(self,twms,Contact,Document):
        self.twms = twms
        self.Contact = Contact
        self.Document = Document
        try:
            sleep(2.5)
            main = twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.Contact)
            sleep(2.5)
            mains = twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").text  # CONTACT
            if mains.lower() in self.Contact.lower():
                mains = twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").click()  # CONTACT
                print(mains)
            else:
                mains = twms.find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("._3soxC._2aY82").find_element_by_css_selector("[class=_3es8f]").click()  # CONTACT
                print("ELSE")
            sleep(2.5)
            clean = twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(2.5)
            medias = twms.find_element_by_css_selector("span[data-icon='clip']").click()
            sleep(2.5)
            attach = twms.find_element_by_css_selector("input[type='file']")
            sleep(2.5)
            attach.send_keys(self.Document)
            sleep(2.5)
            send = twms.find_element_by_xpath("//div[contains(@class, '_3Git-')]")
            sleep(2.5)
            send.click()
            sleep(2.5)
        except:
            self.twms.refresh()
            sleep(10)