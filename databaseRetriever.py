from distutils.command.build import build
import requests
from config.config import base_url, buildApiHeader

# 루트 페이지의 모든 하위 페이지 및 블록을 도는 재귀 함수
# return type [string]: [database_ids]
def getChildrenBlocksRecursively(page_id, database_ids, header):
    url = base_url + f'blocks/{page_id}/children'
    r = requests.get(url, headers=header)

    res = r.json()
    blocks = res['results']
    for block in blocks:
        if block['has_children'] == False:
            if block['type'] == 'child_database':
                database_ids.append(block['id'])

        else:
            getChildrenBlocksRecursively(block['id'], database_ids, header)
    
    return database_ids

# 루트 블록을 넣었을 때 하위의 모든 database id를 반환하는 함수
# main function 에서 사용
def getDatabaseIds(root_id, api_key):
    header = buildApiHeader(api_key)
    ids = []
    res = getChildrenBlocksRecursively(root_id, ids, header)
    return res