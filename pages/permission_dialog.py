import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class PermissionPage(BasePage):
    # Locators
    REPOCKET_HOME_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[1]"
    MAINNOTIFICATION_ICON_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[2]"
    NOTIFICATION_CARD_XPATH = "//android.widget.LinearLayout[@resource-id='com.android.permissioncontroller:id/grant_dialog']"
    ACTIVE_TASKS_XPATH = "//android.view.View[contains(@content-desc, 'active tasks')]"
    NOTIFICATION_ICON_XPATH = "//android.widget.ImageView[@resource-id='com.android.permissioncontroller:id/permission_icon']"
    NOTIFICATIONTEXT_XPATH = "//android.widget.TextView[@resource-id='com.android.permissioncontroller:id/permission_message']"
    ALLOW_BUTTON_XPATH = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"
    DENY_BUTTON_XPATH = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']"

    SLIDEUP_TEXT_XPATH = "//android.view.View[@content-desc='Slide up for more']"
    DETAIL_BUTTON_ID = "com.android.permissioncontroller:id/detail_button"

    HOME_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 1 of 4']"
    EXPLORE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 2 of 4']"
    REFFER_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 3 of 4']"
    PROFILE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 4 of 4']"


    def validate_permission_dialog(self):
        try:
            notification_card = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.NOTIFICATION_CARD_XPATH))
            )
            notification_card.is_displayed()
            self.logger.info("Permission dialog is visible.")
            return True
        except Exception as e:
            self.logger.warning("Permission dialog not visible: " + str(e))
            return False

    def validate_notification_icon(self):
        try:
            notification_icon = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.NOTIFICATION_ICON_XPATH))
            )
            notification_icon.is_displayed()
            self.logger.info("Notification icon is visible.")
            return True
        except Exception as e:
            self.logger.warning("Notification icon not visible: " + str(e))
            return False
    
    def validate_notification_text(self):
        try:
            notification_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.NOTIFICATIONTEXT_XPATH))
            )
            notification_text.is_displayed()
            self.logger.info("Notification text is visible.")
            return True
        except Exception as e:
            self.logger.warning("Notification text not visible: " + str(e))
            return False
    

    def allow_permission_dialog(self):
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
        
    def deny_permission_dialog(self):
        try:
            deny_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.DENY_BUTTON_XPATH))
            )
            deny_button.click()
            self.logger.info("Permission dialog appeared and 'Deny' button was clicked.")
            time.sleep(1)
            return True
        except Exception as e:
            self.logger.warning("Permission dialog not shown or 'Deny' button not found: " + str(e))
            return False

    def validate_rePocket_home(self):
        try:
            rePocket_home = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.REPOCKET_HOME_XPATH))
            )
            rePocket_home.is_displayed()
            self.logger.info("rePocket home is visible.")
            return True
        except Exception as e:
            self.logger.warning("rePocket home not visible: " + str(e))
            return False
        
    def validate_main_notification_icon(self):
        try:
            main_notification_icon = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.MAINNOTIFICATION_ICON_XPATH))
            )
            main_notification_icon.is_displayed()
            self.logger.info("Main notification icon is visible.")
            return True
        except Exception as e:
            self.logger.warning("Main notification icon not visible: " + str(e))
            return False
    
    def validate_active_task(self):
        try:
            active_task = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.ACTIVE_TASKS_XPATH))
            )
            active_task.is_displayed()
            self.logger.info("Active task is visible.")
            return True
        except Exception as e:
            self.logger.warning("Active task not visible: " + str(e))
            return False

    def verify_navigation_after_allow(self):
        try:
            home_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.HOME_BUTTON_XPATH))
            )
            assert home_button.is_displayed(), "Home tab not displayed after allowing permission."
            self.logger.info("Navigated to Home tab after allowing permission.")
            return True
        except Exception as e:
            self.logger.warning(f"Failed to navigate to Home tab: {str(e)}")
            return False

