import json

# object = property_item: unnested
# checkbox, created_time, email, last_edited_time, number, phone_number, url

# object = property_item: nested
# created_by, date, files, formula, last_edited_by, multi_select, select, status 

# object = list
# people, relation, rich_text, title, 

# 구조 바꾸기: dict => ??
unnested = {
    "checkbox": 1,
    "created_time": 1,
    "email": 1,
    "last_edited_time": 1,
    "number": 1,
    "phone_number": 1,
    "url": 1
}

# return type <boolean>
# 빈 값인지 확인하는 함수
def isEmptyCell(item):
    # property_item object
    if item["object"] == "property_item":
        type = item["type"]
        if item[type] is None:
            return True

        return False
    
    # list object
    else: 
        if len(item["results"]) == 0:
            return True

        return False

# 빈 값이 아닐 때, 테이블의 값을 가져오는 함수
def getPropertyItem(item):
    # 빈 셀일 경우 ''로 테이블 채움
    if isEmptyCell(item):
        return ''
    
    if item["object"] == "property_item":
        type = item["type"]

        # linear type인 경우
        if item["type"] in unnested: 
            return item[type]
        # nested dictionary의 경우
        else:
            return nested_item(item)
    
    else:
        return list_people(item["results"])

# =========== for nested dictionary type ===========
def nested_item(item):
    type = item["type"]
    if (type == 'created_by') or (type == 'last_edited_by') or (type == 'select') or (type == 'status'):
        return propertyItem_name(item[type])
    elif type == 'date':
        return propertyItem_date(item[type])
    elif type == 'files':
        return propertyItem_files(item[type])
    elif type == 'formula':
        return propertyItem_formula(item[type])
    elif type == 'multi_select':
        return propertyItem_multi_select(item[type])
    else:
        print (type)
        return "UNEXPECTED PROPERTY ITEM TYPE"

def propertyItem_name(item):
    return item["name"]

def propertyItem_date(date):
    ret = ""
    if date["start"] is not None:
        ret = ret + date["start"]
    
    if date["end"] is not None:
        ret = ret + ' > ' + date["end"]
    
    return ret

def propertyItem_files(files):
    ret = ""
    length = len(files)
    for i in range(length):
        ret += files[i]["name"]
        if i != (length - 1):
            ret += ', '
    
    return ret

def propertyItem_formula(formula):
    # 추가작업: 타입 읽어서 해당 타입만 딱 변환하기
    return json.dumps(formula)  

def propertyItem_multi_select(selects):
    ret = ''
    length = len(selects)
    for i in range(length):
        ret += selects[i]["name"]
        if i != (length - 1):
            ret += ', '
    
    return ret
# =========== for nested dictionary type ===========

# =========== for list type ===========
def list_people(result):
    ret = ''
    length = len(result)

    for i in range(length):
        obj = result[i]
        item = listItemSwitch(obj)
        ret += item
        if i != (length - 1):
            ret += ', '
    
    return ret


def listItemSwitch(obj):
    type = obj["type"]
    if type == "people":
        return obj[type]["name"]
    elif type == "relation":
        return obj[type]["id"]
    elif type == "rich_text" or type == "title":
        return obj[type]["plain_text"]
    else:
        print(type)
        return "UNEXPECTED LIST TYPE"

# =========== for list type ===========