# tests/forgotpass_test.py

import pytest
import json
import os
from pages.forgotpass_page import ForgotPassPage
from pages.login_page import LoginPage
from pages.permission_dialog import PermissionPage

@pytest.mark.smoke

def test_empty_recovery(driver):
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)
    forgot_pass_page = ForgotPassPage(driver)

    # Handle permission dialog if it appears
    permission_dialog.allow_permission_dialog()
    # login_page.handle_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continue_with_email()
    # login_page.tap_continue_with_email()
    login_page.verify_forgot_password()
    login_page.tap_forgot_password()
    login_page.enter_email("")
    forgot_pass_page.tap_recover_button()

def test_invalid_recovery(driver):
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)
    forgot_pass_page = ForgotPassPage(driver)

    try:
        # Load credentials from JSON file
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as file:
            credentials = json.load(file)
            invalid_email = credentials['invalid_email']
    except FileNotFoundError:
        pytest.fail(f"Config file not found at '{config_path}'")
    except KeyError as e:
        pytest.fail(f"Missing key in config file: {e}")
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON format in config file")

    # Handle permission dialog if it appears
    permission_dialog.allow_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continue_with_email()
    login_page.verify_forgot_password()
    login_page.tap_forgot_password()
    login_page.enter_email(invalid_email)
    forgot_pass_page.tap_recover_button()
    
def test_valid_recovery(driver):
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)
    forgot_pass_page = ForgotPassPage(driver)

    try:
        # Load credentials from JSON file
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as file:
            credentials = json.load(file)
            valid_email = credentials['email']
    except FileNotFoundError:
        pytest.fail(f"Config file not found at '{config_path}'")
    except KeyError as e:
        pytest.fail(f"Missing key in config file: {e}")
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON format in config file")

    # Handle permission dialog if it appears
    permission_dialog.allow_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continue_with_email()
    login_page.verify_forgot_password()
    login_page.tap_forgot_password()
    login_page.enter_email(valid_email)
    forgot_pass_page.tap_recover_button()
    