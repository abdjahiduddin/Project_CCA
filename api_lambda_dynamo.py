import boto3
from boto3.dynamodb.conditions import Key,Attr
import json

client = boto3.client('dynamodb')
resource = boto3.resource('dynamodb')

# GET TABLE LIST
response = client.list_tables()
list_tables = []
for item in response["TableNames"]:
    list_tables.append(item)

payload = []
#GET NEW DATA FROM EACH TABLES
for item in list_tables:
    table = resource.Table(item)

    response = table.query(
        KeyConditionExpression=Key('ID').eq(item) & Key('Timestamp').gte(1566185590),
        ScanIndexForward= False,
        Limit= 1
    )

    data = {
        "Filled": float(response['Items'][0]['Filled']),
        "Height": float(response['Items'][0]['Height']),
        "ID": "41-DA",
        "Location": "JL. ABCDEFGHIJ KLMNO 4",
        "Percent": float(response['Items'][0]['Percent']),
        "Timestamp": float(response['Items'][0]['Timestamp']),
    } 
    payload.append(data)
    

payload = json.dumps(payload)



