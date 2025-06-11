# tests/navigate_offers_test.py

import pytest

from pages.permission_dialog import PermissionPage
from pages.guest_with_offrs import GuestUser
from pages.login_page import LoginPage
from tests.login_test import test_valid_login

@pytest.mark.smoke
def test_valid_login(driver):
    permission_page = PermissionPage(driver)
    guest_user_page = GuestUser(driver)
    login_page = LoginPage(driver)

    # Handle permission dialog if it appears
    PermissionPage.validate_permission_dialog(permission_page)
    PermissionPage.allow_permission_dialog(permission_page)


    PermissionPage.validate_rePocket_home(permission_page)
    PermissionPage.validate_main_notification_icon(permission_page)
    PermissionPage.validate_active_task(permission_page)

    GuestUser.validate_slideup(guest_user_page)
    GuestUser.swipe_up_to_explore_tasks(guest_user_page)
    LoginPage.tap_earn(login_page)
    LoginPage.tap_continue_with_email(login_page)
    LoginPage.enter_email(login_page)
    LoginPage.enter_password(login_page)
    LoginPage.tap_login(login_page)
    LoginPage.tap_earn(login_page)
    









