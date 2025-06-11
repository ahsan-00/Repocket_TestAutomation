import time
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.actions.pointer_input import PointerInput
# from appium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ExploreandEarn(BasePage):
    # Locators
    TITLE_XPATH = "//android.view.View[@content-desc='Explore and Earn']"
    AVAILABLE_XPATH = "//android.view.View[@content-desc='Available']"
    ACTIVE_XPATH = "//android.view.View[@content-desc='Active']"
    HISTORY_XPATH = "//android.view.View[@content-desc='History']"
    LIST_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View"
    OFFERS_XPATH = "//android.view.View[@content-desc='Share Leftover bandwidth offer $0.10']"
    NO_OFFERS_MESSAGE_XPATH = "//android.view.View[@content-desc='Nothing found']"
    SEARCH_FIELD_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]"
    FILTER_BUTTON_XPATH = "//android.widget.ImageView[@content-desc='Filters']"
    SORT_BUTTON_XPATH = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]"
    ALL_FILTER_BUTTON_XPATH = "//android.view.View[@content-desc='All']"
    COMPLETED_FILTER_BUTTON_XPATH = "//android.view.View[@content-desc='Completed']"
    PENDING_FILTER_BUTTON_XPATH = "//android.view.View[@content-desc='Pending']"


    def validate_earnandexplore(self):
        try:
            sub_update = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.TITLE_XPATH))
            )
            if sub_update.is_displayed():
                self.logger.info("Subscription update element is visible.")
                return True
        except Exception as e:
            self.logger.warning("Subscription update element not visible: " + str(e))
        return False
    
    def click_available(self):
        try:
            available_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.AVAILABLE_XPATH))
            )
            available_button.click()
            self.logger.info("Clicked on Available button.")
        except Exception as e:
            self.logger.error("Available button not clickable: " + str(e))
            raise AssertionError("Available button not clickable: " + str(e))
        
    def click_active(self):
        try:
            active_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.ACTIVE_XPATH))
            )
            active_button.click()
            self.logger.info("Clicked on Active button.")
        except Exception as e:
            self.logger.error("Active button not clickable: " + str(e))
            raise AssertionError("Active button not clickable: " + str(e))
        

    def click_history(self):
        try:
            history_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.HISTORY_XPATH))
            )
            history_button.click()
            self.logger.info("Clicked on History button.")
        except Exception as e:
            self.logger.error("History button not clickable: " + str(e))
            raise AssertionError("History button not clickable: " + str(e))
        
    def validate_list(self):
        try:
            list_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.LIST_XPATH))
            )
            if list_element.is_displayed():
                self.logger.info("List element is visible.")
                return True
        except Exception as e:
            self.logger.warning("List element not visible: " + str(e))
        return False
    
    def validate_offers(self):
        try:
            offers_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, self.OFFERS_XPATH))
            )
            if offers_element.is_displayed():
                self.logger.info("Offers element is visible.")
                return True
        except Exception as e:
            self.logger.warning("Offers element not visible: " + str(e))
        return False
    
    def validate_offers_in_tab(self, tab_name):
        # Navigate to the specified tab
        if tab_name.lower() == "available":
            self.click_available()
        elif tab_name.lower() == "active":
            self.click_active()
        elif tab_name.lower() == "history":
            self.click_history()
        else:
            self.logger.error(f"Invalid tab name: {tab_name}")
            raise ValueError(f"Invalid tab name: {tab_name}")

        try:
            # Check for offers
            offers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.XPATH, self.OFFERS_XPATH))
            )
            if offers:
                self.logger.info(f"Offers found in {tab_name} tab: {len(offers)} offer(s).")
                return True
        except Exception:
            # Check for 'No available offers' message
            try:
                no_offers = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((AppiumBy.XPATH, self.NO_OFFERS_MESSAGE_XPATH))
                )
                if no_offers.is_displayed():
                    self.logger.info(f"No offers available in {tab_name} tab.")
                    return False
            except Exception:
                self.logger.warning(f"Neither offers nor 'No available offers' message found in {tab_name} tab.")
                return False

    def search_offers(self, search_term):
        """
        Search for offers using the search field.
        """
        try:
            search_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.SEARCH_FIELD_XPATH))
            )
            search_field.clear()
            search_field.send_keys(search_term)
            self.logger.info(f"Searched for offers with term: {search_term}")
            time.sleep(2)  # Wait for search results to load
            return True
        except Exception as e:
            self.logger.error(f"Failed to search offers: {str(e)}")
            return False

    def filter_offers(self, filter_option):
        """
        Apply a filter to the offers (e.g., by category or status).
        Placeholder: Update filter_option with actual filter value.
        """
        try:
            filter_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.FILTER_BUTTON_XPATH))
            )
            filter_button.click()
            # Placeholder: Select filter_option (update with actual UI interaction)
            self.logger.info(f"Applied filter: {filter_option}")
            time.sleep(2)  # Wait for filter to apply
            return True
        except Exception as e:
            self.logger.error(f"Failed to apply filter: {str(e)}")
            return False

    def sort_offers(self, sort_option):
        """
        Sort offers (e.g., by price, date).
        Placeholder: Update sort_option with actual sort value.
        """
        try:
            sort_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.SORT_BUTTON_XPATH))
            )
            sort_button.click()
            # Placeholder: Select sort_option (update with actual UI interaction)
            self.logger.info(f"Applied sort: {sort_option}")
            time.sleep(2)  # Wait for sort to apply
            return True
        except Exception as e:
            self.logger.error(f"Failed to sort offers: {str(e)}")
            return False

    def click_offer(self, offer_index=0):
        """
        Click on a specific offer by index to start earning.
        """
        try:
            offers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.XPATH, self.OFFERS_XPATH))
            )
            if offer_index < len(offers):
                offers[offer_index].click()
                self.logger.info(f"Clicked on offer at index {offer_index}.")
                return True
            else:
                self.logger.error(f"Offer index {offer_index} out of range. Found {len(offers)} offers.")
                return False
        except Exception as e:
            self.logger.error(f"Failed to click offer: {str(e)}")
            return False
        
    def filterbyall(self):
        """
        Click on the filter button to apply filters.
        """
        try:
            filter_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.ALL_FILTER_BUTTON_XPATH))
            )
            filter_button.click()
            self.logger.info("Clicked on Filter button.")
        except Exception as e:
            self.logger.error(f"Filter button not clickable: {str(e)}")
            raise AssertionError(f"Filter button not clickable: {str(e)}")
        
    def filterbycompleted(self):
        """
        Click on the filter button to apply filters.
        """
        try:
            filter_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.COMPLETED_FILTER_BUTTON_XPATH))
            )
            filter_button.click()
            self.logger.info("Clicked on Filter button.")
        except Exception as e:
            self.logger.error(f"Filter button not clickable: {str(e)}")
            raise AssertionError(f"Filter button not clickable: {str(e)}")
        
    def filterbypending(self):
        """
        Click on the filter button to apply filters.
        """
        try:
            filter_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.PENDING_FILTER_BUTTON_XPATH))
            )
            filter_button.click()
            self.logger.info("Clicked on Filter button.")
        except Exception as e:
            self.logger.error(f"Filter button not clickable: {str(e)}")
            raise AssertionError(f"Filter button not clickable: {str(e)}")

    
    
