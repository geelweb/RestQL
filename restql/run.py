# -*- coding: utf8 -*-

import os
import argparse
import restql
from restql.views import *

def main():
    """
    Entry point

    """
    parser = argparse.ArgumentParser(add_help=False, prog='restql')
    parser.add_argument('-h', '--host', help='Server host', default='localhost')
    parser.add_argument('-p', '--port', help='Server port', default='8080')
    parser.add_argument('-m', '--module', help="""
        Name of the module where db entities are defined
        (eg restql.examples.dbentities)""",
        required=True)
    parser.add_argument('-d', '--debug', help='Activate sql debug', action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s ' + restql.__version__)
    parser.add_argument('--help', help='show this help message and exit', action='help')

    args = parser.parse_args()

    if args.debug:
        sql_debug(True)

    os.environ['DB_ENTITIES_MODULE_NAME'] = args.module

    run(host=args.host, port=args.port)

if __name__ == '__main__':
    main()
