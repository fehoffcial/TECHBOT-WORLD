from time import sleep
class Group():
    def __init__(self,twms,Members,Title,SelectImage):
        self.twms = twms
        self.Members = Members
        self.Title = Title
        self.SelectImage = SelectImage
        try:
            sleep(2)
            enter_group = self.twms.find_element_by_css_selector("[class=_1eNef]").find_elements_by_css_selector("[class=_2wfYK]")[-2].click()
            sleep(2)
            enter_groups = self.twms.find_element_by_css_selector("[class=_9u1Pq]").click()
            sleep(2)
            click = self.twms.find_element_by_css_selector("[class=oBUnH]").click()
            sleep(2)
            find_members = self.twms.find_element_by_css_selector("[class=oBUnH]").find_element_by_tag_name("input").send_keys(self.Members)
            sleep(2)
            select_members = self.twms.find_element_by_css_selector("[class=_3Pwfx]").click()
            sleep(2)
            enter_group = self.twms.find_element_by_css_selector("[class=_2YB71]").click()
            sleep(5)
            name_group = self.twms.find_element_by_css_selector("._2HE1Z.ugx-m").find_elements_by_tag_name("div")[-1].send_keys(self.Title)
            sleep(2)
            attach = self.twms.find_element_by_css_selector("input[type='file']")
            sleep(2)
            attach.send_keys(self.SelectImage)
            sleep(5)
            send = self.twms.find_element_by_xpath("//div[contains(@class, '_3Git-')]")
            sleep(2)
            send.click()
            sleep(2)
            enters_group = self.twms.find_element_by_css_selector("[class=_3kOoC]").click()
            sleep(5)
        except:
            self.twms.refresh()