import time
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.actions.pointer_input import PointerInput
# from appium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class GuestUser(BasePage):
    # Locators
    SLIDUP_XPATH = "//android.view.View[@content-desc='Slide up for more']"
    DETAIL_BUTTON_XPATH = "com.android.permissioncontroller:id/detail_button"

    HOME_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 1 of 4']"
    EXPLORE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 2 of 4']"
    REFFER_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 3 of 4']"
    PROFILE_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Tab 4 of 4']"

    def validate_slideup(self):
        try:
            slideup = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.SLIDUP_XPATH))
            )
            if slideup.is_displayed():
                self.logger.info("Slide up element is visible.")
                return True
        except Exception as e:
            self.logger.warning("Slide up element not visible: " + str(e))
        return False

    def swipe_up_to_explore_tasks(self, times=2):
        """
        Performs multiple swipe-up gestures from the middle of the screen.
        
        :param times: Number of times to swipe up.
        """
        try:
            # Get screen dimensions
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]

            # Coordinates for swipe
            start_x = width // 2
            start_y = height * 3 // 4
            end_y = height // 4

            for i in range(times):
                self.logger.info(f"Swipe {i+1} of {times}")

                # Setup touch input
                finger = PointerInput("touch", "finger")
                actions = ActionBuilder(self.driver, mouse=finger)

                # Perform swipe
                actions.pointer_action.move_to_location(start_x, start_y)
                actions.pointer_action.pointer_down()
                actions.pointer_action.pause(0.2)
                actions.pointer_action.move_to_location(start_x, end_y)
                actions.pointer_action.pointer_up()
                actions.perform()

                time.sleep(1)  # Wait a bit between swipes (optional)

            self.logger.info(f"Successfully performed {times} swipe-up gesture(s).")
            return True

        except Exception as e:
            self.logger.warning(f"Failed to perform swipe-up gesture(s): {str(e)}")
            self.driver.get_screenshot_as_file("screenshots/swipe_up_failure.png")
            return False
        
    def validate_details(self):
        try:
            detail_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.DETAIL_BUTTON_XPATH))
            )
            if detail_button.is_displayed():
                self.logger.info("Detail button is visible.")
                return True
        except Exception as e:
            self.logger.warning("Detail button not visible: " + str(e))
        return False
    
    def tap_detail_button(self):
        try:
            detail_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.DETAIL_BUTTON_XPATH))
            )
            detail_button.click()
            self.logger.info("Detail button clicked successfully.")
            return True
        except Exception as e:
            self.logger.error("Failed to click detail button: " + str(e))
            raise AssertionError("Detail button not clickable: " + str(e))
    




