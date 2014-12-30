from mp3skull import *
from common import *
def startskull():
    fckh=""
    url_names=[]
    link=[]
    get_fckh=threading.Thread(target=getfckh)
    get_fckh.start()
    name=input("Enter name of song  ")
    name=name.replace(" ","-")
    tempfn=input('Save as?\n')
    try:
        fileop=open(tempfn,'w')
    except:
        print("INVALID FILE NAME ! Giving Name default.mp3")
        tempfn="default.mp3"
    finally:
        fileop.close()
    get_fckh.join()
    fckh=open('link.txt','r').read()
    s=song_mp3skull(name,fckh)
    link=s.givelinks()
    url_names=s.givenames()
    
    if len(link)==0:
        print("No such song found on site! :/")
        exit()

   # auto_down(tempfn,url_names,link)   
    manual_down(tempfn,url_names,link)
    
         
    

startskull()
