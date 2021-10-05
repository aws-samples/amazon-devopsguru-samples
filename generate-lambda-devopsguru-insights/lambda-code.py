import json
import time

def lambda_handler(event, context):

    # Forcing Lambda to respond slowly
    # print('Slow Lambda kicking in for 120 seconds....')
    # time.sleep(120)

    return {
        'statusCode': 200,
        'body': json.dumps('Success from DevOpsGuruSample-Lambda!')
    }
