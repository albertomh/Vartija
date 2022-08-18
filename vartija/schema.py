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
