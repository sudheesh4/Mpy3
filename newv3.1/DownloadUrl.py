
import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "localhost",9150)
socket.socket = socks.socksocket
import urllib.request
import sys
import os
import time
import threading
class downloadfile:
    def __init__(self,uri,pause):
        self.maxi=13
        i=0
        self.error=False
        self.pause=pause
        self.lastpause=False
        self.size=0
        self.filename=''
        self.parts={}
        self.chunk=0
        self.uri=uri
        self.status='connecting'
        self.pershow=0
        self.notr=6
        self.newsize=0
      #  printgui("Connecting..",lab)
        while i<self.maxi:
            try:
                self.url=urllib.request.urlopen(uri)
            except:
                i=i+1
                print(i)
                continue
            break
        if i==self.maxi:
           # printgui("Umm something unexpected happened!:/",lab)
            self.status="Error-Unable to connect"
            self.error=True
            return
        self.status='connected'
       # printgui("Connected",lab)

    def namesize(self,tempn):
       # self.filename=input("Save as ? \n")
        
        self.filename=tempn
        try:
            self.size=int(self.url.getheader('Content-Length',None))
        except:

           # printgui("No file found here!._.",lab)
            self.status="Error-No file"
            self.error=True
            return
        self.chunk=int(self.size/self.notr)
    def downl(self,start,re):
        req=None
        i=0
        req=re
        st=start
        en=int((start+self.chunk))
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
            #printgui("Bad Header!:/",lab)
            self.status='Error'
            self.error=True
            return
        i=0
       # printgui("Requesting",lab)
        self.status='Requesting'
        while i<self.maxi:
            if self.pause[0]:
                self.status="Paused"
                continue
            self.status='Requesting'
            try:
                f=urllib.request.urlopen(req)
            except:
                i=i+1
                continue
            break
        if i==self.maxi:
            #printgui("No response!:/",lab)
            self.status='Error-No response'
            self.error=True
            return

        newchunk=8192
        #newchunk=self.chunk/4
       # printgui("Reading",lab)
        if not self.error:
            self.status='Downloading'
            tempfl=1
            while not self.error:
                if self.pause[0]:
                    
                    print("PAUSED")
                    continue
                self.status='Downloading'

                
                tempchnk=f.read(newchunk)

                self.newsize=self.newsize+len(tempchnk)
                if not tempchnk:
                    break
                if tempfl==1:
                    self.parts[start]=tempchnk
                    tempfl=tempfl+1
                else:
                    self.parts[start]=self.parts[start]+tempchnk
                "afsa"
                if self.pause[0]:
                    self.lastpause=True
                    print("PAUSED")
                    continue
                self.status='Downloading'
                if self.lastpause:
                    time.sleep(1)
                    self.lastpause=False
               # time.sleep(0.75)
               # printgui(str(round((self.newsize*100)/self.size,2))+"% completed! :D",per)
               # pb_hd["value"] = int(round((self.newsize*100)/self.size,2))
                self.pershow=int(round((self.newsize*100)/self.size,2))

        return
    def er(self):
        return self.error
    def savefile(self,f):
        #f=open(self.filename,"wb")
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
       # f.close()
        #printgui('size- '+str(os.path.getsize(self.filename)),lab)
        self.status='Completed'
    def schnk(self):
        return self.chunk
    def getsize(self):
        return self.size
    def getstatus(self):
        return(self.status,self.pershow)

