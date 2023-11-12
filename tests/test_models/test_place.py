#!/usr/bin/python3
from models.place import Place
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    '''
    =========================
    Place tests
    =========================
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = Place
        self.test_name = "Place"

    def test_city_id(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.city_id, str)

    def test_user_id(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.user_id, str)

    def test_city_name(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.name, str)

    def test_description(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.description, str)

    def test_num_rooms(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.number_rooms, int)

    def test_num_bathrooms(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.number_bathrooms, int)

    def test_max_guest(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.max_guest, int)

    def test_price_by_nigt(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.price_by_night, int)

    def test_longitude(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.longitude, float)

    def test_latitude(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.latitude, float)

    def test_amenity_id(self):
        '''
        Attribute test
        '''
        place = self.test_class()
        self.assertIsInstance(place.amenity_ids, list)
