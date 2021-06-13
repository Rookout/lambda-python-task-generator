from rook.serverless import serverless_rook
import urllib.request, urllib.parse, url
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
  random = get_random(0, 4)
  return build_response(event, context, random)


def build_response(event, context, random):
  headers = event["headers"] if "headers" in event else {}
  if "x-from" in headers and headers["x-from"] == "e2e-test":
    print("E2E Test just triggered this function")

  return {
    "statusCode": 200,
    "isBase64Encoded": False,
    "headers": { "Access-Control-Allow-Origin": "*" },  # Required for CORS support to work
    "body": json.dumps({ "task": tasks[random] })
  }


def get_random(min, max):
  values = {
    "col": "1",
    "num": "1",
    "base": "10",
    "format": "plain",
    "min": "{}".format(min),
    "max": "{}".format(max)
  }
  data = urllib.parse.urlencode(values)
  response = urllib.request.urlopen("https://www.random.org/integers/?{values}".format(values=data))
  random = response.read()
  
  return int(random.strip())
