import time
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.actions.pointer_input import PointerInput
# from appium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class NoOfferGuestUser(BasePage):
    # Locators
    SUB_UPDATE_XPATH = "com.android.permissioncontroller:subscription for update"
    EMAIL_FIELD_XPATH = "//android.widget.Button[@content-desc='Email']"
    SUBMIT_BUTTON_XPATH = "//android.widget.Button[@content-desc='Submit']"


    def validate_subscription_update(self):
        try:
            sub_update = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.SUB_UPDATE_XPATH))
            )
            if sub_update.is_displayed():
                self.logger.info("Subscription update element is visible.")
                return True
        except Exception as e:
            self.logger.warning("Subscription update element not visible: " + str(e))
        return False
    def click_subscription_update(self):
        try:
            sub_update = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.SUB_UPDATE_XPATH))
            )
            sub_update.click()
            self.logger.info("Clicked on Subscription Update element.")
        except Exception as e:
            self.logger.error("Subscription Update element not clickable: " + str(e))
            raise AssertionError("Subscription Update element not clickable: " + str(e))

    def click_email_field(self):
        try:
            email_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EMAIL_FIELD_XPATH))
            )
            email_button.click()
            self.logger.info("Clicked on Email button.")
        except Exception as e:
            self.logger.error("Email button not clickable: " + str(e))
            raise AssertionError("Email button not clickable: " + str(e))
        
    def click_submit_button(self):  
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.SUBMIT_BUTTON_XPATH))
            )
            submit_button.click()
            self.logger.info("Clicked on Submit button.")
        except Exception as e:
            self.logger.error("Submit button not clickable: " + str(e))
            raise AssertionError("Submit button not clickable: " + str(e))
        
    def is_subscription_update_visible(self):
        try:
            sub_update = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.SUB_UPDATE_XPATH))
            )
            return sub_update.is_displayed()
        except Exception as e:
            self.logger.warning("Subscription update element not visible: " + str(e))
            return False
    

