from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
from framework.pom.Product_InformationPage import Product_InfornationPage
import pytest
import unittest
import json


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_Product_Information(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pl = ProductListPage(self.driver)
        self.pi = Product_InfornationPage(self.driver)
        self.bc = Product_InfornationPage(self.driver)

    @pytest.mark.run(order=1)
    def test_ProductListPage(self):
        prod_name = json.loads(open("ReadProductName.json").read())
        self.hp.search(prod_name)
        self.pi.product_click()




