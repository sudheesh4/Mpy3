from emp3 import *
from common import *
from mssgboxes import *
from tkinter import *
root=Tk()

root.withdraw()
def startemp3():
    fckh=""
    url_names=[]
    link=[]
    temp=[]
    d=SOMEMSG(root,"Enter name of song",temp)
    root.wait_window(d.top)
    name=temp[0]
    temp=[]
    name=name.replace(" ","-")

    tempfn="DEFAULT"
 
    name=name.replace(' ','_')
    s=song_emp3(name)

    link=s.givelinks()
    url_names=s.givenames()
    
    if len(link)==0:
        ms=MSSG(root,"No such song found on site! :/")
       # print("No such song found on site! :/")
        exit()

   # auto_down(tempfn,url_names,link)   
    manual_down(tempfn,url_names,link)
    
         
    

#startskull()
