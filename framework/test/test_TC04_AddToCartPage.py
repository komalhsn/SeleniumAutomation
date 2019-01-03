from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.Product_InformationPage import Product_InfornationPage
import time
import pytest
import unittest
import json


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_AddToCartPage(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pl = ProductListPage(self.driver)
        self.pi = Product_InfornationPage(self.driver)



    @pytest.mark.run(order=1)
    def test_ProductListPage(self):
        prod_name = json.loads(open("ReadProductName.json").read())
        self.hp.search(prod_name)
        self.pl.product_click()
        self.pi.addto_cart()
        time.sleep(3)
        self.hp.mouse_hover()
        # self.pl.book_click()
        self.pl.product_grid_computer()
        fc = int(self.hp.cart_count())
        firstCount = str(fc + 1)
        self.pi.addto_cart()
        self.pi.handle_cart_popup()
        secondCount=self.hp.cart_count()
        assert secondCount in firstCount, "cart count not incremented"

