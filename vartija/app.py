# Vartija | Lambda entrypoint
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
# Copyright 2022 Alberto Morón Hernández
import sys

import boto3


def handler(event, context):
    return f"Vartija using Python {sys.version}"
