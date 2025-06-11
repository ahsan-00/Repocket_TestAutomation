# tests/navigate_offers_test.py

import pytest
import os
import json
from pages.permission_dialog import PermissionPage
from pages.guest_with_offrs import GuestUser
from pages.login_page import LoginPage
from pages.explore_and_earn import ExploreandEarn


@pytest.mark.smoke


def test_valid_login(driver):
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)
    explore_page = ExploreandEarn(driver)
    guest_user = GuestUser(driver)

    try:
        # Load credentials from JSON file
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as file:
            credentials = json.load(file)
            email = credentials['email']
            password = credentials['password']
    except FileNotFoundError:
        pytest.fail(f"Config file not found at '{config_path}'")
    except KeyError as e:
        pytest.fail(f"Missing key in config file: {e}")
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON format in config file")

    # Handle permission dialog if it appears
    permission_dialog.allow_permission_dialog()
    guest_user.swipe_up_to_explore_tasks(2)

    # login_page.handle_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continue_with_email()
    # login_page.tap_continue_with_email()
    login_page.verify_forgot_password()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.tap_eye_button()
    login_page.tap_login()
    # guest_user.swipe_up_to_explore_tasks(2)
    login_page.tap_earn()
    explore_page.validate_earnandexplore()
    # explore_page.click_available("available")
    # explore_page.click_active("active")
    # explore_page.click_history("history")