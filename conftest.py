import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    # options.add_argument("--headless")  # Optional: Run in headless mode
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
