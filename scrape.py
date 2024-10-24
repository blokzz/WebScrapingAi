import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website):
     chrome_driver_path = "./chromedriver.exe"
     options = webdriver.ChromeOptions()
     driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)
     try:
        driver.get(website)
        html = driver.page_source
        return html 
     finally:
         driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()
        