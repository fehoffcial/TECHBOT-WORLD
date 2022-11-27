from time import sleep
class Document():
    def __init__(self,twms,document):
        self.twms = twms
        self.document = document
        try:
            sleep(2.5)
            documents = self.twms.find_element_by_css_selector("span[data-icon='clip']").click()
            sleep(2.5)
            attach = twms.find_elements_by_css_selector("input[type='file']")[-2]
            sleep(2.5)
            attach.send_keys(self.document)
            sleep(2.5)
            send = self.twms.find_element_by_xpath("//div[contains(@class, '_3Git-')]")
            sleep(2.5)
            send.click()
            sleep(2.5)
        except:
            self.twms.refresh()