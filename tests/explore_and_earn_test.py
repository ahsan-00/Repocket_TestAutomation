import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.explore_and_earn import ExploreandEarn
from utils.driver_factory import DriverFactory

@pytest.mark.smoke
def explore_page(driver):
    eexplore_page = ExploreandEarn(driver)

def test_validate_explore_and_earn(eexplore_page):
    assert eexplore_page.validate_earnandexplore(), "Explore and Earn title not visible"

def test_offers_in_tabs(explore_page):
    tabs = ["available", "active", "history"]
    for tab in tabs:
        result = explore_page.validate_offers_in_tab(tab)
        explore_page.logger.info(f"Offers in {tab} tab: {'Found' if result else 'Not found or no offers message'}")

def test_search_offers(explore_page):
    explore_page.click_available()
    assert explore_page.search_offers("bandwidth"), "Failed to search offers"
    assert explore_page.validate_offers_in_tab("available"), "No offers found after search"

def test_filter_offers(explore_page):
    explore_page.click_available()
    assert explore_page.filter_offers("category"), "Failed to apply filter"
    assert explore_page.validate_offers_in_tab("available"), "No offers found after filtering"

def test_sort_offers(explore_page):
    explore_page.click_available()
    assert explore_page.sort_offers("price"), "Failed to sort offers"
    assert explore_page.validate_offers_in_tab("available"), "No offers found after sorting"

def test_click_offer(explore_page):
    explore_page.click_available()
    assert explore_page.validate_offers_in_tab("available"), "No offers to click"
    assert explore_page.click_offer(0), "Failed to click offer"