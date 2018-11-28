from rook.serverless import serverless_rook
import random

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
    "status": 200,
    "isBase64Encoded": False,
    "headers": { "Access-Control-Allow-Origin": "*" },  # Required for CORS support to work
    "body": { "task": random.choice(tasks) }
  }

  return response