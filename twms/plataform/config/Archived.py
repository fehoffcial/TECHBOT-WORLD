from time import sleep
class Archived():
    def __init__(self,twms):
        self.twms = twms
        try:
            sleep(1)
            setup = self.twms.find_element_by_css_selector("[class=_1eNef]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            enter_archived = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_tag_name("li")[-5].click()
            sleep(1)
            list_archived = self.twms.find_element_by_css_selector("[class=WnX2e]").text
            sleep(1)
            with open("TWMS-ARCHIVED.txt","w") as f:
                f.write(f"{list_archived}")
            exit = self.twms.find_element_by_css_selector("[class=hYtwT]").click()
        except:
            self.twms.refresh()
            sleep(10)