



import unittest
from selenium import webdriver



class GaryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        
    def test_title(self):
        #Open up the webpage
        self.driver.get('https://www.garyvaynerchuk.com/')
        #Check to make sure the title is correct
        self.assertEqual(self.driver.title, 'GaryVaynerchuk.com')

    def test_menu(self):
        self.driver.get('https://www.garyvaynerchuk.com/')
        #Find 'Books' on the menu bar
        book_button = self.driver.find_element_by_css_selector('#menu-item-53 > a:nth-child(1)')
        #Click books
        book_button.click()
        #Make sure we are on correct page by using the title 
        self.assertEqual(self.driver.title, 'Books')

    def test_search_bar(self):
        self.driver.get('https://www.garyvaynerchuk.com/')
        #Find Ask Gary on the menu bar
        ask_button = self.driver.find_element_by_css_selector('#menu-item-6592 > a:nth-child(1)')
        ask_button.click()
        #Find the search bar
        search_bar = self.driver.find_element_by_css_selector('#s')
        #Enter "Instagram into the search bar
        search_bar.send_keys("Instagram")
        
    


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
    
