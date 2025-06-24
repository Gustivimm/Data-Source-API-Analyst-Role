import time
import requests
from Content.api_auth import headers

# If the rate limit exceds API limit, code wait until API allow new rates
def handle_rate_limit(response):
  if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
      if int(response.headers['X-RateLimit-Remaining']) == 0:
          reset_time = int(response.headers['X-RateLimit-Reset'])
          wait_time = reset_time - int(time.time()) + 1
          print(f"Rate limit reached. Waiting {wait_time} seconds...")
          time.sleep(wait_time)


# Create a list of results from pages
def get_paginated_results(url, params={}):
  results = []
  while url:
      response = requests.get(url, headers=headers, params=params)
      handle_rate_limit(response)
      if response.status_code == 200:
        data = response.json()
        results.extend(data if isinstance(data, list) else [data])
        # Next page detection
        if 'next' in response.links:
          url = response.links['next']['url']
          params = {}
        else:
          break
      # Handling error
      else:
        print(f"Error: {response.status_code}, Message: {response.text}")
        break
  return results
