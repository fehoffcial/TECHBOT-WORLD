from time import sleep
class Agent():
    def __init__(self,twms,Project,Version,Descrition,Licence):
        self.twms = twms
        try:
            notification = twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[id=pane-side]").find_element_by_css_selector("[class=_2Q3SY]").click()
        except:
            self.twms.refresh()
            sleep(10)