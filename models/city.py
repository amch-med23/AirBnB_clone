#!/usr/bin/env python3
"""
this is the class City, it inherents from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The class city inheriting from BaseModel.
    """

    state_id = ""
    name = ""
