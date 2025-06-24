from Content.pagination_and_limits import get_paginated_results
import requests
from Content.api_auth import api_url, headers

# Getting username
user = input("Enter the GitHub username (identical to GitHub): ")
# Getting user repos
repos_url = f"{api_url}/users/{user}/repos"
repos = get_paginated_results(repos_url)
# Listing user repos
print("Repos:", [repo['name'] for repo in repos])

# Getting contents of a Repo Folder
repo_name = input("Enter the GitHub repo name (identical to GitHub): ")
contents_url = f"{api_url}/repos/{user}/{repo_name}/contents/dados"
contents = requests.get(contents_url, headers=headers)
# Showing files
if contents.status_code == 200:
  files_info = contents.json()
  for item in files_info:
    print("File:", item['name'])
# Handling error
else:
  print("Failed to fetch repo contents")

# Getting and printing (count) commits
commits_url = f"{api_url}/repos/{user}/{repo_name}/commits"
commits = get_paginated_results(commits_url)
print("Total commits fetched:", len(commits))