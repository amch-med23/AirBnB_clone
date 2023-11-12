#!/usr/bin/python3
""" This is the base model, the model every other model inherent from """

from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """
    This is the base calss that all the classes will use as a base
    """
    def __init__(self, *args, **kwargs):
        if (kwargs is not None and len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """ updates the updated_at instance to the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ return a dictionary based on the __dict__ instance """
        a_dict = self.__dict__.copy()
        a_dict['__class__'] = self.__class__.__name__
        a_dict['created_at'] = self.created_at.isoformat()
        a_dict['updated_at'] = self.updated_at.isoformat()
        return (a_dict)
