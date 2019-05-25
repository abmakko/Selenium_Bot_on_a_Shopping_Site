from selenium.webdriver.support.ui import WebDriverWait as WebWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_co
from selenium.webdriver.support.ui import Select
from locators import Locators


class ProductPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.submit_button = Locators.submit_button
        self.quantity_button = Locators.quantity_button
        self.color_type = Locators.color_type
        self.no_of_quantity = Locators.no_of_quantity
        self.size_option = Locators.size_option
        self.checkout_link_text = Locators.checkout_link_text
        self.size_option_tag = Locators.size_option_tag

    def wait(self):
        WebWait(self.driver, 5).until(ex_co.element_to_be_clickable((By.NAME, self.submit_button)))

    def enter_quantity(self):
        elem = self.driver.find_element_by_id(self.quantity_button)
        elem.clear()
        elem.send_keys(self.no_of_quantity)

    def pick_color(self):
        self.driver.find_element_by_id(self.color_type).click()

    def select_size(self):
        elem = Select(self.driver.find_element_by_tag_name(self.size_option_tag))
        elem.select_by_value(self.size_option)

    def click_submit(self):
        self.driver.find_element_by_name(self.submit_button).click()

    def wait_2(self):
        WebWait(self.driver, 10).until(ex_co.element_to_be_clickable((By.LINK_TEXT, self.checkout_link_text)))

    def click_checkout(self):
        self.driver.find_element_by_link_text(self.checkout_link_text).click()

