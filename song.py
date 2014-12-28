import urllib.request
import sys
import os
from bs4 import BeautifulSoup
from download import *
import datetime
fckh=""
def filtermp3(link):
    mp3=[]
    for l in link:
        if l[len(l)-4:]=='.mp3':
            #print(l)
            mp3.append(l)
    return mp3
class song:
    def __init__(self,name):
        self.name=name
        self.url="http://mp3skull.com/search_db.php?q="+name+"&fckh="+fckh
        self.html=''
        #print(self.url)
        self.get_html()
        self.soup=BeautifulSoup(self.html)
        self.links=[]
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
            
        self.html=uri.read()

    def get_links(self):
        print("Parsing links")
        for link in self.soup.find_all('a'):
            txt=link.get('href')
            self.links.append(txt)
    def savetofile(self):
        txt=" "
        self.links=filtermp3(self.links)

        
    def givelink(self):
        return self.links
def getfckh():
    tod=str(datetime.date.today())+'\n'
    
    global fckh
    try:
        f=open('link.txt','r')
        for templ in f:
            break
        las=templ

        f.close()
        
    except:
        las=''
    if las==tod:

        fk=open('link.txt','r')
        for l in fk:
            t=l

        fckh=t

        fk.close()
        

        return
    htm=urllib.request.urlopen('http://mp3skull.com/').read()
    s=BeautifulSoup(htm)
    
    for inp in s.find_all('input'):
        nm=inp.get('name')

        if nm=='fckh':
            
            fckh=inp.get('value')
            open('link.txt','w').write(str(datetime.date.today())+'\n'+fckh)
            return
    return
def startm():    
    get_fckh=threading.Thread(target=getfckh)
    get_fckh.start()
    name=input("Enter name of song  ")
    name=name.replace(" ","-")
    get_fckh.join()
    s=song(name)
    s.savetofile()
    link=[]
    link=s.givelink()
    #link=filtermp3(link)
    if len(link)==0:
        print("No such song found on site! :/")
        exit()
    print("Trying First link! ")    
    for i in range(0,len(link)):
        uri=link[0]
        
        uri=uri.replace(" ","%20")#as all space are replaced by %20 while requesting!no whitepace!
        
        j=downsome(uri)
        if j=='404':
            print("Link "+str(i+1)+" Failed! Trying Next")
            continue
        print("DOWNLOADED!")
        break
    if i==len(link):
        print("COULD'NT DOWNLOAD! SORRY! :/")
         
    


