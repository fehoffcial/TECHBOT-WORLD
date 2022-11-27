from time import sleep
class SilenceNotificationGroup:
    def __init__(self,twms,NameGroup,Time):
        self.twms = twms
        self.NameGroup = NameGroup
        self.Time = Time
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
            sleep(1.5)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(1)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(0.5)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            notification = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-3].click()
            sleep(1)
            notifications = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_elements_by_css_selector("label[class=_3ZCHZ]")
            sleep(0.5)
            if notifications[-1].text[:].lower() in self.Time.lower():  # SEMPRE
                notifications_sempre = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_elements_by_css_selector("label[class=_3ZCHZ]")[-1].click()
                click = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_element_by_css_selector("[class=_2SGGH]").find_element_by_css_selector("._30EVj.gMRg5").click()
            if notifications[-2].text[2:].lower() in self.Time.lower():  # SEMANAS
                notifications_semana = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_elements_by_css_selector("label[class=_3ZCHZ]")[-2].click()
                click = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_element_by_css_selector("[class=_2SGGH]").find_element_by_css_selector("._30EVj.gMRg5").click()
            if notifications[-3].text[2:].lower() in self.Time.lower(): # HORAS
                notifications_horas = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_elements_by_css_selector("label[class=_3ZCHZ]")[-3].click()
                click = self.twms.find_element_by_css_selector("[class=_1HX2v]").find_element_by_css_selector("[class=_2SGGH]").find_element_by_css_selector("._30EVj.gMRg5").click()
        except:
            self.twms.refresh()
            sleep(10)