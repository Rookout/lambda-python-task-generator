from rook.serverless import serverless_rook
import random
import json

tasks = [
  "Deploy my serverless application",
  "Secure the MongoDB instance",
  "Get a cake for John\"s birthday",
  "Improve SEO",
  "Learn how to knit"
]

@serverless_rook
def handler(event, context):
  response = {
    "statusCode": 200,
    "isBase64Encoded": False,
    "headers": { "Access-Control-Allow-Origin": "*" },  # Required for CORS support to work
    "body": json.dumps({ "task": random.choice(tasks) })
  }

  return response