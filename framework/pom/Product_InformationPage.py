from framework.base.Selenium_driver import SeleniumDriver

class Product_InfornationPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _add_to_cart = "add-to-cart-button"
    _cart_popup = "attach-close_sideSheet-link"


    def addto_cart(self):

       self.elementClick(self._add_to_cart,"id")


    def handle_cart_popup(self):
        self.elementClick(self._cart_popup,"id")