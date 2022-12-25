from page_objects.login_page import LoginPage
from page_objects.logged_in_page import LoggedInSuccessfullyPage
import pytest

class TestLoginPage:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):  
        login_page = LoginPage(driver)  
        login_page.open("https://practicetestautomation.com/practice-test-login/")
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url
        assert logged_in_page.header == "Logged In Successfully"
        assert logged_in_page.is_logout_button_displayed, "Log"
    
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", 
                            [("incorrectUser", "Password123", "Your username is invalid!"), 
                            ("student", "IncorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open("https://practicetestautomation.com/practice-test-login/")
        login_page.execute_login(username, password)
        assert login_page.error_message.is_displayed(), "Error message is not displayed, but it should be"
        assert login_page.error_message == expected_error_message