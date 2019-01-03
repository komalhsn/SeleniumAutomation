from framework.pom.HomePage import HomePage
from framework.pom.ProductListPage import ProductListPage
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_ProductList(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pl = ProductListPage(self.driver)

    @pytest.mark.run(order=1)
    def test_ProductListPage(self):
        self.hp.search("nikon d5300")
        self.pl.brand_filter()

    @pytest.mark.run(order=2)
    def test_verifyProductListPage(self):
        assert self.pl.verify_ProductListPage_successful

    # @pytest.mark.run(order=3)
    # def test_verify_brand_successful(self):
    #     assert self.bl.verify_brand_successful

