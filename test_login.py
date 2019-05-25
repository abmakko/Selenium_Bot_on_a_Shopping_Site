import unittest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

import pathlib
import sys
import os

sys.path.append(os.path.dirname(__file__))

from product_page import ProductPage
from checkout import CheckOut
from homepage import HomePage

from pyunitreport import HTMLTestRunner

HtmlReport_export_path = pathlib.Path(__file__).parent

# headless chrome option
# C_options = Options()
#
# C_options.add_argument("--disable-extensions")
# C_options.add_argument("--disable-gpu")
# C_options.add_argument("--headless")


class Shopping(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(  # options=C_options,
                                      executable_path=r"C:\Users\Abraham\Desktop\tuts_ex\chromedriver.exe")
        cls.driver.get("http://automationpractice.com/index.php")

    def test_navigation(self):
        driver = self.driver  # shortcut

        homepage_navigation = HomePage(driver)

        homepage_navigation.click_tab()
        homepage_navigation.wait()
        homepage_navigation.click_product()

        productpage_navigation = ProductPage(driver)

        productpage_navigation.wait()
        productpage_navigation.enter_quantity()
        productpage_navigation.pick_color()
        productpage_navigation.select_size()
        productpage_navigation.click_submit()
        productpage_navigation.wait_2()
        productpage_navigation.click_checkout()

        checkout_page = CheckOut(driver)

        checkout_page.wait()
        checkout_page.click_checkout()
        checkout_page.wait_2()
        checkout_page.enter_email()
        checkout_page.enter_passwd()
        checkout_page.click_submit()

        self.driver.get_screenshot_as_file("/Users/Abraham/Pictures/googleshot.png")
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


# setting the working directory export path as a string
Export_path = str(HtmlReport_export_path)

# formatting the working directory link
Export_path = Export_path.replace("\\", "/")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output=Export_path))
