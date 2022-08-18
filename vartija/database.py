"""
Vartija
Copyright 2022 Alberto Morón Hernández

Management utilities for the DynamoDB instance
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

"""
import os

import boto3
from mypy_boto3_dynamodb import DynamoDBClient


class Database:

    def create_ddb_client(self) -> DynamoDBClient:
        """
        Establish a connection with the DynamoDB instance.
        """
        return boto3.client(
            'dynamodb',
            endpoint_url=os.environ.get('AWS_DYNAMODB_ENDPOINT'),
            region_name=os.environ.get('AWS_REGION'),
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
        )
