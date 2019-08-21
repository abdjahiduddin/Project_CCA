import boto3
from decimal import Decimal


# boto3 is the AWS SDK library for Python.
# The "resources" interface allow for a higher-level abstraction than the low-level client interface.
# More details here: http://boto3.readthedocs.io/en/latest/guide/resources.html
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#Testing
table = dynamodb.Table('61-FA')

dummy = {
    "id": "123",
    "payload": {
        "filled": 120,
        "height": 150,
        "id": "123",
        "location": "jl. abcde 3",
        "timestamp": 1566362510
    },
    "timestamp": 1566362510
}

percent = (dummy['payload']['filled'] / dummy['payload']['height']) * 100

payload = {
        "Filled": Decimal(dummy['payload']['filled']),
        "Height": Decimal(dummy['payload']['height']),
        "ID": dummy['id'],
        "Location": dummy['payload']['location'],
        "Percent": Decimal(percent),
        "Timestamp": Decimal(dummy['timestamp']),
    } 


# The BatchWriteItem API allows us to write multiple items to a table in one request.
table.put_item(Item=payload)

#Deploy
import boto3
from decimal import Decimal
import json


def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    tableName = event['id']

    table = dynamodb.Table(tableName)
    
    percent = (event['filled'] / event['height']) * 100
    
    payload = {
            "Filled": Decimal(event['filled']),
            "Height": Decimal(event['height']),
            "ID": event['id'],
            "Location": event['location'],
            "Percent": Decimal(percent),
            "Timestamp": Decimal(event['timestamp']),
        } 
    
    table.put_item(Item=payload)