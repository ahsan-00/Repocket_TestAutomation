#google_signin_page.py
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class GoogleSignPage(BasePage):
    # Locators
    ALLOW_BUTTON_XPATH = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"
    DENY_BUTTON_XPATH = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"
    DETAIL_BUTTON_ID = "com.android.permissioncontroller:id/detail_button"


    HOME_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 1 of 4']"
    EXPLORE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 2 of 4']"
    REFFER_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 3 of 4']"
    PROFILE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 4 of 4']"

    EMAIL_BUTTON_XPATH = "//android.widget.Button[@content-desc='Continue with email']"
    GOOGLE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Continue with Google']"
    CHOOSE_ACCOUNT_XPATH = "//android.widget.LinearLayout[@resource-id='com.google.android.gms:id/account_picker_container']"

    ADD_ACCOUNT_BUTTON_XPATH = "(//android.widget.LinearLayout[@resource-id='com.google.android.gms:id/container'])[2]"
    EMAIL_FIELD_XPATH = "//android.widget.EditText[@resource-id='identifierId']"
    CHOOSE_ACCOUNT_XPATH = "//android.widget.LinearLayout[@resource-id='com.google.android.gms:id/account_picker_container']"
    NEXT_BUTTON_XPATH = "//android.widget.Button[@text='NEXT']"


        
    def tap_choose_account(self):
        try:
            choose_account = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.CHOOSE_ACCOUNT_XPATH))
            )
            choose_account.click()
            time.sleep(3)  # Wait for the account picker to load
            self.logger.info("Choose account button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click choose account button: " + str(e))
            return False


    