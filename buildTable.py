import requests
import json
import pandas as pd

from utils import getPropertyItem

api_key = ''
base_url = 'https://api.notion.com/v1/'

with open("./config/credentials.txt", "r") as file:
    api_key = file.read()

header = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json; charset=utf-8',
    'Notion-Version': '2022-06-28'
}

# class TableBuilder:
#     header = ''
#     baseUrl = ''

#     def __init__(self, header, url):
#         self.header = header
#         self.baseUrl = url
    
# return type <tuple>: (table_name, column_list)
def getTableSchema(database_id):
    url = base_url + f'databases/{database_id}'
    
    r = requests.get(url, headers=header)
    res = r.json()
    
    # title: array of rich-text objects
    title = res["title"][0]["plain_text"]

    # keys: column names of the database
    keys = list(res["properties"].keys())

    return (title, keys)

def getItem(page_id, property_id):
    url = base_url + f'pages/{page_id}/properties/{property_id}'

    r = requests.get(url, headers=header)

    # types에 있는 파일과 같은 형태
    res = r.json()
    return res

# return type <tuple>: (table_name, table_rows)
def getTableRows(database_id, schema):
    url = base_url + f'databases/{database_id}/query'

    r = requests.post(url, headers=header)
    res = r.json()

    keys = schema[1]
    rows = dict()
    for key in keys:
        rows[key] = []

    # 테이블 row별 처리
    for row in res["results"]:
        page_id = row["id"]
        # print(page_id)

        for key in keys:
            prop_id = row["properties"][key]["id"]
            # item = getItem(page_id, prop_id)
            
            item = getPropertyItem(getItem(page_id, prop_id))
            
            rows[key].append(item)
        
        # print(row["properties"])
    
    return (schema[0], rows)

# return type <tuple>: (table_name, table_dataframe)
def turnIntoDataFrame(table_info):
    return (table_info[0], pd.DataFrame(table_info[1]))

# 위 모든 변환을 한번에 하는 함수
def getDataframeFromDatabase(database_id):
    schema = getTableSchema(database_id)
    table = getTableRows(database_id, schema)
    res = turnIntoDataFrame(table)

    return res
