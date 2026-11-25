import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    user = params.get("user", "Guest")

    body = {
        "project": "AWS Final Cloud Deployment Project",
        "message": f"Hello {user}! Live response from Lambda & API Gateway.",
        "utc_time": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "status": "OK"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body)
    }
