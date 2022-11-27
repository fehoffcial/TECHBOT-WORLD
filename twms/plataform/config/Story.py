from time import sleep
class Story():
    def __init__(self,twms):
        self.twms = twms
        try:
            enter_story = self.twms.find_element_by_css_selector("[class=_1eNef]").find_elements_by_css_selector("[class=_2wfYK]")[-3].click()
            sleep(5)
            list_story = self.twms.find_element_by_css_selector("[class=_2PndI]").text
            with open("TWMS-STORY.txt", "w") as f:
                f.write(f"{list_story}")
            exit_story = self.twms.find_element_by_css_selector("[class=_1j-Xk]").click()
        except:
            self.twms.refresh()
            sleep(10)