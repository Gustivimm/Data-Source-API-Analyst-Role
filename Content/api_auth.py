# Getting personal token
def token():
    TOKEN = "your_personal_token_here"
    return TOKEN


def api_url():
    GITHUB_API_URL = "https://api.github.com"
    return GITHUB_API_URL


def headers():
    TOKEN = token()
    HEADERS = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }