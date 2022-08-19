#!/usr/bin/env python3

"""
Vartija
Copyright 2022 Alberto Morón Hernández

Lambda entrypoint
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""
import sys
import logging


from .database import Database
from .schema import Schema


def handler(event, context):
    logging.getLogger().setLevel(logging.INFO)

    db = Database()
    schema = Schema(db)

    return f"Vartija using Python {sys.version_info.major}.{sys.version_info.minor}"
