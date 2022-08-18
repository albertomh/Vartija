"""
Vartija
Copyright 2022 Alberto Morón Hernández

Database schema
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""
from typing import List, TypedDict


# Schema type definitions
AttributeDefinitionEntry = TypedDict('AttributeDefinitionEntry', {'AttributeName': str, 'AttributeType': str})
KeySchemaEntry = TypedDict('KeySchemaEntry', {'AttributeName': str, 'KeyType': str})

class VartijaDDBTable(TypedDict):
    TableName: str
    AttributeDefinitions: List[AttributeDefinitionEntry]
    KeySchema: List[KeySchemaEntry]
