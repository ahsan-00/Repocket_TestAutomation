# utils/driver_factory.py

import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


class DriverFactory:
    def __init__(self, platform):
        self.platform = platform.lower()
        self.appium_server = "http://127.0.0.1:4723"

    def create_driver(self):
        if self.platform == "android":
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.device_name = "emulator-5554"  # or your actual device name
            options.app = os.path.abspath("app/Repocket.apk")
            options.automation_name = "UiAutomator2"

        elif self.platform == "ios":
            options = XCUITestOptions()
            options.platform_name = "iOS"
            options.device_name = "iPhone Simulator"
            options.platform_version = "16.0"
            options.app = "/path/to/your.app"
            options.automation_name = "XCUITest"

        else:
            raise ValueError("Unsupported platform: choose 'android' or 'ios'.")

        return webdriver.Remote(
            command_executor=self.appium_server,
            options=options
        )
