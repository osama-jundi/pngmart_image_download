import requests
from bs4 import BeautifulSoup



sitemap="https://www.pngmart.com/de/sitemap.xml"
request= requests.get(sitemap)
print(request)
html=request.text
soup=BeautifulSoup(html,'html.parser')
answer=soup.find_all("sitemap")
sites=[]
for i in answer:
    ex=i.text.strip()
    exlist=ex.splitlines()
    
    if 'post' in exlist[0]:
        
        sites.append(exlist[0])
#change the "idpage" to download imgs from diffrent page
idpage=0
site_map_1=sites[idpage]
responce=requests.get(site_map_1)
html=responce.text
soup=BeautifulSoup(html,'html.parser')
answer=soup.find_all("loc")
print(responce)

images=[]
for i in answer:
    images.append(i.text)

print(len(images))
for image_url in images:
    print(image_url)
    responce=requests.get(image_url)
    soup=BeautifulSoup(responce.text,"html.parser")
    png_url=soup.find('a',{'class':'download'})['href']
    print(png_url)
    image_title=image_url.split("/")[-1]+"-"+png_url.split("/")[-1]
    print(image_title)
    image=requests.get(png_url)
    #put the path to the file were you wish to download the imgs
    path="ex:/ex/ex/ex/ex/ex/"
    with open(f"{path}{image_title}",'wb') as file:
        file.write(image.content)
    