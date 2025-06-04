import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SignUpPage(BasePage):
    # Locators
    HOME_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 1 of 4']"
    EXPLORE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 2 of 4']"
    REFFER_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 3 of 4']"
    PROFILE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 4 of 4']"

    EMAIL_BUTTON_XPATH = "//android.widget.Button[@content-desc='Continue with email']"
    GOOGLE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Continue with Google']"
    SIGNUP_LINK_XPATH = "//android.widget.Button[@content-desc='Don’t have an account?   Sign Up']"
    BACK_BUTTON_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button"
    NAME_FIELD_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]"
    EMAIL_FIELD_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]"
    PASSWORD_FIELD_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]"
    CONFIRM_PASSWORD_FIELD_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[4]"
    EYE_BUTTON_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]/android.widget.ImageView"

    CHECKBOX_XPATH = "//android.widget.CheckBox"
    SIGNUP_BUTTON_XPATH = "//android.widget.Button[@content-desc='Sign Up']"

    LOGIN_BUTTON_XPATH = "//android.widget.Button[@content-desc='login']"

    def tap_signup_link(self):
        try:
            signup_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.SIGNUP_LINK_XPATH))
            )
            assert signup_link.is_displayed(), "Sign Up link is not displayed."
            self.logger.info("Sign Up link is displayed.")
            signup_link.click()
            self.logger.info("Sign Up link clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click Sign Up link: " + str(e))
            return False
        
    
    def enter_name(self, sname):
        try:
            name_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.NAME_FIELD_XPATH))
            )
            assert name_field.is_displayed(), "Name field is not displayed."
            self.logger.info("Name field is displayed.")
            name_field.click()
            name_field.clear()
            name_field.send_keys(sname)
            self.logger.info("Name entered successfully.")
        except Exception as e:
            self.logger.error("Failed to enter name: " + str(e))
            raise AssertionError("Failed to enter name: " + str(e))
    
    def enter_email(self, semail):
        try:
            email_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EMAIL_FIELD_XPATH))
            )
            assert email_field.is_displayed(), "Email field is not displayed."
            self.logger.info("Email field is displayed.")
            email_field.click()
            email_field.clear()
            email_field.send_keys(semail)
            self.logger.info("Email entered successfully.")
        except Exception as e:
            self.logger.error("Failed to enter email: " + str(e))
            raise AssertionError("Failed to enter email: " + str(e))
    
    def enter_password(self, spassword):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.PASSWORD_FIELD_XPATH))
            )
            assert password_field.is_displayed(), "Password field is not displayed."
            self.logger.info("Password field is displayed.")
            password_field.click()
            password_field.clear()
            password_field.send_keys(spassword)
            self.logger.info("Password entered successfully.")
        except Exception as e:
            self.logger.error("Failed to enter password: " + str(e))
            raise AssertionError("Failed to enter password: " + str(e))
    
    def enter_confirm_password(self, scpassword):
        try:
            confirm_password_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.CONFIRM_PASSWORD_FIELD_XPATH))
            )
            assert confirm_password_field.is_displayed(), "Confirm Password field is not displayed."
            self.logger.info("Confirm Password field is displayed.")
            confirm_password_field.click()
            confirm_password_field.clear()
            confirm_password_field.send_keys(scpassword)
            self.logger.info("Confirm password entered successfully.")
        except Exception as e:
            self.logger.error("Failed to enter confirm password: " + str(e))
            raise AssertionError("Failed to enter confirm password: " + str(e))
    
    def tap_eye_button(self):
        try:
            eye_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EYE_BUTTON_XPATH))
            )
            eye_button.click()
            self.logger.info("Eye button clicked successfully.")
        except Exception as e:
            self.logger.error("Failed to click eye button: " + str(e))
            return False
    
    def tap_checkbox(self):
        try:
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.CHECKBOX_XPATH))
            )
            checkbox.click()
            self.logger.info("Checkbox clicked successfully.")
        except Exception as e:
            self.logger.error("Failed to click checkbox: " + str(e))
            return False
        
    def tap_signup_button(self):
        try:
            signup_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.SIGNUP_BUTTON_XPATH))
            )
            assert signup_button.is_enabled(), "Sign Up button is not enabled."
            self.logger.info("Sign Up button is enabled.")
            signup_button.click()
            self.logger.info("Sign Up button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click Sign Up button: " + str(e))
            return False
        
    def is_error_message_displayed(self):
        error_xpaths = [
            "//android.view.View[normalize-space(@content-desc)='Password is required!']",
            "//android.view.View[normalize-space(@content-desc)='Email is required!']",
            "//android.view.View[normalize-space(@content-desc)='Name is required!']",
            "//android.view.View[normalize-space(@content-desc)='Confirm Password is required!']",
        ]
        
        for xpath in error_xpaths:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
                )
                if element.is_displayed():
                    self.logger.info(f"Error message displayed: {element.get_attribute('content-desc')}")
                    return True
            except Exception:
                continue  # Try next error message

        self.logger.warning("No expected error messages were displayed.")
        return False

        
    def tap_back_button(self):
        try:
            back_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.BACK_BUTTON_XPATH))
            )
            back_button.click()
            self.logger.info("Back button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click Back button: " + str(e))
            return False
