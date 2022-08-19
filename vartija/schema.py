"""
Vartija
Copyright 2022 Alberto Morón Hernández

Single-table database schema
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""
import logging
from typing import List, TypedDict

from mypy_boto3_dynamodb.type_defs import (
    AttributeDefinitionTypeDef,
    KeySchemaElementTypeDef,
    ProvisionedThroughputTypeDef
)
from mypy_boto3_dynamodb.client import BotocoreClientError

from .database import Database


VartijaDDBTable = TypedDict(
    'VartijaDDBTable', {
        'TableName': str,
        'AttributeDefinitions': List[AttributeDefinitionTypeDef],
        'KeySchema': List[KeySchemaElementTypeDef],
        'ProvisionedThroughput': ProvisionedThroughputTypeDef
})

class Schema:

    db: Database

    def __init__(self, db: Database) -> None:
        self.db = db
        if self.db.has_pending_migrations():
            self.run_migrations()

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

    def run_migrations(self) -> None:
        """
        Create the necessary DynamoDB table and items.
        """

        schema: VartijaDDBTable = Schema.get_schema()

        try:
            table = self.db.get_dynamodb().create_table(**schema)
            logging.getLogger().info("Created DynamoDB table 'VartijaData'.")
            logging.getLogger().info(f"\ntablenames: {self.db.get_dynamodb().list_tables()['TableNames']}\n")
        except BotocoreClientError:
            logging.getLogger().error(f"Unable to create DynamoDB table 'VartijaData'. It might already exist.")
            raise
