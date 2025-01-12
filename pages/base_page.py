from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click_and_switch_to_new_window(self, locator, timeout=10):
        initial_windows = self.driver.window_handles
        self.find_element(locator).click()

        # Wait for a new window to open
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len(initial_windows)
        )

        # Switch to the new window
        new_window = [w for w in self.driver.window_handles if w not in initial_windows][0]
        self.driver.switch_to.window(new_window)


