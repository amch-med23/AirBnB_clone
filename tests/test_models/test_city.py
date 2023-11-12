#!/usr/bin/python3
from models.city import City

from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    '''
    =========================
    User tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = City
        self.test_name = "City"

    def test_cityName(self):
        '''
        Attribute test
        '''
        city = self.test_class()
        self.assertIsInstance(city.name, str)

    def test_stateID(self):
        '''
        Attribute test
        '''
        city = self.test_class()
        self.assertIsInstance(city.state_id, str)
