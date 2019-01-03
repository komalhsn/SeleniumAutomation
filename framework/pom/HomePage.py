from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _searchbar = "//input[@id='twotabsearchtextbox']"
    _search_button = "//input[@type='submit' and @class='nav-input']"
    _departments = "//div[@id='nav-shop']//span[text()='Departments']"
    _book = "//div[@id='nav-flyout-shopAll']//span[text()='Books']"
    _cart_icon = "nav-cart-count"
    _computers = "//div[@id='nav-flyout-shopAll']//span[.='Computers']"



    """method to search a product and click on search icon"""
    def search(self,name):

        self.sendKeys(name, self._searchbar,"xpath")
        self.elementClick(self._search_button,"xpath")

    """ method to mouse hover to shop by department and click on particular link"""
    def mouse_hover(self):
        dept=self.getElement(self._departments,"xpath")
        action=ActionChains(self.driver)
        action.move_to_element(dept).perform()
        # self.elementClick(self._book,"xpath")
        self.elementClick(self._computers, "xpath")

    """method to count the item in cart icon"""
    def cart_count(self):
        count=self.getElement(self._cart_icon,"id").text
        return count


