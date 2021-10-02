import json
from google.cloud import storage

def chart(request):
  response = {}
  return json.dumps(response)

def get_rate(request):
  storage_client = storage.Client()
  bucket_name = "get-technical"
  
