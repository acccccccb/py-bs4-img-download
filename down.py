import requests,time
from bs4 import BeautifulSoup

site = 'http://jandan.net'
page = 181
local = 'img/'
n = 1
headers={ 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Referer': 'http://www.zhihu.com/',
'Content-Length': '154',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
'Accept-Encoding': 'gzip, deflate, sdch',
'Host':' www.zhihu.com',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
'Content-Type': 'application/x-www-form-urlencoded',
'Connection':' keep-alive'
}

# 保存图片函数
def downloadImg(imgUrl,n) :
    ir = requests.get(imgUrl)
    localfile = local + str(n) + '.jpg'
    if ir.status_code == 200:
        open( localfile,'wb').write(ir.content) # The 'wb' means write in file like 101101010

# 翻页循环
while page > 178 :
    page = page - 1
    url = site + '/pic/page-' + str(page)
    print (url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    imgSrc = soup.findAll('img', {'class': ''})
    # 将获取获取图片链接
    for i in imgSrc :
        n = n + 1
        imgUrl = 'http:' + i.get('src')
        downloadImg(imgUrl,n)
    time.sleep(10)
