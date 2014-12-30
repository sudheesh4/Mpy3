import urllib.request
import sys
import os
import time
import threading
re=None
def reqfunc(a,b):
    global re
    re=urllib.request.Request(a)
class downloadfile:
    def __init__(self,uri):
        self.maxi=10
        i=0
        self.error=False
        self.size=0
        self.filename=''
        self.parts={}
        self.chunk=0
        self.uri=uri
        print("Connecting..")
        while i<self.maxi:
            try:
                self.url=urllib.request.urlopen(uri)
            except:
                i=i+1
                print(i)
                continue
            break
        if i==self.maxi:
            print("Umm something unexpected happened!:/")
            self.error=True
            return
        print("Connected")

    def namesize(self,tempn):
       # self.filename=input("Save as ? \n")
        self.filename=tempn
        try:
            self.size=int(self.url.getheader('Content-Length',None))
        except:

            print("No file found here!._.")
            self.error=True
            return
        self.chunk=int(self.size/5)
    def downl(self,start,randomargument):
        req=None
        global re
        i=0
        req=re
        while i<self.maxi:
            try:
                req.headers['Range']='bytes=%s-%s'% (start,start+self.chunk)
            except:
                i=i+1
                continue
            break
        if i==self.maxi:
            print("Bad Header!:/")
            self.error=True
            return
        i=0
        while i<self.maxi:
            try:
                f=urllib.request.urlopen(req)
            except:
                i=i+1
                continue
            break
        if i==self.maxi:
            print("No response!:/")
            self.error=True
            return
        self.parts[start]=f.read()
        print("\n"+str(int(start/self.chunk))+" completed! :D\n")
        return
    def er(self):
        return self.error
    def savefile(self):
        f=open(self.filename,"wb")
        ch=''
        i=1
        while ch!=None:
            k=i*self.chunk
            if k in self.parts:
                ch=self.parts[i*self.chunk]
                self.parts[0]=self.parts[0]+ch
                i=i+1
            else:
                break
        f.write(self.parts[0])
        f.close()
        print('size- ',os.path.getsize(self.filename))
    def schnk(self):
        return self.chunk
        
def downsome(uri,tempna):
    temp=threading.Thread(target=reqfunc,args=(uri,"random"))
    temp.start()
    code='404'
    d=downloadfile(uri)
    threads=[]
    if d.er():
        print("Try again later!:/")
        return code
    
    d.namesize(tempna)
    if d.er():
        print("Try again later!:/")
        return code
    temp.join()
    starttime=time.time()
    for i in range(0,5):
        t=threading.Thread(target=d.downl,args=(i*d.schnk(),"RANDOM"))
        t.start()
        print("started",i)
        threads.append(t)
    
    for i in threads:
        i.join()
    endtime=time.time()
    if d.er():
        print("Try again later!:/")
        return code
    d.savefile()
    print("Time Taken-",str(endtime-starttime))
    return '400'
    
#downsome('http://v4.mywappy.com/Singletrack/128/Turn%20Down%20For%20What%20-%20Manj%20Musik%20Ft%20Lil%20John%20(DjPunjab.Com).mp3')        
    
