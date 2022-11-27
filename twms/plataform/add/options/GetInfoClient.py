from time import sleep
class GetInfoClient():
    def __init__(self,twms):
        self.twms = twms
        try:
            if True:
                get_number = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("[class=YEe1t]").text
                sleep(0.5)
                print(get_number)
                main = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("[class=_1UuMR]").click()
                sleep(5)
                get_img = self.twms.find_element_by_css_selector("div[class=_1l12d]").find_element_by_css_selector("img").get_attribute("src")
                sleep(0.5)
                print(get_img)
                get_nick = self.twms.find_element_by_css_selector(".i5ly3._299go").find_element_by_css_selector("div[class=_16tJY]").text
                sleep(0.5)
                if get_nick:
                    print(get_nick)
                else:
                    get_nick = "~|~ TWMS PRO ~|~"
                get_name = self.twms.find_element_by_css_selector("[class=_3ZYWe]").text
                sleep(0.5)
                print(get_name)
                get_id = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("div[class=RUGMB]").find_element_by_css_selector("div[class=_26MUt]").find_element_by_css_selector("div[class=tSmQ1]").find_elements_by_css_selector("._1RAno._3ASsl.focusable-list-item")[-1].get_attribute("data-id")  # TRUE | FALSE
                if get_id:
                    sleep(0.5)
                    get_id = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("div[class=RUGMB]").find_element_by_css_selector("div[class=_26MUt]").find_element_by_css_selector("div[class=tSmQ1]").find_elements_by_css_selector("._1RAno._3ASsl.focusable-list-item")[-1].get_attribute("data-id")[5:22]  # TRUE
                    print(get_id[5:22])
                else:
                    get_id = self.twms.find_element_by_css_selector("[id=main]").find_element_by_css_selector("div[class=RUGMB]").find_element_by_css_selector("div[class=_26MUt]").find_element_by_css_selector("div[class=tSmQ1]").find_element_by_css_selector("._1RAno.message-in.focusable-list-item").get_attribute("data-id")[6:23]  # FALSE
                    print(get_id[6:23])
                    sleep(0.5)
                get_hours = self.twms.find_elements_by_css_selector("[class=_16tJY]")[-1].text
                sleep(1.5)
                if get_hours:
                    get_hours = twms.find_elements_by_css_selector("[class=_16tJY]")[-1].text
                else:
                    get_hours = "~|~ TWMS PRO ~|~"
                sleep(0.5)
                with open(f"TWMS-INFO-CLIENT-{get_number}.txt","w") as f:
                    f.write(f"Image: {get_img}\n")
                    f.write(f"ID Number: {get_id} ~|~ DEFAULT [@c.us] ~|~\n")
                    f.write(f"Name: {get_name}\n")
                    f.write(f"Nick: {get_nick}\n")
                    f.write(f"Status: {get_hours}\n")
                    f.write(f"Number: {get_number}\n")
                #print("Success")
                exit = self.twms.find_element_by_css_selector(".i5ly3._299go").find_element_by_css_selector("div[class=_1K7Z6]").find_element_by_css_selector("button[class=hYtwT]").click()
                sleep(1)
            else:
                exit = self.twms.find_element_by_css_selector(".i5ly3._299go").find_element_by_css_selector("div[class=_1K7Z6]").find_element_by_css_selector("button[class=hYtwT]").click()
                print("Exit 1")
        except:
            self.twms.refresh()
            sleep(10)