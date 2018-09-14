from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from BeautifulSoup import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#use firefox to get page with javascript generated content
with closing(Firefox()) as driver:
#    driver.get("http://www.att.com/shop/wireless/devices/smartphones.html")
#    button = driver.find_element_by_id('deviceShowAllLink')
    driver.get("http://www.python.org")
    button = driver.find_element_by_id('about')
    button.click()
    # wait for the page to load
#    element = WebDriverWait(driver, 10).until(
#    EC.invisibility_of_element_located((By.ID, "deviceShowAllLink"))
#    )
    element = WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "about"))
    )
    # store it to string variable
    page_source = driver.page_source

soup = BeautifulSoup(page_source)
print soup
#items = soup.findAll('div', {"class": "list-item"})
#print "items count:",len(items)
