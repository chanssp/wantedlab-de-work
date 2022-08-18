from buildTable import getDataframeFromDatabase
from databaseGetter import getDatabaseIds

if __name__ == "__main__":
    root = ''

    with open("./config/root.txt", "r") as file:
        root = file.read()

    ids = getDatabaseIds(root)
    print(ids)

    # df를 array[tuple]로 저장해서 반환
    for id in ids:
        df = getDataframeFromDatabase(id)
        
        print(df[0])
        print('----------')
        print(df[1])
        print('==============')