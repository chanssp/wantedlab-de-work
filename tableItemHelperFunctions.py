def isEmptyCell(item):
    # property_item object
    if item['object'] == 'property_item':
        type = item['type']
        if item[type] is None:
            return True

        return False
    
    # list object
    else: 
        if len(item['results']) == 0:
            return True

        return False

# <all possible page property types>

# object = property_item: unnested
# checkbox, created_time, email, last_edited_time, number, phone_number, url

# object = property_item: nested
# created_by, date, files, formula, last_edited_by, multi_select, select, status 

# object = list
# people, relation, rich_text, title

# =========== helper functions for nested dictionary type ===========
def property_item(item):
    type = item['type']
    
    if type == 'created_by' or type == 'last_edited_by' or type == 'select' or type == 'status':
        return propertyItem_name(item[type])
    elif type == 'date':
        return propertyItem_date(item[type])
    elif type == 'files':
        return propertyItem_files(item[type])
    elif type == 'formula':
        return propertyItem_formula(item[type])
    elif type == 'multi_select':
        return propertyItem_multi_select(item[type])
    else:  # unnested_dictionay
        return item[type]

def propertyItem_name(item):
    return item['name']

def propertyItem_date(date):
    ret = ''
    if date['start'] is not None:
        ret = ret + date['start']
    
    if date['end'] is not None:
        ret = ret + ' > ' + date['end']
    
    return ret

def propertyItem_files(files):
    ret = ''
    length = len(files)
    
    for i in range(length):
        ret += files[i]['name']
        if i != (length - 1):
            ret += ', '
    
    return ret

def propertyItem_formula(formula):
    type = formula['type']
    return formula[type]

def propertyItem_multi_select(selects):
    ret = ''
    length = len(selects)

    for i in range(length):
        ret += selects[i]['name']
        if i != (length - 1):
            ret += ', '
    
    return ret
# ===================================================================

# ====================== helper for list type =======================
def list_item(result):
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
    type = obj['type']
    if type == 'people':
        return obj[type]['name']
    elif type == 'relation':
        return obj[type]['id']
    elif type == 'rich_text' or type == 'title':
        return obj[type]['plain_text']
    else:
        print(type)
        return 'UNEXPECTED LIST TYPE'
# ===================================================================
