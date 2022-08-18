import requests

api_key = ''
base_url = 'https://api.notion.com/v1/'

with open("./config/credentials.txt", "r") as file:
    api_key = file.read()

header = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json; charset=utf-8',
    'Notion-Version': '2022-06-28'
}


# 루트 페이지의 모든 하위 페이지 및 블록을 돌기위한 함수
def getChildrenBlocksRecursively(page_id, database_ids):
    url = base_url + f'blocks/{page_id}/children'
    r = requests.get(url, headers=header)

    res = r.json()
    blocks = res["results"]
    for block in blocks:
        if block["has_children"] == False:
            if block["type"] == "child_database":
                database_ids.append(block["id"])

        else:
            getChildrenBlocksRecursively(block["id"], database_ids)
    
    return database_ids

def getDatabaseIds(root_id):
    ids = []
    res = getChildrenBlocksRecursively(root_id, ids)
    return res