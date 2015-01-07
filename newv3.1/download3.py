
import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "localhost",9150)
socket.socket = socks.socksocket
import urllib.request
import sys
import os
import time
import threading
from tkinter import *
import tkinter.ttk as ttk
re=None
newsize=0
notr=7
pauseint=0
pauseflag=False
def compl():
    k=0
    for i in range(0,7):
        k=k+totc[i]
    return k
        
def guiclt(goturi,gotname):
    def myexit():
        pass
    try:
        root=Tk()
        root.title('downloader')
        #root.protocol("WM_DELETE_WINDOW", myexit)
        lab=Label(root,text="Wait...",fg="red")
        per=Label(root,text="Please Wait..",fg="blue")
        
        pause=Button(root,text="PAUSE")
        
        pb_hd = ttk.Progressbar(root, orient='horizontal', mode='determinate')
        
        pb_hd.pack(expand=True)
        
        pb_hd["maximum"] = 100
        
        pb_hd['value']=0
        
        lab.pack()
        per.pack()
        def pauseplay(event):
            global pauseint,pauseflag
            if pauseint==0:
                pauseflag=True
                pauseint=1
                pause['text']='Play'
                time.sleep(0.5)
            else:
                pauseflag=False
                pause['text']='Pause'
                pauseint=0
                time.sleep(0.5)
        pause.bind('<Button-1>',pauseplay)
        pause.pack()
        def printgui(text,k):
            text=text
            k['text']=text
            print(text)
        def reqfunc(a,b):
            global re
            re=urllib.request.Request(a)
        class downloadfile:
            def __init__(self,uri):
                self.maxi=13
                i=0
                self.error=False
                self.size=0
                self.filename=''
                self.parts={}
                self.chunk=0
                self.uri=uri
                printgui("Connecting..",lab)
                while i<self.maxi:
                    try:
                        self.url=urllib.request.urlopen(uri)
                    except:
                        i=i+1
                        print(i)
                        continue
                    break
                if i==self.maxi:
                    printgui("Umm something unexpected happened!:/",lab)
                    
                    self.error=True
                    return
                printgui("Connected",lab)

            def namesize(self,tempn):
               # self.filename=input("Save as ? \n")
                global notr
                self.filename=tempn
                try:
                    self.size=int(self.url.getheader('Content-Length',None))
                except:

                    printgui("No file found here!._.",lab)
                    self.error=True
                    return
                self.chunk=int(self.size/notr)
            def downl(self,start,randomargument):
                req=None
                global re,totc,pauseflag,nosut
                i=0
                req=re
                st=start
                en=int((start+self.chunk))
                dconst=en
                self.parts[start]=b''

                
                while i<self.maxi:
                    try:
                        req.headers['Range']='bytes=%s-%s'% (st,en)
                        
                        req.headers['User-agent']='Mozilla/5.0'
                    except:
                        i=i+1
                        continue

                    break

                if i==self.maxi:
                    printgui("Bad Header!:/",lab)
                    self.error=True
                    return
                i=0
                printgui("Requesting",lab)
                while i<self.maxi:
                    if pauseflag:
                        
                        continue
                    
                    try:
                        f=urllib.request.urlopen(req)
                    except:
                        i=i+1
                        continue
                    break
                if i==self.maxi:
                    printgui("No response!:/",lab)
                    self.error=True
                    return
                global newsize
                newchunk=int(self.chunk/3)
                printgui("Reading",lab)
                tempfl=1
                while True:
                    if pauseflag:
                        
                        continue
                    
                    tempchnk=f.read(newchunk)

                    newsize=newsize+len(tempchnk)
                    if not tempchnk:
                        break
                    if tempfl==1:
                        self.parts[start]=tempchnk
                        tempfl=tempfl+1
                    else:
                        self.parts[start]=self.parts[start]+tempchnk
                    while pauseflag:
                        
                        continue
                    
                   # time.sleep(0.75)
                    printgui(str(round((newsize*100)/self.size,2))+"% completed! :D",per)
                    pb_hd["value"] = int(round((newsize*100)/self.size,2))
 
                return
            def er(self):
                return self.error
            def savefile(self):
                f=open(self.filename,"wb")
                ch=''
                i=1
                res=self.parts[0]
                while ch!=None:
                    k=i*self.chunk
                    if k in self.parts:
                        ch=self.parts[i*self.chunk]
                        res=res+self.parts[i*self.chunk]
                        i=i+1
                    else:
                        break
                f.write(res)
                f.close()
                printgui('size- '+str(os.path.getsize(self.filename)),lab)
            def schnk(self):
                return self.chunk
                
        def downsome(uri,tempna):
              
            temp=threading.Thread(target=reqfunc,args=(uri,"random"))
            temp.start()
            code='404'
            d=downloadfile(uri)
            threads=[]
            if d.er():
                printgui("Try again later!:/",lab)
                return code
            
            d.namesize(tempna)
            if d.er():
                printgui("Try again later  !:/",lab)
                return code
            temp.join()
            starttime=time.time()
            global notr
            for i in range(0,notr):
                t=threading.Thread(target=d.downl,args=(i*d.schnk(),"RANDOM"))
                t.start()
                printgui("started"+str(i),per)
                threads.append(t)
            printgui("0% Completed :/",per)
            for i in threads:
                i.join()
                root.protocol("WM_DELETE_WINDOW", root.destroy)
            endtime=time.time()
            if d.er():
                printgui("Try again later!",lab)
                return code
            d.savefile()
            time.sleep(2)
            printgui("Time Taken-"+str(endtime-starttime),per)
            time.sleep(2)
            root.destroy()
            return '400'
        stop_threads = False
        t=threading.Thread(target=downsome,args=(goturi,gotname)  )
        t.start()
            
        root.mainloop()
    except:
        print('ERROR')

def interact(u,n):
    guiclt(u,n)
