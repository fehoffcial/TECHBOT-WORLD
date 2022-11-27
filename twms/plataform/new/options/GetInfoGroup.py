from time import sleep
class GetInfoGroup():
    def __init__(self,twms,NameGroup):
        self.twms = twms
        self.NameGroup = NameGroup
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
            sleep(2)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(2)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(1)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            data = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-5].click()
            sleep(1)
            dataimg = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("img[class=_1VzZY]").get_attribute("src")
            sleep(0.5)
            datacreate = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_13BQq]").text
            sleep(0.5)
            dataname = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("._2_g1_._21Cgd").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").text
            sleep(0.5)
            datadics = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_2fh-m]").text
            sleep(0.5)
            datadicsimg = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_1fPA0]").text
            sleep(0.5)
            datamember = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_elements_by_css_selector("._3Pwfx._2XSjg")
            sleep(1)
            for datamembers in datamember:
                datamembes = datamembers.text
                sleep(1)
            with open("TWMS-GROUP-INFO.txt","w") as f:
                f.write(f"IMAGE: {dataimg}\n")
                f.write(f"DATE CREATED: {datacreate}\n")
                f.write(f"NAME GROUP: {dataname}\n")
                f.write(f"DISCRETION GROUP: {datadics}\n")
                f.write(f"MEDIA, LINKS AND DOCUMENTS: ~|~ TWMS PRO ~|~ \n")
                f.write(f"GROUP MEMBERS: \n{datamembes}\n")
            sleep(0.5)
            exit = self.twms.find_element_by_css_selector("[class=hYtwT]").click()
        except:
            self.twms.refresh()


