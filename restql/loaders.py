# -*- coding: utf8 -*-

import os

class LoaderError(Exception):
    pass

def load_entity(class_name):
    """
    Returns the class defined in the dbentities module according to the
    class_name

    :param class_name: Class name to load
    :type  class_name: string

    :return: Entity class
    :rtype: pony.orm.core.Entity

    :todo: the dbentities module should be configurable (that's why it's not
    directly imported)
    """
    module_name = os.environ['DB_ENTITIES_MODULE_NAME']
    try:
        module = __import__(module_name)
        for k in module_name.split('.')[1:]:
            module = getattr(module, k)
        my_class = getattr(module, class_name)
    except AttributeError:
        raise LoaderError('Entity "%s" not found' % class_name)

    return my_class


