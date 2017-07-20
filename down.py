import requests,time
from bs4 import BeautifulSoup

site = 'http://jandan.net'
page = 181
local = 'img/'
n = 1

def downloadImg(imgUrl,n) :
    ir = requests.get(imgUrl)
    localfile = local + str(n) + '.jpg'
    if ir.status_code == 200:
        open( localfile,'wb').write(ir.content) # The 'wb' means write in file like 101101010


while page > 178 :
    page = page - 1
    url = site + '/pic/page-' + str(page)
    print (url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    imgSrc = soup.findAll('img', {'class': ''})

    for i in imgSrc :
        n = n + 1
        imgUrl = 'http:' + i.get('src')
        downloadImg(imgUrl,n)
    time.sleep(10)
