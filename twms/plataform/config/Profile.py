from time import sleep
class Profile():
    def __init__(self,twms):
        self.twms = twms
        try:
            sleep(1)
            setup = self.twms.find_element_by_css_selector("[class=_1eNef]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            enter_profile = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_tag_name("li")[-6].click()
            sleep(1)
            find_image = self.twms.find_element_by_css_selector("[class=_1VzZY]").get_attribute("src")
            sleep(1)
            finds_names = self.twms.find_element_by_css_selector("._32vnm._2k4Ax._2zqsv").find_element_by_tag_name("span").text
            sleep(1)
            find_name = self.twms.find_element_by_css_selector("._32Tkw._3OSUF").text
            sleep(1)
            find_dics = self.twms.find_element_by_css_selector("[class=_2Phw8]").text
            sleep(1)
            find_scraps = self.twms.find_elements_by_css_selector("span[class=_1fPA0]")[-1].text
            sleep(1)
            finds_scraps = self.twms.find_elements_by_css_selector("._32Tkw._3OSUF")[-1].text
            sleep(2)
            exit = self.twms.find_element_by_css_selector("[class=hYtwT]").click()
            with open("TWMS-PROFILE.txt","w") as f:
                f.write(f"Image: {find_image}\n")
                f.write(f"{finds_names}: {find_name}\n")
                f.write(f"Discretion: {find_dics} \n")
                f.write(f"{find_scraps}: {finds_scraps} \n")
        except:
            self.twms.refresh()
            sleep(10)