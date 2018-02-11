from chalice import Chalice, Response
import boto3
import botocore
import logging
from os import environ
import random

app = Chalice(app_name=environ['APP_NAME'])
ddb_table = environ['DYNAMO_TABLE']
logger = logging.getLogger()

client = boto3.client('dynamodb', region_name=environ['AWS_DEFAULT_REGION'])


@app.route('/')
def index():
    url = environ['SITE_FALLBACK']
    return Response(
        status_code=302,
        body='',
        headers={'Location': url})


@app.route('/fortune', methods=['GET'])
def fortune():
    fortune_text = 'Do or do not, there is no try!'
    record = 0
    try:
        # Get count of items in DDB Table. ID == table_count
        # Per AWS, this can take 6 hours to update. 
        table_info = client.describe_table(
            TableName=ddb_table
        )
        table_count = table_info['Table']['ItemCount']
        # Pick a random number in the range of the table
        # and then retrieve that record.
        record = str(random.choice(range(1, table_count + 1)))
        response = client.get_item(
            TableName=ddb_table,
            Key={
                'fid': {'S': record}
            },
            AttributesToGet=[
                'fortune',
            ]
        )
        fortune_text = response['Item']['fortune']['S']
    except botocore.exceptions.ClientError as client_error:
        logger.error('ClientError: {}'.format(client_error))
        logger.error('')
    except KeyError as key_error:
        logger.error('Error getting table count or fortune.')
        logger.error('key_error: {}'.format(key_error))
        logger.error('table_info: {}'.format(table_info))
    return {"id": record, "fortune": fortune_text}
