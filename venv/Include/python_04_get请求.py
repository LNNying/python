import requests
from urllib.parse import urlencode
from urllib import request



url = 'https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/jquery/jquery-1.10.2.min_65682a2.js'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

req = request.Request(url, headers=headers)

reponse = request.urlopen(req)

with open('myJS', 'w+', encoding='utf-8') as file:
    file.write(str(reponse.read().decode()))