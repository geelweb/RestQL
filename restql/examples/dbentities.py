# -*- coding: utf8 -*-

from pony.orm import *

db = Database('sqlite', ':memory:')
class Person(db.Entity):
    name = Required(unicode)
    age = Required(int)

db.generate_mapping(create_tables=True)
