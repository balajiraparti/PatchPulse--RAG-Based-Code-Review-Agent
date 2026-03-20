import httpx
import os
# import dotenv as dt
# dt.load_dotenv()
# TOKEN = os.getenv("GITHUB_TOKEN")



def get_code_changes(OWNER:str,REPO:str,PR_NUMBER:str,TOKEN:str):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{PR_NUMBER}/files"
    response = httpx.get(url, headers=headers)
    changes=[]
    files = response.json()
    if response.status_code != 200:
        raise Exception(f"GitHub API Error: {response.text}")
    for f in files:
     
        changes.append(f"file: {f.get('filename')},\n status:{f.get('status')},\n Additions:{f.get('additions')},\n Deletions:{f.get('deletions')}")
        if f.get("patch"):
            changes.append(f"\n patch:{f.get('patch')}")
    return "".join(changes)

def get_patches(url:str,TOKEN:str):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    url_split=url.split('/')
    OWNER=url_split[3]
    REPO=url_split[4]
    PR_NUMBER=url_split[6]
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{PR_NUMBER}/files"
    response = httpx.get(url, headers=headers)
    patch=""
    files = response.json()

    for f in files:
        if f.get("patch"):
            patch+=f"\n patch:{f.get('patch')}"
    return patch