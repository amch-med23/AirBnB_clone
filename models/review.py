#!/usr/bin/python3
"""
This is the class Review, it inherits form BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review class handles the review attributes
    """
    place_id = ""
    user_id = ""
    text = ""
