#!/usr/bin/python3
'''
this is the class User, it inherents from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Class User inherits from BaseModel
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
