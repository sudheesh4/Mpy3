import urllib.request
from bs4 import BeautifulSoup

class songsearch:
    def __init__(self,query):
        
        query=query.replace(" ","+")
        self.url='http://search.azlyrics.com/search.php?q='+query+'&p=1&w=songs'
        self.error=False
        self.html=''
        self.links=[]
        self.get_html()
        if self.error:
            return
        self.soup=BeautifulSoup(self.html)
        
        self.get_links()
    def get_html(self):
        i=0
        maxi=10
        print("conecting")
        while i<maxi:
            try:
                uri=urllib.request.urlopen(self.url)
            except:
                print("again")
                i=i+1
                continue
            break
        if i==maxi:
            self.error=True
            print("Cant connect")
            return
        
        print("conneccted")
        self.html=uri.read()
    def get_links(self):
        print("extracting links")
        for link in self.soup.find_all('a'):
            txt=link.get('href')
            txt=str(txt)
            if txt[0:31]=='http://www.azlyrics.com/lyrics/':
                tempsoup=BeautifulSoup(str(link))
                for name in tempsoup.find_all('b'):
                    name=str(name)
                name=name.replace('<b>','')
                name=name.replace('</b>','')
                self.links.append((name,txt))
                
    def give_links(self):
        return self.links
            
            

        
