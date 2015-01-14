##import datetime
##import socket
##import socks
##
##socks.set_default_proxy(socks.SOCKS5, "localhost",9150)
##socket.socket = socks.socksocket
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
class song_emp3:
    def __init__(self,name):
        self.name=name
        self.url="http://emp3world.com/search/"+name+"_mp3_download.html"
        self.html=''
        #print(self.url)
        self.get_html()
        self.soup=BeautifulSoup(self.html)
        self.links=[]
        self.urlnames=[]
        #print(self.url)
        self.get_links()
        self.error=False

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
            self.error=True
            print("Not able to connect!Try Again later:/")
            
        print('connected!')
            
        self.html=uri.read()

    def get_links(self):
        print("Parsing links")
        for link in self.soup.find_all('a'):
            
            txt=link.get('href')
            self.links.append(txt)
            
        i=1
        self.links=filtermp3(self.links)
        for link in self.soup.find_all('span'):
            txt=link.get('id')
            if txt=='song_title':
                link=str(link)
                link=link.replace('<span id="song_title">','  ')
                link=link.replace('</span>','  ')
                self.urlnames.append(link)
##        index=0
##        for link in self.soup.find_all('div'):
##            txt=link.get('class')
##            print(link)
##            input()
##            if txt=='song_size':
##                link=str(link)
##                link=link.replace('<div class="song_size">',' ')
##                link=link.replace('</div>',' ')
##                self.urlnames[index]=self.urlnames[index]+"-"+link
##                print(self.urlnames[index])
##                index=index+1
                
    def givelinks(self):
        return self.links
    def givenames(self):
        return self.urlnames



