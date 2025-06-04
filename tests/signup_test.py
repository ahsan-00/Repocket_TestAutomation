# tests/signup_test.py

import pytest
import json
import os
from pages.signup_page import SignUpPage
from pages.login_page import LoginPage
from pages.permission_dialog import PermissionPage

@pytest.mark.smoke

def test_empty_signup(driver):
    signup_page = SignUpPage(driver)
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)

    # Handle permission dialog if it appears
    permission_dialog.allow_permission_dialog()
    # login_page.handle_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continue_with_email()
    # login_page.tap_continue_with_email()
    login_page.verify_forgot_password()
    signup_page.tap_signup_link()
    signup_page.enter_name("")
    signup_page.enter_email("")
    signup_page.enter_password("")
    signup_page.enter_confirm_password("")
    signup_page.tap_eye_button()
    signup_page.tap_checkbox()
    signup_page.tap_signup_button()

    # Assert that the error message is displayed
    assert signup_page.is_error_message_displayed(), "Error message should be displayed for empty fields"


def test_invalid_signup(driver):
    signup_page = SignUpPage(driver)
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)

    try:
        # Load credentials from JSON file
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as file:
            credentials = json.load(file)
            siname = credentials['siname']
            siemail = credentials['siemail']
            sipassword = credentials['sipassword']
            scipassword = credentials['scipassword']

    except FileNotFoundError:
        pytest.fail(f"Config file not found at '{config_path}'")
    except KeyError as e:
        pytest.fail(f"Missing key in config file: {e}")
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON format in config file")

    # Handle permission dialog if it appears
    permission_dialog.allow_permission_dialog()
    # login_page.handle_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continue_with_email()
    # login_page.tap_continue_with_email()
    login_page.verify_forgot_password()
    signup_page.tap_signup_link()
    signup_page.enter_name(siname)
    signup_page.enter_email(siemail)
    signup_page.enter_password(sipassword)
    signup_page.enter_confirm_password(scipassword)
    signup_page.tap_eye_button()
    signup_page.tap_checkbox()
    signup_page.tap_signup_button()

    # Assert login failure
    # assert not login_page.is_login_successful(), "Login should have failed but was successful"

def test_valid_signup(driver):
    signup_page = SignUpPage(driver)
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)

    try:
        # Load credentials from JSON file
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as file:
            credentials = json.load(file)
            sname = credentials['sname']
            semail = credentials['semail']
            spassword = credentials['spassword']
            scpassword = credentials['scpassword']

    except FileNotFoundError:
        pytest.fail(f"Config file not found at '{config_path}'")
    except KeyError as e:
        pytest.fail(f"Missing key in config file: {e}")
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON format in config file")

    # Handle permission dialog if it appears
    permission_dialog.allow_permission_dialog()
    # login_page.handle_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continue_with_email()
    # login_page.tap_continue_with_email()
    login_page.verify_forgot_password()
    signup_page.tap_signup_link()
    signup_page.enter_name(sname)
    signup_page.enter_email(semail)
    signup_page.enter_password(spassword)
    signup_page.enter_confirm_password(scpassword)
    signup_page.tap_eye_button()
    signup_page.tap_checkbox()
    signup_page.tap_signup_button()

    # Assert login success
    # assert login_page.is_login_successful(), "Login failed: Dashboard not found"