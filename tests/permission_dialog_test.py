# tests/permission_dialog_test.py

import pytest
from pages.permission_dialog import PermissionPage

@pytest.mark.smoke
def test_valid_login(driver):
    permission_page = PermissionPage(driver)

    # Handle permission dialog if it appears
    PermissionPage.validate_permission_dialog(permission_page)
    PermissionPage.validate_notification_icon(permission_page)
    PermissionPage.validate_notification_text(permission_page)
    # PermissionPage.allow_permission_dialog(permission_page)
    PermissionPage.deny_permission_dialog(permission_page)
    PermissionPage.validate_rePocket_home(permission_page)
    PermissionPage.validate_main_notification_icon(permission_page)
    PermissionPage.validate_active_task(permission_page)



