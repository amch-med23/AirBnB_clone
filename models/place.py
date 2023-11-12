#!/usr/bin/python3
"""class PlaceAmenity"""


from models.base_model import BaseModel

class placeAmenity(BaseModel):
  """Class representing a place amenities."""

  user_id = ""
  name = ""
  city_id = ""
  description = ""
  number_rooms = ""
  number_pathrooms = ""
  max_guest = int
  price_per_night = int
