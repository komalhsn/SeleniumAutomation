from framework.pom.HomePage import HomePage
import pytest
import unittest
import json



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_SearchBar(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)



    @pytest.mark.run(order=1)
    def test_HomePage(self):
        prod_name=json.loads(open("ReadProductName.json").read())
        self.hp.search(prod_name)



