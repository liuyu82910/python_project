import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
        self.driver.get("http://www.python.org")

    def test_example(self): # must start with test
        print("This is a test.")
        assert True

    def another_test(self): # this func won't work because it does not start with test
        print("This is going to fail.")

    def test_a_example(self):
        print("Is this going to print?")
        assert False

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()