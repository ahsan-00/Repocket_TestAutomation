from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger  # Import the logger utility


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # Default wait time in seconds
        self.logger = get_logger(self.__class__.__name__)  # ✅ Centralized logger

    def click(self, by, locator):
        """Click an element identified by the given locator."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            raise AssertionError(f"Element not clickable: {locator}")

    def type(self, by, locator, text):
        """Type text into an element identified by the given locator."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Typed into element: {locator} -> {text}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found or not visible: {locator}")
            raise AssertionError(f"Element not found or not visible: {locator}")

    def is_element_present(self, by, locator):
        """Check if an element is present and visible."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            self.logger.info(f"Element present: {locator}")
            return True
        except TimeoutException:
            self.logger.warning(f"Element not found: {locator}")
            return False
