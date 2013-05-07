# -*- coding: utf8 -*-

import bottle
from bottle import route, run, request, abort
from pony.orm import *

from restql.serializers import *
from restql.loaders import *

@route('/:table', method='GET')
@route('/:table/<id:int>', method='GET')
def get_records(table, id=None):
    """
    Lists the objects or one object loaded by it's ID

    :param table: The db table name
    :type  table: string

    :param id: The record ID
    :type  id: int

    :return: The json representation of the record(s)
    :rtype: string
    """
    try:
        my_class = load_entity(table)
    except LoaderError as e:
        abort(400, e)

    if id is not None:
        try:
            r = my_class[id]
        except ObjectNotFound:
            abort(404)
        return serialize_entity(r)

    records = select(r for r in my_class)
    return serialize_entity_collection(records)

@route('/:table', method='POST')
def post_record(table):
    """
    Creates new record

    :param table: The db table name
    :type  table: string

    :return: The json representation of the created record
    :rtype: string
    """
    try:
        my_class = load_entity(table)
    except LoaderError as e:
        abort(400, e)

    p= my_class(**request.params)
    commit()
    return serialize_entity(p)

@route('/:table/<id:int>', method='PUT')
def put_record(table, id):
    """
    Updates an existing record

    :param table: The db table name
    :type  table: string

    :param id: The record ID
    :type  id: int

    :return: The json representation of the updated record
    :rtype: string
    """
    try:
        my_class = load_entity(table)
    except LoaderError as e:
        abort(400, e)

    p = my_class[id]
    for k in request.params:
        setattr(p, k, getattr(request.params, k))
    commit()
    return serialize_entity(p)

@route('/:table/<id:int>', method='DELETE')
def del_record(table, id):
    """
    Removes a record

    :param table: The db table name
    :type  table: string

    :param id: The record ID
    :type  id: int

    :return: True if the record is deleted
    :rtype: boolean
    """
    try:
        my_class = load_entity(table)
    except LoaderError as e:
        abort(400, e)

    p = my_class[id]
    p.delete()
    return "True"
