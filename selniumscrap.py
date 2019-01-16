from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from operator import itemgetter
import os

urls=["https://www.flipkart.com/smart-a1-brown-watch-smartwatch/p/itmfamyccuxe2rh7?pid=SMWFAHWNJ387MN6K","https://www.flipkart.com/smarty-dual-antenna-wifi-ip-smart-onvif-camera-p2p-mini-wireless-cctv-surveillance-720p-night-vision-security/p/itmffk4gu67vmqs2?pid=HSAFFJWT2WUYHHHX"]
#urls = ["https://www.flipkart.com/sellers?pid=HSAFFJWT2WUYHHHX"]
driver = None

#Function to get data in a div
def get_text(element):
    return element.text

#initialize selenium
def selenium_init():

    # create options
    global driver

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'), chrome_options=options)
    driver.implicitly_wait(30)


#Iterate all the urls
def get_url():
    global driver
    global urls

    for url in reversed(urls):
        print (" Opening the URL")
        driver.get(url)
        process()

#put the pin
def put_pin():
    global driver

    print("putting pin")
    pincode = driver.find_element_by_id("pincodeInputId")
    pincode.send_keys("110092")
    print("Pin put success")
    driver.find_element_by_class_name('_2aK_gu').click()
    print("Click check success now waiting for page to load")
    wait_for_classname('_2jjXhE')

#Function to wait
def wait_for_classname(name):
    global driver

    try:
        myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,name)))
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"


def process():
    global driver
    adhyatm_index = 0;

    put_pin()
    print(" Clicking VIEW MORE SELLERS")
    driver.execute_script("document.getElementsByClassName('_37fzmc')[0].click();")
    print("waiting for page to load")
    wait_for_classname('_3fm_R4')

    page_source = BeautifulSoup(driver.page_source, 'lxml')

    nameDivs = [get_text(div.span) for div in page_source.find_all("div", class_="_3fm_R4")]
    priceDivs = [get_text(div) for div in page_source.find_all("div", class_="_1vC4OE")]
    deliveryDateDivs = [get_text(div) for div in page_source.find_all("div", class_="_29Zp1s")]
    ratingDivs = [get_text(div) for div in page_source.find_all("div", class_="hGSR34")] [1:]

    adhyatm_index = nameDivs.index('ADHYATM')

    if adhyatm_index > 1 :
        nameDivs = itemgetter(0,1,adhyatm_index)(nameDivs)
        priceDivs = itemgetter(0,1,adhyatm_index)(priceDivs)
        deliveryDateDivs = itemgetter(0,1,adhyatm_index)(deliveryDateDivs)
        ratingDivs = itemgetter(0,1,adhyatm_index)(ratingDivs)

    else:
        nameDivs = nameDivs[:2]
        priceDivs = priceDivs[:2]
        deliveryDateDivs = deliveryDateDivs[:2]
        ratingDivs = ratingDivs[:2]

    print (nameDivs)
    print (priceDivs)
    print (deliveryDateDivs)
    print (ratingDivs)

    #soup_level1("div",string = "ADHYATM")
    # end the Selenium browser session


selenium_init()
get_url()
driver.quit() 




















































