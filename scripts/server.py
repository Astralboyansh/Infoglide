def getadd(folder,name,ext):
    path=__file__.split("/")
    path[-1]=str(name)+str(ext)
    path[-2]=str(folder)
    path="/".join(path)
    return path

categories=["index","world","Technology","sports","science","pib","lifestyle","india","business","environment","entertainment","contact","single"]
for k in categories:
    file=getadd("website",k+"1",".html")
    with open(file,"r") as f:
        web=f.read()
    web=web.split("@123")
    imgvar=1
    headlinevar=1
    textvar=1
    filevar=1
    videovar=1
    audiovar=1
    for i in range(len(web)):
        if web[i]=='0':
            con=getadd("content/news",imgvar,".png")
            print(web[i])
            web[i]=con
            print(web[i])
            if imgvar<=35:
                imgvar+=1
            else:
                imgvar=1
        if web[i]=='1':
            con=getadd("content/vid_content/"+str(textvar),"text",".txt")
            with open(con,"r") as f:
                text=f.read().split("\n")
            text=text[1:]
            text=''.join(text)
            print(web[i])
            web[i]=text
            print(web[i])
            if textvar<=35:
                textvar+=1
            else:
                textvar=1
        if web[i]=='2':
            con=getadd("content/vid_content",headlinevar,".txt")
            with open(con,"r") as f:
                text=f.read().split("\n")
            with open(con,"r") as f:
                text=f.read().split("\n")
            text=text[0]
            print(web[i])
            web[i]=text
            print(web[i])
            if headlinevar<=35:
                headlinevar+=1
            else:
                headlinevar=1
        if web[i]=='3':
            con=getadd("content/output","output",".mp4")
            web[i]=str(con)

        if web[i]=='4':
            con=getadd("content/vid_content/1","output2",".mp3")
            web[i]=str(con)

        if web[i]=='5':
            con=getadd("website",filevar,".html")
            print(web[i])
            web[i]=con
            print(web[i])
            if filevar<=35:
                filevar+=1
            else:
                filevar=1

web=''.join(web)
file=getadd("website","single",".html")
with open(file,"w") as f:
    f.write(web)

