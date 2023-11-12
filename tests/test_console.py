#!/usr/bin/python3
"""
TEST CONSOLE
"""
from console import HBNBCommand
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel


class Test_console(unittest.TestCase):
    """check commands"""
    def test_prompt(self):
        """comprobamos que la cadena del prompt sea correcta"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
