import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.google_signin_page import GoogleSignPage
from utils.driver_setup import setup_driver  # Assuming this provides an Appium driver

@pytest.fixture
def driver():
    """Fixture to set up and tear down the Appium driver."""
    driver = setup_driver()  # Initialize Appium driver from utils.driver_setup
    yield driver
    driver.quit()  # Clean up after tests

@pytest.fixture
def google_sign_page(driver):
    """Fixture to initialize the GoogleSignPage."""
    return GoogleSignPage(driver)

def test_tap_continue_with_google(google_sign_page):
    """Test the tap_continew_with_google method."""
    # Act: Attempt to click the 'Continue with Google' button
    result = google_sign_page.tap_continew_with_google()
    
    # Assert: Verify the click was successful
    assert result is True, "Failed to click 'Continue with Google' button"
    
    # Optional: Verify the UI state (e.g., account picker is displayed)
    try:
        WebDriverWait(google_sign_page.driver, 5).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, google_sign_page.CHOOSE_ACCOUNT_XPATH)
            )
        )
        google_sign_page.logger.info("Account picker displayed after clicking 'Continue with Google'.")
    except Exception as e:
        google_sign_page.logger.error("Account picker not displayed: " + str(e))
        assert False, "Account picker not displayed after clicking 'Continue with Google'"

def test_tap_choose_account(google_sign_page):
    """Test the tap_choose_account method."""
    # Precondition: Click 'Continue with Google' to reach the account picker
    assert google_sign_page.tap_continew_with_google(), "Failed to reach account picker"
    
    # Act: Attempt to click the 'Choose account' button
    result = google_sign_page.tap_choose_account()
    
    # Assert: Verify the click was successful
    assert result is True, "Failed to click 'Choose account' button"
    
    # Optional: Verify the next UI state (e.g., email field or next button appears)
    try:
        WebDriverWait(google_sign_page.driver, 5).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, google_sign_page.EMAIL_FIELD_XPATH)
            )
        )
        google_sign_page.logger.info("Email field displayed after choosing account.")
    except Exception as e:
        google_sign_page.logger.error("Email field not displayed: " + str(e))
        assert False, "Email field not displayed after choosing account"