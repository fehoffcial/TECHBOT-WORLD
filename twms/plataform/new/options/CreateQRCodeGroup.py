from time import sleep
import pyqrcode
class CreateQRCodeGroup():
    def __init__(self,twms,NameGroup,ResetLink):
        self.twms = twms
        self.NameGroup = NameGroup
        self.ResetLink = ResetLink
        try:
            sleep(0.5)
            main = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_2Evw0]").find_element_by_css_selector("._1awRl.copyable-text.selectable-text").send_keys(self.NameGroup)
            sleep(2)
            mains = self.twms.find_element_by_css_selector("[id=side]").find_elements_by_css_selector("[class=_1MZWu]")[-1].click()  # CONTACT
            sleep(3)
            clean = self.twms.find_element_by_css_selector("[id=side]").find_element_by_css_selector("[class=_1Ra05]").find_element_by_css_selector("[class=_3Eocp]").click()
            sleep(0.1)
            setup = self.twms.find_element_by_css_selector("[class=VPvMz]").find_elements_by_css_selector("[class=_2wfYK]")[-1].click()
            sleep(1)
            data = self.twms.find_element_by_css_selector("[class=_1hhxx]").find_elements_by_css_selector("li")[-5].click()
            sleep(1)
            data_group = self.twms.find_elements_by_css_selector("._32vnm._2k4Ax")[4].find_elements_by_css_selector("._3Pwfx._2XSjg")  # LINK
            x = len(data_group)
            sleep(0.5)
            y = x - 1
            sleep(0.5)
            data_group = self.twms.find_elements_by_css_selector("._32vnm._2k4Ax")[4].find_elements_by_css_selector("._3Pwfx._2XSjg")[-y].click()
            sleep(1)
            data_group_img = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_1l12d]").find_element_by_css_selector("img").get_attribute("src")
            data_group_name = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_1c_mC]").find_element_by_css_selector("span[class=_1VzZY]").text
            data_group_link = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("span[class=_3lSC7]").find_element_by_css_selector("a[id=group-invite-link-anchor]").get_attribute("href")
            if "RESETLINK".lower() in self.ResetLink.lower() or "YES".lower() in self.ResetLink.lower():
                sleep(0.5)
                reset_link = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_1RHZR]").find_elements_by_css_selector("[class=_1OZ02]")[-1].click()
                sleep(0.5)
                resets_links = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("[class=_2SGGH]").find_element_by_css_selector("._30EVj.gMRg5").click()
                sleep(0.5)
                with open("TWMS-GROUP-QRCODE.txt","w") as f:
                    f.write(f"IMAGE: {data_group_img}\n")
                    f.write(f"NAME: {data_group_name}\n")
                    f.write(f"LINK: {data_group_link}")
                sleep(1.5)
                qr_code = pyqrcode.create(data_group_link)
                sleep(1.5)
                qr_code.png('TWMS-GROUP-QRCODE.png', scale=6)
                sleep(1.5)
                exit = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("header[class=_3tpsN]").find_element_by_css_selector("[class=hYtwT]").click()
                sleep(0.5)
                exit = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("header[class=_3tpsN]").find_element_by_css_selector("[class=hYtwT]").click()
                sleep(0.5)
            else:
                with open("TWMS-GROUP-QRCODE.txt", "w") as f:
                    f.write(f"IMAGE: {data_group_img}\n")
                    f.write(f"NAME: {data_group_name}\n")
                    f.write(f"LINK: {data_group_link}")
                sleep(1.5)
                qr_code = pyqrcode.create(data_group_link)
                sleep(1.5)
                qr_code.png('TWMS-GROUP-QRCODE.png', scale=6)
                sleep(1.5)
                exit = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("header[class=_3tpsN]").find_element_by_css_selector("[class=hYtwT]").click()
                sleep(0.5)
                exit = self.twms.find_element_by_css_selector("[class=_1TBWy]").find_element_by_css_selector("header[class=_3tpsN]").find_element_by_css_selector("[class=hYtwT]").click()
                sleep(0.5)
        except:
            self.twms.refresh()
            sleep(10)
