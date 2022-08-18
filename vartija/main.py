#!/usr/bin/env python3

"""
Vartija
Copyright 2022 Alberto Morón Hernández

Lambda entrypoint
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""
import sys


from .database import Database


def handler(event, context):
    db = Database()

    return f"Vartija using Python {sys.version_info.major}.{sys.version_info.minor}"
