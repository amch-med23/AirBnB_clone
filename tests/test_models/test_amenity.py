#!/usr/bin/python3
"""
TEST OF CLASS AMENITY
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    def test_procedence(self):
        """chequeamos que sea otra subclase de basemodel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_clase(self):
        """
        test class & test subclass
        """
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_no_receive(self):
        """chequeamos cuando no recibe nada"""
        self.assertEqual(Amenity, type(Amenity()))

    """Casos de prueba para la clase Amenity"""
    def test_attr(self):
        """chequeamos existencia de atributo"""
        obj = Amenity()
        self.assertTrue(hasattr(obj, "name"))
        self.assertEqual(obj.name, "")
        obj.name = "Naruto"
        self.assertEqual(obj.name, "Naruto")

    def test_instances_attr(self):
        """chequeamos attr(type, value) y confirmamos procedencia"""
        obj = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertEqual(obj.name, "")
        self.assertEqual(type(obj.name), str)

    def test_dif_id(self):
        """Chequeamos cambios de id"""
        obj = Amenity()
        other = Amenity()
        self.assertNotEqual(obj, other)

    def test_date_amen(self):
        """chequeamos methods in different times"""
        obj1 = Amenity()
        sleep(0.2)
        obj2 = Amenity()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)
        self.assertLess(obj1.created_at, obj2.created_at)

    def test_str_amen(self):
        obj = Amenity()
        obj.id = "123"
        obj_str = obj.__str__()
        self.assertIn("[Amenity] (123)", obj_str)

    def test_documentation(self):
        """
        chequeamos la documentacion
        """
        self.assertIsNotNone(Amenity.__doc__)    


if __name__ == '__main__':
    unittest.main()
