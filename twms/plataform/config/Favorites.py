from time import sleep
class Favorites():
    def __init__(self,twms):
        self.twms = twms
        try:
            sleep(1)
            setup = self.twms.find_element_by_css_selector("[class=_1eNef]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            enter_archived = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_tag_name("li")[-4].click()
            sleep(1)
            list = self.twms.find_element_by_css_selector("[class=_1RHZR]").text
            sleep(1)
            with open("TWMS-FAVORITES.txt","w") as f:
                f.write(list)
            sleep(1)
            exit = self.twms.find_element_by_css_selector("[class=hYtwT]").click()
        except:
            self.twms.refresh()
            sleep(10)