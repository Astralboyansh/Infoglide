import news
import image
import gpt
import tts
#import pib


"""news.getrss()
length=news.getnews()
news.get_content()
news.extract()
"""
"""
for i in range(1,10):
    file=news.getadd("content/vid_content/"+str(i),"images",".txt")
    with open(file,"r") as f:
        text=f.read()
    text=text.split("\n")
    for k in range(len(text)):
        image.get_image(text[k][1:-1],news.getadd("content/vid_content/"+str(i),"img"+str(k),".png"))
"""
for i in range(6,10):
    file=news.getadd("content/vid_content/"+str(i),"anim",".txt")
    with open(file,"r") as f:
        text=f.read()
    tts.final_audio(text,news.getadd("content/vid_content/"+str(i),"",""))