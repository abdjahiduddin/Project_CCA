import pandas as pd
from datetime import datetime
from decimal import Decimal
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    resource = boto3.resource('dynamodb')

    timestamp = event['time']
    dt_object = datetime.fromtimestamp(timestamp)

    date = str(dt_object).split(" ")[0]

    min_time = date + " " + "00:00:01"
    max_time = date + " " + "23:59:59"

    min_do = datetime.strptime(min_time, '%Y-%m-%d %H:%M:%S')
    max_do = datetime.strptime(max_time, '%Y-%m-%d %H:%M:%S')

    min_ts = datetime.timestamp(min_do)
    max_ts = datetime.timestamp(max_do)

    # GET TABLE LIST
    response = client.list_tables()
    list_tables = []
    list_data = []
    for item in response["TableNames"]:
        if item == "mean":
            pass
        else:
            list_tables.append(item)

    # GET NEW DATA FROM EACH TABLES
    for item in list_tables:
        tmp = []
        table = resource.Table(item)
        response = table.query(
            KeyConditionExpression=Key('ID').eq(item) & Key(
                'Timestamp').between(Decimal(min_ts), Decimal(max_ts)),
            ScanIndexForward=False
        )
        for data in response['Items']:
            tmp.append(float(data['Filled']))
        list_data.append(tmp)

    # Find mean of Each Sensor by date
    df = pd.DataFrame(list_data)

    mean = df.mean(axis=1)
    mean = mean.tolist()

    # Insert data to mean table
    final_data = []
    counter = 0
    for i in mean:
        payload = {
            "id" : date,
            "sensor" : list_tables[counter],
            "mean" : str(i)
        }
        counter = counter + 1
        final_data.append(payload)
    