#!/usr/bin/python3
"""
TEST THE CONSOLE
"""
from console import HBNBCommand
from datetime import datetime
import unittest
from time import sleep
import json
from models.base_model import BaseModel


class Test_console(unittest.TestCase):
    """check the commands commands"""
    def test_prompt(self):
        """checks if the prompt result is correct """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
