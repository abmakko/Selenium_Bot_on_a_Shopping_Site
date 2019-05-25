from selenium.webdriver.support import expected_conditions as ex_co
from selenium.webdriver.support.ui import WebDriverWait as WebWait
from selenium.webdriver.common.by import By
from locators import Locators


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.tab_button_name = Locators.tab_button_name  # click()
        self.product_link_text = Locators.product_link_text  # click()

    def click_tab(self):
        self.driver.find_element_by_class_name(self.tab_button_name).click()

    def wait(self):
        WebWait(self.driver, 5).until(ex_co.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.product_link_text)))

    def click_product(self):
        self.driver.find_element_by_partial_link_text(self.product_link_text).click()


