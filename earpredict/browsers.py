url = 'https://www.royal777.win/lottery-bet/SELF_MONEY_TREE'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time 



browser = webdriver.Firefox() 
browser.get(url) 



def read(amount,predict):
    if(float(amount) < 80.00):
        print(str(amount))
        amoun=str(amount)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[1]/span[1]/span/input').send_keys(amoun)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[1]/span[1]/span/input').clear()
        browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[1]/span[1]/span/input').send_keys(Keys.BACKSPACE)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[1]/span[1]/span/input').send_keys(amoun)
        if(predict == '1'):
            browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]/div/div[3]/input').click()#odd
        else:
            browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[3]/div[2]/div[4]/div/div[3]/input').click()#even
        browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[2]/div[1]/button[1]').click()#submit btn
        time.sleep(0.5)
        try:
            browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
            time.sleep(0.5)
            try:
                browser.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button').click()
            except Exception:
                browser.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button').click()

        except Exception :
            browser.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
            time.sleep(0.5)
            try:
                browser.find_element_by_xpath('/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button').click()
            except Exception:
                browser.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button').click()

        
    else:
        print("amount excced above 15.06")
