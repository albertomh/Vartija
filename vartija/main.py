#!/usr/bin/env python3

"""
Vartija
Copyright 2022 Alberto Morón Hernández

Lambda entrypoint
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""

import sys

from .dynamodb import DynamoDB
from .schema import Schema


def handler(event, context):
    #ddb = DynamoDB()
    #schema = Schema(ddb)

    return f"Vartija using Python {sys.version_info.major}.{sys.version_info.minor}"
