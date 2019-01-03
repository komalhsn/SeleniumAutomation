from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.Product_InformationPage import Product_InfornationPage
from framework.pom.CartPage import CartPage
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_RemoveCart(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pl = ProductListPage(self.driver)
        self.pi = Product_InfornationPage(self.driver)
        self.cp = CartPage(self.driver)


    @pytest.mark.run(order=1)
    def test_ProductListPage(self):
        self.hp.search("nikon d5300")
        self.pl.product_click()
        self.pi.addto_cart()
        self.hp.mouse_hover()
        self.pl.book_click()
        self.pl.product_click()
        self.pi.addto_cart()
        self.cp.cart_icon()
        # totalPrice=int(self.cp.check_sub_totalprice())
        price=self.cp.check_price()
       # self.cp.delete_item()
        # difference = str(int(totalPrice) - int(price))
        # assert price in difference, "price not matching"
        # self.cp.check_price()

