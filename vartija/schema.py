"""
Vartija
Copyright 2022 Alberto Morón Hernández

Single-table database schema
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""
from typing import List, TypedDict

from mypy_boto3_dynamodb.type_defs import (
    AttributeDefinitionTypeDef,
    KeySchemaElementTypeDef,
    ProvisionedThroughputTypeDef
)

VartijaDDBTable = TypedDict(
    'VartijaDDBTable', {
        'TableName': str,
        'AttributeDefinitions': List[AttributeDefinitionTypeDef],
        'KeySchema': List[KeySchemaElementTypeDef],
        'ProvisionedThroughput': ProvisionedThroughputTypeDef
})

class Schema:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_schema() -> VartijaDDBTable:
        """
        Vartija uses a single-table schema. Returns the definition 
        of this table in the form:
            {
                'TableName': '<table_name>',
                'AttributeDefinitions': [
                    {
                        'AttributeName': '<name>',
                        'AttributeType': '<one of 'S','N','B'>'
                    }, ...
                ],
                'KeySchema': [
                    {
                        'AttributeName': '<name>',
                        'KeyType': 'HASH'
                    }
                ]
            }
        """

        vartija_table: VartijaDDBTable = {
            'TableName': 'VartijaData',
            'AttributeDefinitions': [
                {
                    'AttributeName': 'Timestamp',  # ISO8601
                    'AttributeType': 'S'           # 1970-01-01T10:20:00
                }
            ],
            'KeySchema': [
                {
                    'AttributeName': 'Timestamp',
                    'KeyType': 'HASH'
                }
            ],

            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        }

        return vartija_table
