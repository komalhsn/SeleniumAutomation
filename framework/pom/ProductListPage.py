from framework.base.Selenium_driver import SeleniumDriver

class ProductListPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    _brand_checkbox = "//div[@class='a-checkbox s-ref-link-cursor a-spacing-none']//input[@name='s-ref-checkbox-Nikon']"
    _product_list_element = "//span[@id='s-result-count']"
    _product_click = "(//div[@class='a-row a-spacing-none scx-truncate-medium sx-line-clamp-2']//h2)[1]"
    _book_click = "//div[@id='anonCarousel1']//span[.='Great Book of Woodworking Tips: Over 650...']"
    _product_grid_bookclick = "//div[@id='anonCarousel1']//span"
    _product_grid_computer_click = "//li[@id='result_0']//h2"


    #_brand_element="//span[.='Nikon']"


    def brand_filter(self):

       self.elementClick(self._brand_checkbox,"xpath")


    def verify_ProductListPage_successful(self):
        return self.elementPresenceCheck(self._product_list_element, "xpath")


    # def verify_brand_successful(self):
    #     return self.elementPresenceCheck(self._brand_element, "xpath")

    def product_click(self):
        self.elementClick(self._product_click, "xpath")



    def book_click(self):
        self.elementClick(self._book_click,"xpath")


    def product_grid_book_click(self):
        self.elementClick(self._product_grid_bookclick,"xpath")


    def product_grid_computer(self):
        self.elementClick(self._product_grid_computer_click,"xpath")

