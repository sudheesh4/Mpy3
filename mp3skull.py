import datetime
import urllib.request
import os
import sys
from bs4 import BeautifulSoup

def filtermp3(link): 
    mp3=[]
    for l in link:
        if l[len(l)-4:]=='.mp3':
            #print(l)
            mp3.append(l)
    return mp3
class song_mp3skull:
    def __init__(self,name,fckh):
        self.name=name
        self.url="http://mp3skull.com/search_db.php?q="+name+"&fckh="+fckh
        self.html=''
        #print(self.url)
        self.get_html()
        self.soup=BeautifulSoup(self.html)
        self.links=[]
        self.urlnames=[]
        #print(self.url)
        self.get_links()

    def get_html(self):
        i=0
        maxi=100
        print("Connecting to site..")
        while i<maxi:
            try:
                uri=urllib.request.urlopen(self.url)
            except:
                print("Trying again..")
                i=i+1
                continue
            break
        if i==maxi:
            print("Not able to connect!Try Again later:/")
            exit()
        print('connected!')
            
        self.html=uri.read()

    def get_links(self):
        print("Parsing links")
        for link in self.soup.find_all('a'):
            
            txt=link.get('href')
            self.links.append(txt)
        i=1
        self.links=filtermp3(self.links)
        for link in self.soup.find_all('b'):
            link=str(link)
            link=link[3:len(link)-4]
            if link[len(link)-3:] == "mp3":
                link=str(i)+"->"+link
                self.urlnames.append(link)
                i=i+1
                #print(link)


    def savetofile(self):
        txt=" "       
    def givelinks(self):
        return self.links
    def givenames(self):
        return self.urlnames


def getfckh():  
    try:
        htm=urllib.request.urlopen('http://mp3skull.com/').read()
        s=BeautifulSoup(htm)
        
        for inp in s.find_all('input'):
            nm=inp.get('name')

            if nm=='fckh':
                
                fckh=inp.get('value')
                open('link.txt','w').write(fckh)
                return
    except:
        
        print("something!")
    return
