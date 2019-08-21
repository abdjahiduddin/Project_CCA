import boto3
from boto3.dynamodb.conditions import Key,Attr
import json

resource = boto3.resource('dynamodb')
table = resource.Table('21-BA')

response = table.scan(
    Limit= 1
)
print(response)