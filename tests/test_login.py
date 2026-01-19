import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, INVENTORY_URL


@allure.feature("Login")
class TestLogin:

    @allure.story("Successful login")
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.open(BASE_URL)
        login_page.login("standard_user", "secret_sauce")

        page.wait_for_url(INVENTORY_URL)

        assert page.url == INVENTORY_URL
        assert inventory_page.is_opened()
        assert inventory_page.menu_is_visible()

    @allure.story("Wrong password")
    def test_login_wrong_password(self, page):
        login_page = LoginPage(page)

        login_page.open(BASE_URL)
        login_page.login("standard_user", "wrong_password")

        assert "Username and password do not match" in login_page.get_error_text()

    @allure.story("Locked out user")
    def test_locked_out_user(self, page):
        login_page = LoginPage(page)

        login_page.open(BASE_URL)
        login_page.login("locked_out_user", "secret_sauce")

        assert "locked out" in login_page.get_error_text().lower()

    @allure.story("Empty fields")
    def test_login_empty_fields(self, page):
        login_page = LoginPage(page)

        login_page.open(BASE_URL)
        login_page.login()

        assert "Username is required" in login_page.get_error_text()

    @allure.story("Performance glitch user")
    def test_performance_glitch_user(self, page):
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.open(BASE_URL)
        login_page.login("performance_glitch_user", "secret_sauce")

        page.wait_for_url(INVENTORY_URL, timeout=10000)

        assert page.url == INVENTORY_URL
        assert inventory_page.is_opened()
