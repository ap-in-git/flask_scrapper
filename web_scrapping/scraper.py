import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_scraped_data(postal_code):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    url = "https://welaunch.io/plugins/wordpress-store-locator/single-category/?location=" + postal_code + "&category=34&radius=25"
    driver.get(url)
    time.sleep(5)
    s1 = BeautifulSoup(driver.page_source, 'lxml')
    a = s1.find_all('div', class_='store_locator_details')
    final_data = []
    for x in a:
        c = {}
        c['name'] = x.a.h3.text
        c['name_url'] = x.find('a')['href']
        location = ''
        location_class = ['store_locator_street', 'store_locator_city', 'store_locator_region', 'store_locator_zip', 'store_locator_country']
        for _ in location_class:
            location += x.find('span',class_=_).text
        c['location'] = location

        final_data.append(c)
    return final_data