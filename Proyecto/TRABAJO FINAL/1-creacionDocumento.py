
from bs4 import BeautifulSoup
import urllib.request
import json

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

def replace(string):
    string = string.replace("\n", " ")
    string = string.replace("\r", " ")
    string = string.replace("\t", " ")
    string = string.replace("\x03", " ")    
    string = string.replace("     ", " ")
    string = string.replace("    ", " ")
    string = string.replace("   ", " ")
    string = string.replace("  ", " ")    
    return  string


def GetContentPage(url):
    peli_title = ""
    peli_content = ""
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.body.find("section", class_="movie-text")
    title = section.find("h1", class_="title-detail title-detail-tablet")
    if title:
        peli_title = title.get_text()    
        div = soup.body.find("div", class_="blockout txt")
    if div.p:
        div.p.span.clear()
        peli_content = div.p.get_text()
    
    return peli_title, peli_content
    

links = []    
file_links = open("links.csv","r")        

links = file_links.readlines()

pages = []
pages = links

dic_corpus = {}

for id, page in enumerate(pages):
    print("..."+ str(page))
    doc_title, doc_content = GetContentPage(page) 
    dic_corpus[id] = replace("TITULO: "+doc_title+" SINOPSIS:"+ doc_content).lower()

print(dic_corpus)   


file = open("documents/documentsGen.txt","w")   
file.write(json.JSONEncoder().encode(dic_corpus))
file.close() 