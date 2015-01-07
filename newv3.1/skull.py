from mp3skull import *
from common import *
from mssgboxes import *
from tkinter import *
root=Tk()

root.withdraw()
def startskull():
    fckh=""
    url_names=[]
    link=[]
    get_fckh=threading.Thread(target=getfckh)
    get_fckh.start()
    temp=[]
    d=SOMEMSG(root,"Enter name of song",temp)
    root.wait_window(d.top)
    name=temp[0]
    temp=[]
    name=name.replace(" ","-")
##    d=SOMEMSG(root,"Save as ?",temp)
##    root.wait_window(d.top)
##    tempfn=temp[0]
##
####    tempfn=input('Save as?\n')
##    try:
##        fileop=open(tempfn,'w')
##    except:
##        ms=MSSG(root,"INVALID FILE NAME ! Giving Name default.mp3")
##        tempfn="default.mp3"
##    finally:
##        fileop.close()
    tempfn="DEFAULT"
    get_fckh.join()
    
    
    fckh=open('link.txt','r').read()
    s=song_mp3skull(name,fckh)

    link=s.givelinks()
    url_names=s.givenames()
    
    if len(link)==0:
        ms=MSSG(root,"No such song found on site! :/")
       # print("No such song found on site! :/")
        exit()

   # auto_down(tempfn,url_names,link)   
    manual_down(tempfn,url_names,link)
    
         
    

#startskull()
