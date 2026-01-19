from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = ".inventory_list"
        self.menu_button = "#react-burger-menu-btn"

    def is_opened(self) -> bool:
        return self.page.is_visible(self.inventory_container)

    def menu_is_visible(self) -> bool:
        return self.page.is_visible(self.menu_button)
