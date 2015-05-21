import urllib.request
from bs4 import BeautifulSoup
import azlyr
lyrics=''
def extractlyrics(link):
    global lyrics
    uri=urllib.request.urlopen(link)
    html=uri.read()
    soup=BeautifulSoup(html)
    
    for div in soup.find_all('div'):
        cls=div.get('class')
        
##        if cls==['col-xs-12', 'col-lg-8', 'text-center']:
##            print('container')
        if cls==None:
            lyrics=str(div)
            
            lyrics=lyrics.replace('<div id="fb-root"></div>','')
            lyrics=lyrics.replace('<div>','')
            lyrics=lyrics.replace('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->','')
            lyrics=lyrics.replace('</div>','')
            lyrics=lyrics.replace('<br>','')
            lyrics=lyrics.replace('<br/>','')
           
            
def lyricfind(name):
    search=azlyr.songsearch(name)
    links=search.give_links()
    if links==[]:
        print("No result found")
        exit(1)
    i=0
    for l in links:
        print(str(i)+"-"+l[0]+"-"+l[1])
        i=i+1
    choice=input("\n Enter choice  ")
    try:
        extractlyrics(links[int(choice)][1])
    except:
        pass
    return lyrics




