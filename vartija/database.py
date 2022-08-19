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

    __dynamodb: DynamoDBClient = None  # type: ignore

    def __init__(self):
        self.__dynamodb = self.get_dynamodb()

    def get_dynamodb(self) -> DynamoDBClient:
        """
        Return the DynamoDB instance used by Vartija.
        """
        if self.__dynamodb is None:
            self.__dynamodb = self.create_ddb_client()
        return self.__dynamodb

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

    def has_pending_migrations(self) -> bool:
        """
        Return whether or not all the tables defined in `Schema::get_schema` 
        have been created in the DynamoDB instance.
        """
        tables = self.get_dynamodb().list_tables()['TableNames']
        return len(tables) < 1
