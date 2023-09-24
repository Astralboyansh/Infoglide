import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def format_input(input_text):
    return "+".join(input_text.split(" "))

def get_google_images_url(query):
    query = format_input(query)

    google_images_url = f'https://www.google.com/search?q={query}&tbm=isch&tbs=isz:m,islt:cl'
    return google_images_url

def get_src_img(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for image in range(1,2,1):
        src = images[image].get('src')
        return(src)

def download_image(image_url, save_path="extracted_img_11.png"):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as image_file:
            image_file.write(response.content)
        print(f"Image downloaded and saved as '{save_path}'")
    else:
        print("Failed to download the image.")
def get_image(inp,path):
    download_image(get_src_img(get_google_images_url(inp)),path)
if __name__=="__main__":

    inp=input()+" hd landscape"
    os.chdir(".")
    path=__file__.split("/")
    path[-1]="name.png"
    path[-2]="content"
    path="/".join(path)
    print(path)
    path=getadd("content/vid_content",)
    print(get_src_img(get_google_images_url(inp)))
    download_image(get_src_img(get_google_images_url(inp)),path)