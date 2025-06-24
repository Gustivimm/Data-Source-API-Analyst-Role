import requests
from Content.api_auth import api_url

def simulate_unauthorized():
  # Creating wrong headers (as simulation)
  wrong_headers = {
    "Authorization": "Bearer WRONG_TOKEN",
    "Accept": "application/vnd.github+json"
  }
  # Applying wrong headers (as simulation)
  r = requests.get(f"{api_url}/user", headers=wrong_headers)
  # Handling wrong headers (as simulation)
  if r.status_code == 401:
    print("401 Unauthorized. Cause: Invalid token.")

simulate_unauthorized()