from bs4 import BeautifulSoup as soup
import requests as rq
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.welcometothejungle.co/companies?q=&hPP=30&idx=cms_companies_production&p=0&dFR%5Buniverses.name%5D%5B0%5D=Web%20%26%20Tech'

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get(url)
myDynamicElement = driver.find_element_by_id("search-hits")

# Parser
soup = soup(driver.page_source, "html.parser")
containers = soup.findAll("div", {"class":"ais-hits--item"})


def scrapt_first_page(containers):
    f = open("first_page_wttj2.csv", 'w')
    headers = "Company_name, Numer of Jobs, Sector, url\n"
    f.write(headers)
    for container in containers :
        company_name = container.h4.text.split('\n')[1][12:]
        number_of_job = container.h4.text.split('\n')[3].split(" ")[0]
        sector = container.p.span.text
        url = "https://www.welcometothejungle.co" + container.a["href"]
        f.write(company_name + "," + number_of_job + "," + sector + "," + url + "\n")
    f.close()
scrapt_first_page(containers)

