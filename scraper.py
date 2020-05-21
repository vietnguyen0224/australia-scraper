'''
Project
Assignment 1: Web scraper
Scrape the latest news from Australia CNN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Scraper:
    '''Class to scrape latest news'''

    def __init__(self, url, headline_class):
        '''create and initialize data fields'''

        self.url = url
        self.headline_class = headline_class
        self.headline_list = []

    def scraper(self):
        '''scrape the headlines'''

        #set up webdriver
        options = webdriver.ChromeOptions()

        path = "C:/Python/project/chromedriver_win32/chromedriver.exe"
        browser = webdriver.Chrome(executable_path=path, options=options)

        browser.get(self.url)

        #specify a timeout period
        timeout = 10
        wait = WebDriverWait(browser, timeout)

        try:
            wait.until(EC.presence_of_element_located((By.XPATH, self.headline_class)))
        except TimeoutException:
            print("Timed out waiting for page to load")
            browser.quit()
            return

        #scrape the latest news
        headlines = browser.find_elements_by_xpath(self.headline_class)
        self.headline_list = []
        for headline in headlines:
            self.headline_list.append(headline.text)

    def print_scraper(self):
        '''print list of headlines'''

        if len(self.headline_list) == 0:
            print("None")
            return None

        print("List of headlines: ")
        for headline in self.headline_list:
            print(headline)
        return self.headline_list

if __name__ == "__main":
    headline = Scraper("https://www.cnn.com/australia", "//h3[@data-analytics='Australia latest_list-xs_article_']")
    headline.scraper()
    headline.print_scraper()