from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.Product_InformationPage import Product_InfornationPage
from framework.pom.CartPage import CartPage
import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_Add_same_itemMultipleTimes(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pl = ProductListPage(self.driver)
        self.pi = Product_InfornationPage(self.driver)
        self.cp = CartPage(self.driver)


    @pytest.mark.run(order=1)
    def test_ProductListPage(self):
        self.hp.mouse_hover()
        self.pl.product_grid_computer()
        self.pi.addto_cart()
        self.pi.handle_cart_popup()
        time.sleep(5)
        fc = int(self.hp.cart_count())
        firstCount = str(fc + 1)
        self.hp.mouse_hover()
        self.pl.product_grid_computer()
        self.pi.addto_cart()
        self.pi.handle_cart_popup()
        time.sleep(2)
        self.cp.cart_icon()
        self.pi.addto_cart()
        secontCount = self.hp.cart_count()
        assert secontCount in firstCount, "cart count not incremented"
        print("cart count incremented")


