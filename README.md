# RestQL

**RestQL** is a simple REST server designed to provide a complete interface for
SQL databases.

## Requirements

 * [Bottle](http://bottlepy.org)
 * [Pony ORM](http://ponyorm.com)

## Features

 * CRUD support

## Installation

From source

    python setup.py build
    python setup.py install

## Configuration

Create your database entities like in the file examples/dbentities.py. Ensure
this module is in your PYTHON_PATH

## Execution

Start the REST server

    restql-run --module restql.examples.dbentities

## CRUD utilisation

Create a new record in the table Person

    $ curl http://localhost:8080/Person -X POST -d"name=Jack" -d"age=42"
    {"age": 42, "id": 1, "name": "Jack"}

Get all the records in the table Person

    $ curl http://localhost:8080/Person
    [{"age": 42, "id": 1, "name": "Jack"}]

Update the record of the table Person with id = 1

    $ curl http://localhost:8080/Person/1 -X PUT -d"name=Jacques"
    {"age": 42, "id": 1, "name": "Jacques"}

Get the record of the table Person with id = 1

    $ curl http://localhost:8080/Person/1
    {"age": 42, "id": 1, "name": "Jacques"}

Delete the record of the table Person with id = 1

    $ curl http://localhost:8080/Person/1 -X DELETE
    True
