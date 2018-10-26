from tests.base import DriverMethods


class RegistrationScreen(DriverMethods):

    def click_on_next(self):
        self.find_element_by_xpath('//XCUIElementTypeOther[@name="NEXT"]').click()

    def get_personal_info_field(self):
        return self.get_element_by_xpath('//XCUIElementTypeOther[@name="First Name"]//XCUIElementTypeTextField')

    def submit_personal_information(self, first_name, last_name, email):
        self.enter_text('//XCUIElementTypeOther[@name="First Name"]//XCUIElementTypeTextField', first_name)
        self.enter_text('//XCUIElementTypeOther[@name="Last Name"]//XCUIElementTypeTextField', last_name)
        self.enter_text('//XCUIElementTypeOther[@name="Email"]//XCUIElementTypeTextField', email)
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="CREATE MY ACCOUNT"])[2]').click()
