#!/usr/bin/env python

import googlefed
import sys
import argparse

def init(args):
    args = vars(args)
    googlefed.GoogleApi(clientId=args['clientid'], clientSecret=args['clientsecret'])

def schema_verify(args):
    args = vars(args)
    schema = googlefed.Schema(customerId=args['customerid'])
    if schema.has_sso_schema():
        print("Schema exists")
    else:
        print("Schema does not exist")
        sys.exit(1)

def schema_create(args):
    args = vars(args)
    schema = googlefed.Schema(customerId=args['customerid'])
    if schema.has_sso_schema():
        return True

    print("Creating custom schema")

def schema_delete(args):
    args = vars(args)
    schema = googlefed.Schema(customerId=args['customerid'])
    if not schema.has_sso_schema():
        return True

    print("Deleting custom schema")

def main():
    parser = argparse.ArgumentParser(prog="Federator", description="Manage Google Apps configurations for AWS Single Sign On")
    main_subparsers = parser.add_subparsers(help="subcommand help")

    parser_init = main_subparsers.add_parser("init", help="Initial setup of Federator")
    parser_schema = main_subparsers.add_parser("schema", help="Operations on custom schema")
    
    parser_init.add_argument("-I", "--clientid", required=True)
    parser_init.add_argument("-S", "--clientsecret", required=True)
    parser_init.set_defaults(func=init)

    parser_schema.add_argument("-C", "--customerid", required=True)

    schema_subparser = parser_schema.add_subparsers(help="Schema subcommand help")
    parser_schema_create = schema_subparser.add_parser("create", help="Create the custom schema")
    parser_schema_create.set_defaults(func=schema_create)

    parser_schema_delete = schema_subparser.add_parser("delete", help="Delete the custom schema")
    parser_schema_delete.set_defaults(func=schema_delete)

    parser_schema_verify = schema_subparser.add_parser("verify", help="Delete the custom schema")
    parser_schema_verify.set_defaults(func=schema_verify)

    args = parser.parse_args()
    # have to clean out our command-line args or they get swallowed twice during init
    sys.argv = ['']
    args.func(args)

if __name__ == "__main__":
    main()
