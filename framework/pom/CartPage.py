from framework.base.Selenium_driver import SeleniumDriver

class CartPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _delete = "(//input[@value='Delete'])[1]"
    _subTotal = "//span[@class='a-size-medium a-color-price sc-price sc-white-space-nowrap  sc-price-sign']"
    _price1 = "(//p[@class='a-spacing-small'])"
    _cart_icon1 = "nav-cart-count"

    """ method is to click on delete link in cart page"""
    def delete_item(self):
        self.elementClick(self._delete,"xpath")


    """method to click in cart icon"""
    def cart_icon(self):
        self.elementClick(self._cart_icon1,"id")


    """method to get subtotal price of the items in cart """
    def check_sub_totalprice(self):
        subtotal_price=self.getElement(self._subTotal,"xpath").text
        return subtotal_price


    """method to get price of 1st item in cart page"""
    def check_price(self):
        price1=self.getElement(self._price1,"xpath").text
        return price1
