import _lib.HtmlXmlTestRunner_pkg.HtmlXmlTestRunner as HtmlXmlTestRunner
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from _lib._lib import *
import unittest
import pages
import time
import os

class SmokeTests(unittest.TestCase):
    # Execute BEFORE each Test
    def setUp(self):
        # Write test name into the Textbox file
        test_name = '.'.join(self._testMethodName.split('.')[-2:])
        f = open(os.path.join(os.getcwd(), 'tools', 'textbox', 'textbox.txt'), 'wb')
        f.write(test_name)
        f.close()

        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options)
        

    def tearDown(self):
        self.driver.quit()

    def test_001_SumUp_Login(self):
        Reporting.TestLog("Create all pages and navigate")
        main_page = pages.MainPage(self.driver, 'https://me.sumup.com/en-gb/login')
        dashboard_page = pages.DashboardPage(self.driver)

        main_page.login("qa_task@qa.com", "qataskqatask")
        label_text = dashboard_page.get_label_text()
        assert "find anything that matches your search." in label_text

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

    #Use it to add manually test cases - handy when debugging a specific part of the set
    #suite = unittest.TestSuite() -
    #suite.addTest(SmokeTests('test_100_Start_Browser'))
    #suite.addTest(SmokeTests('FREE_SLOT_FOR_THE_NEXT_TEST'))

    outfile = open("Report.html", "w")
    runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Testing Amazon Cart")
    runner.run(suite)
    outfile.close()