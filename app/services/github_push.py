import httpx
from dotenv import load_dotenv
load_dotenv()
import os
def push_comment(url:str,messsage:str):
    url_split=url.split('/')
    OWNER=url_split[3]
    REPO=url_split[4]
    PR_NUMBER=url_split[6]
    try:
        TOKEN = os.getenv("GITHUB_TOKEN")
        # OWNER = "balajiraparti"
        # REPO = "balajiraparti"
        # PR_NUMBER = 3

        url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{PR_NUMBER}/comments"

        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json"
        }

        data = {
            "body": messsage
        }

        response = httpx.post(url, headers=headers, json=data)
        print(response.json())
    except:
        print("An excpetion occured while send http post request")