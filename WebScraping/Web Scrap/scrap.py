import requests
from bs4 import BeautifulSoup

def WebScrap():
    res=requests.get('https://www.worldometers.info/coronavirus/')
    if(res.status_code!=200):
        return {'message': 'Server error'}
    soup=BeautifulSoup(res.text,'html.parser')
    print(soup)
    return {"message": "From scrap"}