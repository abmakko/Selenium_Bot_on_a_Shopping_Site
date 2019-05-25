from selenium.webdriver.support.ui import WebDriverWait as WebWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_co
from locators import Locators


class CheckOut(object):

    def __init__(self, driver):
        self.driver = driver
        self.checkout_link_text = Locators.checkout_link_text
        self.email_id = Locators.email_id
        self.email = Locators.email
        self.passwd = Locators.passwd
        self.passwd_id = Locators.passwd_id
        self.submit_id = Locators.submit_id

    def wait(self):
        WebWait(self.driver, 10).until(ex_co.element_to_be_clickable((By.LINK_TEXT, self.checkout_link_text)))

    def click_checkout(self):
        self.driver.find_element_by_link_text(self.checkout_link_text).click()

    def wait_2(self):
        WebWait(self.driver, 10).until(ex_co.presence_of_element_located((By.ID, self.email_id)))

    def enter_email(self):
        self.driver.find_element_by_id(self.email_id).send_keys(self.email)

    def enter_passwd(self):
        self.driver.find_element_by_id(self.passwd_id).send_keys(self.passwd)

    def click_submit(self):
        self.driver.find_element_by_id(self.submit_id).click()
