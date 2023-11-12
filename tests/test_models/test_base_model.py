#!/usr/bin/python3
"""
TEST OF CLASS BASE
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """def class Testbasemodel"""

    def test_instancias(self):
        """checkear si se crearon las instancias"""
        obj1 = BaseModel()
        self.assertTrue(hasattr(obj1, "id"))
        self.assertTrue(hasattr(obj1, "created_at"))
        self.assertTrue(hasattr(obj1, "updated_at"))
        self.assertEqual(type(obj1), BaseModel)

    def test_id(self):
        """2 instancias deben tener diferente id"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertFalse(obj1.id == obj2.id)

    def test_data_dif(self):
        """crear 2 instancias en diferentes tiempos"""
        obj1 = BaseModel()
        sleep(0.1)
        obj2 = BaseModel()
        self.assertNotEqual(obj1.created_at, obj2.created_at)

    def test_date(self):
        """test date"""
        obj1 = BaseModel()
        self.assertEqual(obj1.created_at, obj1.updated_at)

    def test_date_types(self):
        """chequeamos tipos date"""
        obj = BaseModel()
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)

    def test_format_date(self):
        """chequeamos el formato de date"""
        obj = BaseModel()
        dic = obj.to_dict()
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)

    def test_save(self):
        """test save"""
        obj1 = BaseModel()
        obj1.save()
        self.assertNotEqual(obj1.created_at, obj1.updated_at)

    def test_save(self):
        """chequeamos función save en 2 llamadas distintas"""
        obj = BaseModel()
        obj.save()
        sleep(0.1)
        obj.save()
        self.assertLess(obj.created_at, obj.updated_at)

    def test_id_assign(self):
        """ """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertEqual(len(obj.id), 36)        

    def test_dict(self):
        """comprobar typo del update luego de to_dict()"""
        obj1 = BaseModel()
        dic = obj1.to_dict()
        self.assertEqual(type(dic["updated_at"]), str)
        self.assertEqual(type(dic["created_at"]), str)

    def test_dict2(self):
        """comprobar existencia de keys """
        obj = BaseModel()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())

    def test_to_dict(self):
        """
        test to dict method
        """
        obj = BaseModel()
        dic = obj.to_dict()
        self.assertIsInstance(dic, dict)
    
    def test_dict_equal(self):
        """comprobar igualdad de attributos"""
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_kwarg(self):
        """test que valida que se llene mediante un diccionario"""
        dic = {'id': '12', 'created_at': '2017-09-28T21:03:54.052302',
               'updated_at': '2017-09-28T21:03:54.052302'}
        obj1 = BaseModel(**dic)
        data1 = '%Y-%m-%dT%H:%M:%S.%f'
        data2 = '2017-09-28T21:03:54.052302'

        self.assertEqual(obj1.id, "12")
        self.assertEqual(obj1.created_at, datetime.strptime(data2, data1))
        self.assertEqual(obj1.updated_at, datetime.strptime(data2, data1))
        self.assertEqual(type(dic["created_at"]), str)

    def test_kwargs_more(self):
        """chequeamos que este creando bien los atributos con kwargs"""
        obj = BaseModel(name="Naruto")
        self.assertTrue(hasattr(obj, "name"))

    def test_no_kwarg(self):
        """chequeamos la instanciacion cunado no recibe args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_str(self):
        """chequeo de la str function"""
        obj = BaseModel()
        self.assertEqual(type(str(obj)), str)
        # self.assertEqual(type(__str__(obj)), str)

    def test_more_attr(self):
        """chequeamos si se estan creando atributos"""
        obj = BaseModel()
        obj.name = "naruto"
        self.assertIn("name", obj.to_dict())

    def test_documentation(self):
        """
        chequeamos la documentacion
        """
        self.assertIsNotNone(BaseModel.__doc__)


if __name__ == '__main__':
    unittest.main()
