# tests/test_login.py
import pytest
import json
import os
# from pages import google_signin_page
from pages.login_page import LoginPage
from pages.permission_dialog import PermissionPage
from pages.google_signin_page import GoogleSignPage

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    permission_dialog = PermissionPage(driver)
    google_signin_page = GoogleSignPage(driver)

    try:
        # Load credentials from JSON file
        config_path = os.path.join('config', 'config.json')
        with open(config_path, 'r') as file:
            credentials = json.load(file)
    except FileNotFoundError:
        pytest.fail(f"Config file not found at '{config_path}'")
    except KeyError as e:
        pytest.fail(f"Missing key in config file: {e}")
    except json.JSONDecodeError:
        pytest.fail("Invalid JSON format in config file")

    permission_dialog.allow_permission_dialog()
    login_page.tap_earn()
    login_page.tap_continew_with_google()
    google_signin_page.tap_choose_account()
