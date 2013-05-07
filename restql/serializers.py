# -*- coding: utf8 -*-

import json

def serialize_entity(class_entity):
    """
    Serializes a database object entity

    :param class_entity: The Entity object to serialize
    :type  class_entity: pony.orm.core.Entity

    :return: The json representation of the object
    :rtype: string

    >>> from pony.orm import *
    >>> db = Database('sqlite', ':memory:')
    >>> class Person(db.Entity):
    ...     name = Required(unicode)
    ...     age = Required(int)
    >>> db.generate_mapping(create_tables=True)
    >>> p = Person(name='John', age=42)
    >>> commit()
    >>> serialize_entity(p)
    '{"age": 42, "id": 1, "name": "John"}'
    """
    data = {}
    for k in class_entity.__class__.__dict__['_adict_']:
        data[k] = getattr(class_entity, k)
    return json.dumps(data)

def serialize_entity_collection(collection):
    """
    Serializes a collection of database entities

    :param collection: A collection of objects
    :type collection: list

    :return: The json representation of the list
    :rtype: string

    >>> from pony.orm import *
    >>> db = Database('sqlite', ':memory:')
    >>> class Person(db.Entity):
    ...     name = Required(unicode)
    ...     age = Required(int)
    >>> db.generate_mapping(create_tables=True)
    >>> p1 = Person(name='John', age=42)
    >>> p2 = Person(name='Jack', age=33)
    >>> commit()
    >>> serialize_entity_collection(select(r for r in Person))
    '[{"age": 42, "id": 1, "name": "John"}, {"age": 33, "id": 2, "name": "Jack"}]'
    """
    list = []
    for class_entity in collection:
        data = {}
        for k in class_entity.__class__.__dict__['_adict_']:
            data[k] = getattr(class_entity, k)
        list.append(data)
    return json.dumps(list)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
