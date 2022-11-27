from time import sleep
class Message():
    def __init__(self,twms,SendMessage,TrainingPhrases):
        self.twms = twms
        self.SendMessage = SendMessage
        self.TrainingPhrases = TrainingPhrases
        try:
            check = twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("[class=tSmQ1]").find_elements_by_css_selector("[data-id*=false]")[-1].text.lower()
            if self.TrainingPhrases.lower() in check:
                send = twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(sel)
                send_msg = twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("footer[class=_2ig1U]").find_element_by_css_selector("[class=_3qpzV]").click()
                sleep(0.5)

        except:
            self.twms.refresh()
            sleep(10)