# tests/guest_with_offers.py
import time
import pytest
from pages.permission_dialog import PermissionPage
from pages.guest_with_offrs import GuestUser

@pytest.mark.smoke
def test_valid_login(driver):
    permission_page = PermissionPage(driver)
    guest_user_page = GuestUser(driver)

    PermissionPage.allow_permission_dialog(permission_page)
    time.sleep(5)
    GuestUser.validate_slideup(guest_user_page)
    GuestUser.swipe_up_to_explore_tasks(guest_user_page)
    GuestUser.validate_details(guest_user_page)
    # GuestUser.tap_detail_button(guest_user_page)




