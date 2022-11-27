from time import sleep
class Media():
    def __init__(self,twms,Media):
        self.twms = twms
        self.Media = Media
        try:
            sleep(2.5)
            medias = self.twms.find_element_by_css_selector("span[data-icon='clip']").click()
            sleep(1.5)
            attach = self.twms.find_element_by_css_selector("input[type='file']")
            sleep(2.5)
            attach.send_keys(self.Media)
            sleep(1.5)
            send = self.twms.find_element_by_xpath("//div[contains(@class, '_3Git-')]")
            sleep(0.5)
            send.click()
            sleep(5)
        except:
            self.twms.refresh()
            sleep(10)