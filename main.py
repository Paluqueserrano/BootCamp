import urllib3
import json
def get_data():
    http = urllib3.PoolManager()
    url = "https://cloud.iexapis.com/stable/stock/tsla/previous?token=<pk_56ee13d1359e4c2d8ce2898fc7f5beda>"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values
get_data()