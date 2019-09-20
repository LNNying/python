import requests
from urllib.parse import urlencode
from urllib import request



uploads = {
    "ad_cb": "",
    "as_server": 'bilibili',
    "area": 0,
    "client_version": "",
    "event": "show",
    "id": 265703,
    "idx": 1,
    "is_ad": 0,
    "is_visible": 1,
    "load_ts": 1963155456954,
    "mid": "7712616",
    "resource_id": 31,
    "server_type": 0,
    "src_id": 32,
    "ts": 1963162559293
}
url = 'https://cm.bilibili.com/cm/api/fees/pc'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
data = urlencode(uploads).encode('utf-8')

req = request.Request(url, data=data, headers=headers)

reponse = request.urlopen(req)

print(req.headers)

print(reponse.read().decode("utf-8"))
