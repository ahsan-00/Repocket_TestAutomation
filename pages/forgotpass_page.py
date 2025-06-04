import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ForgotPassPage(BasePage):
    # Locators
    HOME_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 1 of 4']"
    EXPLORE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 2 of 4']"
    REFFER_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 3 of 4']"
    PROFILE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 4 of 4']"

    EMAIL_BUTTON_XPATH = "//android.widget.Button[@content-desc='Continue with email']"
    GOOGLE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Continue with Google']"
    FORGOTPASS_LINK_XPATH = "//android.view.View[@content-desc='Forget password?   ']"
    BACK_BUTTON_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button"
    EMAIL_FIELD_XPATH = "//android.widget.EditText"
    EYE_BUTTON_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]/android.widget.ImageView"
    RESET_PASS_BUTTON_XPATH = "//android.widget.Button[@content-desc='Reset password']"

    def tap_forgotpass_link(self):
        try:
            forgotpass_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.FORGOTPASS_LINK_XPATH))
            )
            assert forgotpass_link.is_displayed(), "Forgot Password link is not displayed."
            self.logger.info("Forgot Password link is displayed.")
            forgotpass_link.click()
            self.logger.info("Forgot Password link clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click Forgot Password link: " + str(e))
            return False
        
    def enter_email(self, email):
        try:
            email_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EMAIL_FIELD_XPATH))
            )
            assert email_field.is_displayed(), "Email field is not displayed."
            self.logger.info("Email field is displayed.")
            email_field.click()
            email_field.clear()
            email_field.send_keys(email)
            self.logger.info("Email entered successfully.")
        except Exception as e:
            self.logger.error("Failed to enter email: " + str(e))
            raise AssertionError("Failed to enter email: " + str(e))
    
    def tap_recover_button(self):
        try:
            send_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.RESET_PASS_BUTTON_XPATH))
            )
            assert send_button.is_displayed(), "Send button is not displayed."
            self.logger.info("Send button is displayed.")
            send_button.click()
            self.logger.info("Send button clicked successfully.")
        except Exception as e:
            self.logger.error("Failed to click Send button: " + str(e))
            raise AssertionError("Failed to click Send button: " + str(e))
    
    def tap_back_button(self):
        try:
            back_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.BACK_BUTTON_XPATH))
            )
            assert back_button.is_displayed(), "Back button is not displayed."
            self.logger.info("Back button is displayed.")
            back_button.click()
            self.logger.info("Back button clicked successfully.")
        except Exception as e:
            self.logger.error("Failed to click Back button: " + str(e))
            raise AssertionError("Failed to click Back button: " + str(e))