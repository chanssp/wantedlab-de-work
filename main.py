from tableBuilder import getDataframeFromDatabase
from databaseRetriever import getDatabaseIds

# 메인 함수
def main(root):
    ids = getDatabaseIds(root)
    dataframes = dict()

    for id in ids:
        df = getDataframeFromDatabase(id)
        dataframes[df[0]] = df[1]
    
    return dataframes

# 결과를 보기위한 보조 함수
def printDataframe(dfs):
    keys = list(dfs.keys())

    for key in keys:
        print ('table name:', key)
        print (dfs[key])
        print ('----------------------')

if __name__ == '__main__':
    root = ''

    with open('./config/root.txt', 'r') as file:
        root = file.read()

    tables = main(root)

    printDataframe(tables)
