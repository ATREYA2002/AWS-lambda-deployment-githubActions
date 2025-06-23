import json

def lambda_handler(event, context):
    """
    Sample Lambda function that returns a simple response.
    """
    print("Received event:", json.dumps(event))

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda!",
            "input": event
        })
    }
    
    return response


