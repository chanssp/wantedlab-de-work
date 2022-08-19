import requests
import pandas as pd
from tableItem import getTableItem
from config.config import base_url, buildApiHeader
    
# return type <tuple>: (table_name, column_list)
def getTableSchema(database_id, header):
    url = base_url + f'databases/{database_id}'
    
    r = requests.get(url, headers=header)
    res = r.json()
    
    # title: array of rich-text objects
    title = res['title'][0]['plain_text']

    # keys: column names of the database
    keys = list(res['properties'].keys())

    return (title, keys)

def getItem(page_id, property_id, header):
    url = base_url + f'pages/{page_id}/properties/{property_id}'

    r = requests.get(url, headers=header)

    res = r.json()
    return res

# return type <tuple>: (table_name, table_rows)
def getTableRows(database_id, schema, header):
    url = base_url + f'databases/{database_id}/query'

    r = requests.post(url, headers=header)
    res = r.json()

    keys = schema[1]
    rows = dict()
    for key in keys:
        rows[key] = []

    # row별로 item 추가해주기
    for row in res['results']:
        page_id = row['id']
        
        for key in keys:
            prop_id = row['properties'][key]['id']
            item = getTableItem(getItem(page_id, prop_id, header))
            rows[key].append(item)
    
    return (schema[0], rows)

# return type <tuple>: (table_name, table_dataframe)
def turnIntoDataFrame(table_info):
    return (table_info[0], pd.DataFrame(table_info[1]))

# 위 모든 변환을 한 flow로 이어주는 함수
# main function 에서 사용
def getDataframeFromDatabase(database_id, api_key):
    header = buildApiHeader(api_key)
    schema = getTableSchema(database_id, header)
    table = getTableRows(database_id, schema, header)
    res = turnIntoDataFrame(table)

    return res
