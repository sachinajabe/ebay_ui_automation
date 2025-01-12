import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddToCart(BasePage):
    search_input_xpath = (By.XPATH,'//input[@id="gh-ac"]')
    search_button_xpath = (By.XPATH,'//input[@id="gh-btn"]')
    first_book_xpath = (By.XPATH,'(//div[@class="s-item__title"]//parent::a[contains(@href,"skw=book")])[1]')
    add_to_cart_button_xpath = (By.XPATH, '//a[@id="atcBtn_btn_1"]')
    item_in_cart_xpath= (By.XPATH,'//i[@id="gh-cart-n"]')

    def add_to_cart(self):
        self.input_text(self.search_input_xpath, "book")
        self.click(self.search_button_xpath)
        self.click_and_switch_to_new_window(self.first_book_xpath)
        time.sleep(30)
        self.click(self.add_to_cart_button_xpath)
        element = self.find_element(self.item_in_cart_xpath)

        return element.text

