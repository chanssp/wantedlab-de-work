base_url = 'https://api.notion.com/v1/'

def buildApiHeader(api_key):
    return {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json; charset=utf-8',
        'Notion-Version': '2022-06-28'
    }
