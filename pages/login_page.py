import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    ALLOW_BUTTON_XPATH = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"
    DENY_BUTTON_XPATH = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"
    DETAIL_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Details Estimated task time: 5 seconds']"


    HOME_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 1 of 4']"
    EXPLORE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 2 of 4']"
    REFFER_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 3 of 4']"
    PROFILE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 4 of 4']"

    EMAIL_BUTTON_XPATH = "//android.widget.Button[@content-desc='Continue with email']"
    GOOGLE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Continue with Google']"

    EMAIL_FIELD_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]"
    PASSWORD_FIELD_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]"
    EYE_BUTTON_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]/android.widget.ImageView"
    LOGIN_BUTTON_XPATH = "//android.widget.Button[@content-desc='login']" 
    DASHBOARD_ELEMENT_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[2]"  # Update with real ID
    FORGOT_PASSWORD_XPATH = "//android.view.View[@content-desc='Forget password?   ']"

    def handle_permission_dialog(self):
        try:
            allow_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.ALLOW_BUTTON_XPATH))
            )
            allow_button.click()
            self.logger.info("Permission dialog appeared and 'Allow' button was clicked.")
            time.sleep(1)
            return True
        except Exception as e:
            self.logger.warning("Permission dialog not shown or 'Allow' button not found: " + str(e))
            return False

    def tap_home(self):
        try:
            tap_home_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.HOME_BUTTON_XPATH))
            )   
            tap_home_button.click()
            self.logger.info("Home button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click home button: " + str(e))
            return False

    def tap_earn(self):
        try:
            tap_earn_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EXPLORE_BUTTON_XPATH))
            )
            tap_earn_button.click()
            self.logger.info("Explore & Earn button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Explore & Failed to click earn button: " + str(e))
            return False
        
    def tap_continue_with_email(self):
        try:
            email_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EMAIL_BUTTON_XPATH))
            )
            email_button.click()
            self.logger.info("Continue with Email button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click continue with email button: " + str(e))
            return False
        
    def tap_continew_with_google(self):
        try:
            google_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.GOOGLE_BUTTON_XPATH))
            )
            google_button.click()
            self.logger.info("Continue with Google button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click continue with Google button: " + str(e))
            return False

    def tap_detail(self):
        try:
            detail_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.DETAIL_BUTTON_XPATH))
            )
            detail_button.click()
            self.logger.info("Detail button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click detail button: " + str(e))
            return False
        
    def verify_forgot_password(self):
        try:
            forgot_password = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.FORGOT_PASSWORD_XPATH))
            )
            if forgot_password.is_displayed():
                self.logger.info("Forgot password element is visible.")
                return True
        except Exception as e:
            self.logger.warning("Forgot password element not visible: " + str(e))
        return False

    def enter_email(self, email):
        try:
            email_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EMAIL_FIELD_XPATH))
            )
            email_button.click()
            email_button.send_keys(email)
            self.logger.info("Email field clicked & entered successfully.")
        except Exception as e:
            self.logger.error("Failed to click email: " + str(e))
            return False

    def enter_password(self, password):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.PASSWORD_FIELD_XPATH))
            )
            password_field.click()
            password_field.send_keys(password)
            self.driver.hide_keyboard()
            self.logger.info("Password field clicked & entered successfully.")
        except Exception as e:
            self.logger.error("Failed to click email field: " + str(e))
            return False
        

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

    def tap_login(self):
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.LOGIN_BUTTON_XPATH))
            )
            login_button.click()
            time.sleep(5)  # Wait for login to process
            self.logger.info("Login button clicked successfully.")
        except Exception as e:
            self.logger.error("Failed to click Login button: " + str(e))
            return False
        
    def is_login_successful(self):
        try:
            dashboard_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.DASHBOARD_ELEMENT_XPATH))
            )
            if dashboard_element.is_displayed():
                self.logger.info("Login successful: Dashboard element is found.")
                return True
        except Exception as e:
            self.logger.error("Login failed: Dashboard not found. " + str(e))
        return False