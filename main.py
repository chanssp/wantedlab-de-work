from tableBuilder import getDataframeFromDatabase
from databaseRetriever import getDatabaseIds

# 메인 함수
def main(root, api_key):
    ids = getDatabaseIds(root, api_key)
    dataframes = dict()

    for id in ids:
        df = getDataframeFromDatabase(id, api_key)
        dataframes[df[0]] = df[1]
    
    return dataframes

# 결과를 보기 위한 보조 함수
def printDataframe(dfs):
    keys = list(dfs.keys())

    for key in keys:
        print ('table name:', key)
        print (dfs[key])
        print ('----------------------')

if __name__ == '__main__':
    root = ''
    api_key = ''

    with open('./config/root.txt', 'r') as file:
        root = file.read()

    with open('./config/credentials.txt', 'r') as file:
        api_key = file.read()

    tables = main(root, api_key)

    printDataframe(tables)
