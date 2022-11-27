from time import sleep
class SearchMessage():
    def __init__(self,twms,SearchMessage):
        self.twms = twms
        self.SearchMessage = SearchMessage
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_22PcK]").find_element_by_css_selector("label[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.SearchMessage)
            sleep(5)
            search = self.twms.find_element_by_css_selector("[id=pane-side]").text
            sleep(0.5)
            with open("TWMS-SEARCH-MESSAGE.txt","w") as f:
                f.write(f"{search}")
            clear = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(0.5)
            clears = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_3Wrfs]").click()
            sleep(0.9)
        except:
            self.twms.refresh()
            sleep(10)