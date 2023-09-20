import requests
from bs4 import BeautifulSoup
def getrss():
    url = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'
    data = requests.get(url)

    news = BeautifulSoup(data.text, 'xml')
    titles=news.find_all('title')
    links=news.find_all('link')
    image=news.find_all('enclosure')
    with open('news.txt','w') as f:
        for i in range(2,len(titles)):
            text=str(titles[i])
            url=str(links[i+2])
            img=str(image[i-2]).split()
            f.write(str(i-1)+"@~"+text[7:-8]+"@~"+url[6:-7]+"@~"+img[3][5:-3])
            f.write("\n")
def getnews():
    with open("news.txt","r") as f:
            nd=f.read()
            nd=nd.split("\n")
            
    for i in range(len(nd)-1):
        nd[i]=nd[i].split("@~")
    for i in range(5):
        url=nd[i][2]
        nsite=requests.get(url)
        nhtml=BeautifulSoup(nsite.text,'html.parser').find('div',attrs={'id': 'app'}).find('div',attrs={'class':'nonAppView layout_type_2'}).find('div',attrs={'class':'contentwrapper clearfix'}).find('div',attrs={'class':'clearfix rel'}).find('div',attrs={'class':'NvaTO'}).find('div',attrs={'class':'cCU6C innerbody'}).find('div',attrs={'class':'okf2Z'}).find('div',attrs={'class':'JuyWl'}).find('div',attrs={'class':'vSlIC'}).find('div',attrs={'class':'heightCalc'}).find('div',attrs={'data-articlebody':'1'}).find('div',attrs={'class':'_s30J clearfix'})
        with open(nd[i][0]+".txt","w") as f:
            f.write(nd[i][1]+"\n"+str(nhtml.get_text()))
        img_data = requests.get(nd[i][3],stream=True)
        with open(nd[i][0], 'wb') as handler:
            handler.write(img_data.content)

getrss()
getnews()