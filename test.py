def lambda_handler(event, context):
    printt("In lambda handler")
    
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "mate"
    }
    
    return resp
