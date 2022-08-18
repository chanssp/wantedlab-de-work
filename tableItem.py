from tableItemHelperFunctions import isEmptyCell, property_item, list_item

# 빈 값이 아닐 때, 테이블의 값을 가져오는 함수
def getTableItem(item):
    # 빈 셀일 경우 ''로 테이블 채움
    if isEmptyCell(item):
        return ''
    
    if item['object'] == 'property_item':
        return property_item(item)
    else:
        return list_item(item['results'])

