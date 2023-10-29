import pdf
import summariser
import tts
import anim
import image

file=input()
pdf.pdf(file)
summariser.summarise(file)
with open(str(file)+"1.txt",'r') as f:
    text=f.read()
    text=text.split('\n')
    images=text[-1]
    text=text[:-3]
    text='\n'.join(text)
    tts.final_audio(text)
    print("Audio Generated!")
images=images.split()
for i in images:
    image.get_image(i,"images/"+i+".png")
anim.anim()