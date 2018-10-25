import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPIUM_SERVER = 'http://127.0.0.1:4723/wd/hub'
DESIRED_CAPABILITIES = {
  "platformName": "iOS",
  "platformVersion": "10.3",
  "deviceName": "iPhone 7",
  "automationName": "XCUITest",
  "app": os.path.join(PROJECT_PATH, 'apps', 'app.zip')
}
