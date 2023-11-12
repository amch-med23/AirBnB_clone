#!/usr/bin/python3
"""
TEST OF CLASS FileStorage
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    def test_instances(self):
        """chequeamos instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        obj = FileStorage()
        """checking the documentation"""
        self.assertIsInstance(obj, FileStorage)
        self.assertIsNotNone(FileStorage.new.__doc__)        
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    if __name__ == '__main__':
        unittest.main()
