from time import sleep
class HangTags():
    def __init__(self,twms):
        self.twms = twms
        try:
            sleep(1)
            setup = self.twms.find_element_by_css_selector("[class=_1eNef]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            enter_hangtags = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_tag_name("li")[-3].click()
            sleep(1)
            hangtags = twms.find_element_by_css_selector("[class=_1RHZR]")
            with open("TWMS-HANGTAGS.txt", "w") as f:
                f.write(f"{hangtags.text}\n")
            sleep(1)
            exit = self.twms.find_element_by_css_selector("[class=hYtwT]").click()
        except:
            self.twms.refresh()
            sleep(10)