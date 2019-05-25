import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as exco
from selenium.webdriver.support.ui import WebDriverWait as Webwait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

C_options = Options()

C_options.add_argument("--disable-extensions")
C_options.add_argument("--disable-gpu")
C_options.add_argument("--headless")


class Shopping(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(options=C_options,
                                      executable_path=r"C:\Users\Abraham\Desktop\tuts_ex\chromedriver.exe")
        cls.driver.get("http://automationpractice.com/index.php")

    def test_navigation(self):
        self.driver.find_element_by_class_name("blockbestsellers").click()
        Webwait(self.driver, 5).until(exco.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Printed Chiffon Dress")))
        self.driver.find_element_by_partial_link_text("Printed Chiffon Dress").click()

        Webwait(self.driver, 10).until(exco.element_to_be_clickable((By.NAME, "Submit")))
        elem = self.driver.find_element_by_id("quantity_wanted")
        elem.clear()
        elem.send_keys("3")
        self.driver.find_element_by_id("color_15").click()
        elem = Select(self.driver.find_element_by_tag_name("select"))
        elem.select_by_value("2")
        self.driver.find_element_by_name("Submit").click()
        Webwait(self.driver, 10).until(exco.element_to_be_clickable((By.LINK_TEXT, "Proceed to checkout")))
        self.driver.find_element_by_link_text("Proceed to checkout").click()

        Webwait(self.driver, 10).until(exco.element_to_be_clickable((By.LINK_TEXT, "Proceed to checkout")))
        self.driver.find_element_by_link_text("Proceed to checkout").click()
        Webwait(self.driver, 10).until(exco.presence_of_element_located((By.ID, "email")))
        self.driver.find_element_by_id("email").send_keys("abrahammakko@gmail.com")
        self.driver.find_element_by_id("passwd").send_keys("tester")
        self.driver.find_element_by_id("SubmitLogin").click()

        # action = ActionChains(driver)
        # action.send_keys(Keys.ARROW_LEFT)
        # action.perform()
        # action.send_keys(Keys.TAB)

        # elem = driver.switch_to.active_element()
        #
        # elem.send_keys("admin")

        # driver.find_element_by_tag_name("body").send_keys("admin")

        # actions.send_keys("admin").perform()
        # actions.send_keys(Keys.TAB).perform()
        # actions.send_keys("admin").perform()
        # actions.send_keys(Keys.ENTER).perform()

        self.driver.get_screenshot_as_file("/Users/Abraham/Pictures/googleshot.png")
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
