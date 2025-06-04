# tests/guest_with_no_offers.py

import pytest
from pages.permission_dialog import PermissionPage
from pages.guest_with_no_offrs import NoOfferGuestUser
from pages.login_page import LoginPage
from pages.base_page import BasePage

@pytest.mark.smoke
def test_valid_login(driver):
    permission_page = PermissionPage(driver)
    guest_user_page = NoOfferGuestUser(driver)

    PermissionPage.allow_permission_dialog(permission_page)
    NoOfferGuestUser.validate_subscription_update(guest_user_page)
    NoOfferGuestUser.click_subscription_update(guest_user_page)
    NoOfferGuestUser.click_email_field(guest_user_page)
    NoOfferGuestUser.click_submit_button(guest_user_page)
    assert NoOfferGuestUser.is_subscription_update_visible(guest_user_page), "Subscription update element is not visible."
    LoginPage.tap_earn(guest_user_page)
    LoginPage.tap_continue_with_email(guest_user_page)
    LoginPage.enter_email(guest_user_page, "test@gmail.com")
    LoginPage.enter_password(guest_user_page, "test1234")
    LoginPage.tap_login(guest_user_page)
    assert LoginPage.is_login_successful(guest_user_page), "Login was not successful."
    





