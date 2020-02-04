import json
import boto3

def init():
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
    return(dynamodb)


# Create the DynamoDB table.
def create_table(dynamodb, table_name):
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table


def get_table_object(dynamodb, table_name):
    import boto3

    # Get the service resource.

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table(table_name)
    return table

    # Print out some data about the table.
    # This will cause a request to be made to DynamoDB and its attribute
    # values will be set based on the response.

# Wait until the table exists.
#table.meta.client.get_waiter('table_exists').wait(TableName='users')

def put_item_to_table(table_name):
    table_name.put_item(
    Item={
            'username': 'janeedoe123321',
            #'first_name': 'Jane',
            'last_name': 'Doe',
            #'age': 25,
            #'account_type': 'standard_user',
        }
    )


def hello(event, context):
    a = init()
    table = get_table_object(a, 'users')
    print(table)
    print(put_item_to_table(table))


    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """



