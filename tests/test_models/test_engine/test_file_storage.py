#!/usr/bin/python3
""" handles the storage testing """
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    '''
    FileStorage test
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage

    def test_pathname(self):
        '''
        Attrib test
        '''
        test = self.test_class()
        self.assertIsInstance(test._FileStorage__file_path, str)

    def test_file_save(self):
        '''
        File creation test
        '''
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_objects(self):
        '''
        Test
        '''
        test = self.test_class()
        self.assertIsInstance(test._FileStorage__objects, dict)

    def tearDown(self):
        '''
        Destroy JSON file
        '''
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_file_empty(self):
        '''
        File empty test
        '''
        base = BaseModel()
        my_dict = base.to_dict()
        base.save()
        base2 = BaseModel(**my_dict)
        self.assertFalse(os.stat('file.json').st_size == 0)
    """Test FileStorage Class"""

    def test_instances(self):
        """ check instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """check docmentation """
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)
        self.assertIsNotNone(FileStorage.new.__doc__)        
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
