import boto3

# boto3 is the AWS SDK library for Python.
# We can use the low-level client to make API calls to DynamoDB.
client = boto3.client('dynamodb', region_name='us-east-1')

sensors = ["11-AA","21-BA","41-DA","51-EA","61-FA"]

for sensor in sensors:
    try:
        resp = client.create_table(
            TableName=sensor,
            # Declare your Primary Key in the KeySchema argument
            KeySchema=[
                {
                    "AttributeName": "ID",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "Timestamp",
                    "KeyType": "RANGE"
                }
            ],
            # Any attributes used in KeySchema or Indexes must be declared in AttributeDefinitions
            AttributeDefinitions=[
                {
                    "AttributeName": "ID",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "Timestamp",
                    "AttributeType": "N"
                }
            ],
            # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
            # You can control read and write capacity independently.
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
        )
        print("Table created successfully!")
    except Exception as e:
        print("Error creating table:")
        print(e)