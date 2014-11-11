import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import string


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability.json")
#        print (driver.page_source)
############### Login ID and Password##############
        user_apple_id = ""
        user_apple_password = ""
        phone_number = ""
############### Login ID and Password##############

        input_captcha_counter = 0

        running = True
        
        while running:

            if "false" in driver.page_source:

                driver.maximize_window()
                driver.get("https://reserve.cdn-apple.com/HK/zh_HK/reserve/iPhone/availability")
                print (driver.title)
                self.assertIn("Apple", driver.title)
                start_button = driver.find_element_by_xpath('//*[@id="wrapper"]/div[3]/div[2]/div/div[2]/a')
                start_button.click()
                self.assertEqual(self.driver.title, "Apple - 預訂與取貨")

                appleid = self.driver.find_element_by_name("appleId")
                appleid.clear()
                appleid.send_keys(user_apple_id)

                applepassword = self.driver.find_element_by_name("accountPassword")
                applepassword.clear()
                applepassword.send_keys(user_apple_password)

                captcha = self.driver.find_element_by_name("captchaInput")
                captcha.clear()
                captchainput = input("Enter a CAPTCHA: ")
                input("Press<Enter>")
                captcha.clear()
                captcha.send_keys(captchainput)
                    

                login_button = driver.find_element_by_xpath('//*[@id="signInHyperLink"]')
                login_button.click()

###############################################If Captcha Wrong#######################################################################
#                while "輸入你看到或聽到的字元，然後繼續。" in self.driver.page_source:
#                    applepassword_again = self.driver.find_element_by_name("accountPassword")
#                    applepassword_again.clear()                 
#                    applepassword_again.send_keys(user_apple_password)
#                    
#                    captcha_again = self.driver.find_element_by_name("captchaInput")
#                    captcha_again.clear()
#                    captchainput_again = input("Enter CAPTCHA Again: ")
#                    input("Press<Enter>")
#                    captcha_again.send_keys(captchainput_again[input_captcha_counter])
#                    login_button_again = driver.find_element_by_xpath('//*[@id="signInHyperLink"]')
#                    login_button_again.click()
#                    input_captcha_counter += 1
#                    print ("Times retried: " + str(input_captcha_counter))
#                else:
#                    print ("failed")
#
###############################################If Captcha Wrong########################################################################

        #        alert = self.driver.switch_to_alert()
        #        print (alert)
                PageSource = self.driver.page_source
        #        print (PageSource)

                if "Apple" in PageSource:
                       
                    try:
                        phonenumber = WebDriverWait(driver, 10).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="phoneNumber"]'))
                        print ("phone number area has finded")
                        # do smth with the found element
                    except TimeoutException:
                        print ("Phone number area Not Found")

                    phonenumber.send_keys(phone_number)

                    print ("phone number has input")

                    try:
                        reservationcode = WebDriverWait(driver, 10).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="reservationCode"]'))
                        print ("reservation code area has finded")
                        # do smth with the found element
                    except TimeoutException:
                        print ("Reservation Code area Not Found")
##################################### Reservation Code Imput ###########################################
                    reservationcodeinput = input("Enter a RS Code: ")
                    input("Press<Enter>")
                    reservationcode.clear()
                    reservationcode.send_keys(reservationcodeinput)
##################################### Reservation Code Imput ###########################################

                    try:
                        continue_button = WebDriverWait(driver, 10).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="smsPageForm"]/div[4]/a'))
                        print ("continue button has found")
                        # do smth with the found element
                    except TimeoutException:
                        print ("Continue Button Not Found")        

                    continue_button.click()

############################################## Choose phone page ##################################################


                    if "選擇 iPhone 型號。" in self.driver.page_source:
                        print ("選擇 iPhone 型號。")
                        shop_name = WebDriverWait(driver, 20).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="store"]/div/div/div/select'))
                        myselect = Select(shop_name)
                        myselect.select_by_value("R409")
                        print ("Causeway Bay")

                        #iphone6 = WebDriverWait(driver, 30).until(lambda driver: EC.element_to_be_clickable(By.XPATH, '//*[@id="product"]/div/ul/li[1]/label/input'))
                        #iphone6 = WebDriverWait(driver, 30).until(EC.presence_of_element_located(By.XPATH, '//*[@id="product"]/div/ul/li[1]/label/input'))
                        #try :
                            #iphone6 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(By.CSS_SELECTOR, '$("Item1 .item input")[1].click()'))
                            #iphone6 = WebDriverWait(driver, 30).until(lambda driver: EC.element_to_be_clickable(By.CSS_SELECTOR, '$("Item1 .item input")[1].click()'))
                        #except TimeoutException:
                        #    print ("Not clickable button")

                        

                        iphone6 = self.driver.find_element_by_css_selector('#product > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > label:nth-child(1) > div:nth-child(2) > img:nth-child(2)')
                        
                        #ac(driver).move_to_element(iphone6).perform()
                        if iphone6.is_selected():
                            iphone6.click()
                        else:
                            print ("failed to select")
                        

#                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="product"]/div/ul/li[1]/label/input')))
#                        print("'MyRadio' is present")
#                        iphone = self.driver.find_element_by_xpath('//*[@id="product"]/div/ul/li[1]/label/input')
#                        print("About to click 'MyRadio'")
#                        time.sleep(3)
#                        if iphone.is_displayed():
#                            iphone.click()
#                        else:
#                            print ("Button not visible")
#                        iphone6 = WebDriverWait(driver, 10).until(lambda driver: self.driver.find_element_by_css_selector('#product > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > label:nth-child(1) > input:nth-child(1)'))
#                        driver.implicitly_wait(10)
#                        iphone6.click()
                            
#                        iphone = self.driver.find_element_by_xpath('//*[@id="product"]/div/ul/li[1]/label/input')
#                        print (iphone)
#                        iphone.click()
#                        driver.implicitly_wait(20)                        
#                        iphone6 = self.driver.find_element_by_css_selector('#product > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > label:nth-child(1) > input:nth-child(1)')
#                        ac(driver).move_to_element(iphone6).perform()
#                        ipone6.click()
#                        ac(driver).send_keys(Keys.SPACE).perform()
############################################## Choose phone page ##################################################

                        print ("can reach here")
                    else:
                        print ("Jump to wrong page")


                    

                    #
                    
                    quit()
                else:
                    print ("failed")

            else:
                print ("no iphone detected")
                driver.refresh()
                print ("refreshed")

        else:
            print ("The while loop is over.")


        print ("Done")
#    def tearDown(self):
#        self.driver.close()

if __name__ == "__main__":
    unittest.main()
