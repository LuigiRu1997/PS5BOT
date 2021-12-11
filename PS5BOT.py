from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains ## MAYBE
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randint, randrange
import time 
import random

AMAZON_URL = 'https://www.amazon.it/Sony-Console-Standard-825GB-Europa/dp/B08LLZ2CWD'
AMAZON_TEST_URL = 'https://www.amazon.it/dp/B07ZZVWB4L/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A2VX19DFO3KCLO&pf_rd_s=merchandised-search-3&pf_rd_r=XK2FD06YC2Y627SAP5B2&pf_rd_t=101&pf_rd_p=255d6c07-a7c1-489d-a852-7c98c2d1ea73&pf_rd_i=14232089031'
WAIT_TIME = 3
PRICE_LIMIT = 700.00

class JahkRShop:
    def __init__(self, username, password):
        """ Initializes Bot with class-wide variables. """
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'\Users\Luigi\Desktop\geckodriver.exe')
    
    ## Sign into site with the product
    def signIn(self):
        """ Sign into site with the product. """
        driver = self.driver ## Navigate to URL
        
        ## Enter Username
        username_elem = driver.find_element_by_xpath("//input[@name='email']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        username_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
        ## Enter Password
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        password_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
    ## Find product under X amount
    def findProduct(self):
        """ Finds the product with global link. """
        driver = self.driver
        driver.get(AMAZON_URL)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
        ## If the product is not available, wait until it is available
        isAvailable = self.isProductAvailable()
        
        if isAvailable == 'Non disponibile.':
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
        elif isAvailable <= PRICE_LIMIT:
            ## Buy Now
            buy_now = driver.find_element_by_name('submit.buy-now')
            buy_now.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.signIn()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            
            ## Place Order
            place_order = driver.find_element_by_name('placeYourOrder1')
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            print(f'***** PLACE ORDER: {place_order}')
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            place_order.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            
        else:
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
            
    def isProductAvailable(self):
        """ Checks if product is available. """
        driver = self.driver
        available = driver.find_element_by_class_name('a-color-price').text
        if available == 'Non disponibile.':
            print(f'***** AVAILABLE: {available}')
            return available
        else:
            available = driver.find_element_by_class_name('a-text-price').text
            print(f'***** PRICE: {available}')
            return float(available[0]) ## $123.22 -> 123.22
    
    def closeBrowser(self):
        """ Closes browser """
        self.driver.close()
        

if __name__ == '__main__':
    shopBot = JahkRShop(username="TYPE_YOUR_EMAIL", password="TYPE_YOUR_PASSWORD")
    shopBot.findProduct()
    shopBot.closeBrowser()
