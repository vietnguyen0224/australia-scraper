'''
Using unittesst to test the program Scraper
'''

import unittest
import scraper

class Test(unittest.TestCase):
    '''Test if the program returns exactly three latest headlines in CNN Australia or returns None'''

    def test_three_headlines(self):
        '''Test if the program returns exactly three latest headlines'''

        headline = scraper.Scraper("https://www.cnn.com/australia", "//h3[@data-analytics='Australia latest_list-xs_article_']")
        headline.scraper()
        self.assertEqual(len(headline.headline_list), 3)

    def test_none(self):
        '''Test if the program returns None when no headline is found'''

        headline = scraper.Scraper("https://www.cnn.com/australia", "//h3[@data-analytics='Australia latest_list-xs_article_']")
        headline.scraper()
        self.assertEqual(headline.print_scraper(), "None")

if __name__ == "__main__":
    unittest.main()
