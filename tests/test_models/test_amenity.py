#!/usr/bin/python3

from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    '''
    =========================
    Amenity tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = Amenity
        self.test_name = "Amenity"

    def test_amenity(self):
        '''
        Attribute test
        '''
        amenity = self.test_class()
        self.assertIsInstance(amenity.name, str)
