import json
import boto3
from boto3.dynamodb.conditions import Key

# dynamodb table 선언
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('unho-check-spark-executor-call-db')

# 항목 업데이트 함수
def update_item(event_method, event_count):
    
    response = table.update_item(
        # 기본 키
        Key={
            'method': event_method
        },
        UpdateExpression="SET #pre_count = #pre_count + :val",
        ExpressionAttributeValues={
            ':val': event_count
        },
        ExpressionAttributeNames={
            '#pre_count' : 'count'
        }
    )
    return response
    

def lambda_handler(event, context):

    # Update 함수
    return {
        'statusCode': 200,
        'body': json.dumps(update_item(event["body-json"]["method"],event["body-json"]["count"]))
    }
