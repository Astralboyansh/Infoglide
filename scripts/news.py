import requests
from bs4 import BeautifulSoup
import gpt
import os

def getadd(folder,name,ext):
    path=__file__.split("/")
    path[-1]=str(name)+str(ext)
    path[-2]=str(folder)
    path="/".join(path)
    return path
prompt="i'll call you gpt when referring to you, i am giving you a news article, i want you to increase the readability and paraphrase , to optimise the article for listening but don't summarise or leave out information as all of it is crucial. insert breaks and new lines wherever you think it can increase understanding in speech, mirroring pauses in speech, strictly only identify names of places and objects(sfw) , not absolutely anything else,especially try to avoid images of actual people and their family's, along with the sentiment of image(negative/positive), which will be inserted to increase visual understanding, insert the list index of those items strictly only at start of lines where image can be inserted in the format [image of object/place and sentiment]line  of article where item should be inserted in which you think the images can be added to increase visual understanding,so we can add image at each index. example of format to be followed: [crying little girl- sad]little girl is crying. if no image is associated with the line, no need to add square brackets. the output should strictly follow the format: modified article with readability and images inserted and nothing more: "
file=getadd("content/setup","news",".txt")

def getrss(nfile=file,url = 'https://timesofindia.indiatimes.com/rssfeedstopstories.cms'):
    data = requests.get(url)

    news = BeautifulSoup(data.text, 'xml')
    titles=news.find_all('title')
    links=news.find_all('link')
    image=news.find_all('enclosure')
    with open(nfile,'w') as f:
        for i in range(2,len(titles)):
            text=str(titles[i])
            url=str(links[i+2])
            img=str(image[i-2]).split()
            f.write(str(i-1)+"@~"+text[7:-8]+"@~"+url[6:-7]+"@~"+img[3][5:-3])
            f.write("\n")
def getnews(nfile=file):
    with open(nfile,"r") as f:
            nd=f.read()
            nd=nd.split("\n")
    global length
    length=len(nd)
    for i in range(len(nd)-1):
        nd[i]=nd[i].split("@~")
    for i in range(len(nd)-1):
        newsadd=getadd("content/news",str(i+1),".txt")
        imgadd=getadd("content/news",str(i+1),".png")
        url=nd[i][2]
        nsite=requests.get(url)
        nhtml=BeautifulSoup(nsite.text,'html.parser').find('div',attrs={'id': 'app'}).find('div',attrs={'class':'nonAppView layout_type_2'}).find('div',attrs={'class':'contentwrapper clearfix'}).find('div',attrs={'class':'clearfix rel'}).find('div',attrs={'class':'NvaTO'}).find('div',attrs={'class':'cCU6C innerbody'}).find('div',attrs={'class':'okf2Z'}).find('div',attrs={'class':'JuyWl'}).find('div',attrs={'class':'vSlIC'}).find('div',attrs={'class':'heightCalc'}).find('div',attrs={'data-articlebody':'1'}).find('div',attrs={'class':'_s30J clearfix'})
        with open(newsadd,"w") as f:
            f.write(nd[i][1]+"\n"+str(nhtml.get_text()))
        img_data = requests.get(nd[i][3],stream=True)
        with open(imgadd,'wb') as handler:
            handler.write(img_data.content)
    return len(nd)
def get_content(end,start=1):
    while(start!=end):
        try:
            for i in range(start,end):
                var=i
                file=getadd("content/news",i,".txt")
                with open(file,"r") as f:
                    content=f.read()
                content=content.split("\n")
                title=content[0]
                text=content[1]
                
                modified_text=gpt.cgpt(prompt+text)
                final=title+"\n"+modified_text
                filen=getadd("content/vid_content",i,".txt")
                with open(filen,"w") as f:
                    f.write(final)
                print(str(i)+" done")
            break
        except Exception as e:
                print(e)
                get_content(end,start=var)
                break
        
def extract(length):
    for k in range(1,length):
        file=getadd("content/vid_content",k,".txt")
        with open(file,"r") as f:
            con=f.read()
        con=con.split("\n")
        images=[]
        text=[]
        conn=[]
        for i in range(len(con)-1):
            try:
                if con[i][0]=="[":
                    images.append(con[i])
                    con[i]="[Image]"
                else:
                    text.append(con[i])
                conn.append(con[i])
            except Exception as e:
                pass
        try:
            os.mkdir(getadd("content/vid_content",k,""))
        except:
            pass
        text='\n'.join(text)
        images='\n'.join(images)
        anim='\n'.join(conn)
        filet=getadd("content/vid_content/"+str(k),"text",".txt")
        filei=getadd("content/vid_content/"+str(k),"images",".txt")
        filea=getadd("content/vid_content/"+str(k),"anim",".txt")
        file=[filet,filei,filea]
        filec=[text,images,anim]
        for i in range(len(file)):
            with open(file[i],"w") as f:
                f.write(filec[i])
def extract(length):
    for k in range(1,length):
        file=getadd("content/vid_content",k,".txt")
        with open(file,"r") as f:
            con=f.read()
        con=con.split("\n")
        images=[]
        text=[]
        conn=[]
        for i in range(len(con)-1):
            try:
                if con[i][0]=="[":
                    images.append(con[i])
                    con[i]=".@123."
                else:
                    text.append(con[i])
                conn.append(con[i])
            except Exception as e:
                pass
        try:
            os.mkdir(getadd("content/vid_content",k,""))
        except:
            pass
        text='\n'.join(text)
        images='\n'.join(images)
        anim='\n'.join(conn)
        filet=getadd("content/vid_content/"+str(k),"text",".txt")
        filei=getadd("content/vid_content/"+str(k),"images",".txt")
        filea=getadd("content/vid_content/"+str(k),"anim",".txt")
        file=[filet,filei,filea]
        filec=[text,images,anim]
        for i in range(len(file)):
            with open(file[i],"w") as f:
                f.write(filec[i])

def tts(length):
    for i in range(1,length):
        pass
        

def getmain():
    
    getrss(file)
    length=getnews(file)
    get_content(length)
    extract(length)

