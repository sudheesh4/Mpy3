from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter import ttk
import tkinter.filedialog
from tkinter import *
from DownloadUrl import *
from emp3 import *
import sys
import os
import time
import threading
#import subprocess
root = Tk()
#root.iconbitmap('favicon.ico')
root.title('Mpy3')
def help():
    top=Toplevel(root)
    #top.iconbitmap('favicon.ico')
    top.title('Mpy3- Help')
    Label(top,text="1.Enter name of song you want to download and Go!").grid(row=0,column=0,sticky=W)
    Label(top,text="2.Select which song to download from List").grid(row=1,column=0,sticky=W)
    Label(top,text="3.Green -Downloading;Red -Paused or Error;Blue-Completed ").grid(row=2,column=0,sticky=W)
    Label(top,text="4.To pause a download or resume a paused link just click on the link").grid(row=3,column=0,sticky=W)
    Label(top,text="5.Once Download is complete click on the link to play it!").grid(row=4,column=0,sticky=W)
def proxy():
    pass
def about():
    top=Toplevel(root)
    top.title('Mpy3- About')
    Label(top,text="Mpy3! No more need to search through out Google to download a song!").grid(row=0,column=0,sticky=W)
    Label(top,text="Download quick and Fast!").grid(row=1,column=0,sticky=W)
    Label(top,text="I hope it helps you! :)").grid(row=2,column=0,sticky=W)
    Label(top,text="Report errors/bugs at -..").grid(row=3,column=0,sticky=W)
    Label(top,text="jointedace_s4").grid(row=4,column=1,sticky=E)
def update(name,label,dobj,complete):
    global log,dictlabel
    
    while not complete[0]:
        status,per=dobj.getstatus()
        size=dobj.getsize()
        if size>1024*1024:
            size=round(size/(1024*1024),2)
            size=str(size)+" Mb"
        else:
            size=str(size)+" Kb"
        try:
            label['text']=name+"-"+size+"-"+status+"-"+str(per)+"%"
            root.update()
        except:
            pass
    if not dobj.er():
        try:
            label['text']=name+"-"+size+"-"+status+"-"+"100%"
            root.update()
        except:
            pass



def peer(event,name,i):
    if i==1:
        t=''
        for c in name:
            if c=='/':
                t=t+'\\'
            else:
                t=t+c
        try:
            os.system(t)
        except:
            print("cannot open from here! :/")
        return
    if i==2:
        
       # subprocess.Popen('explorer "{0}"'.format(name))
        #dir=name
        t=''
        dir=os.path.dirname(name)
        for c in dir:
            if c=='/':
                t=t+'\\'
            else:
                t=t+c
        try:
            os.system('explorer '+t)
        except:
            print("cannot open from here! :/")
        return



def peerpause(event,pause,label,c):
    try:
        if c==0:
            pause[0]=True
            label.bind('<Button-1>',lambda event:peerpause(event,pause,label,1)) 
            label.config(fg="red",cursor="hand2")
        if c==1:
            pause[0]=False
            label.bind('<Button-1>',lambda event:peerpause(event,pause,label,0)) 
            label.config(fg="green",cursor="hand2")
    except:
        pass
    


    

def handlelink(label,uri,name):
    try:
        uri=uri.replace(' ','%20')
        pause=[]
        pause.append(False)
        print(uri)
        label.bind('<Button-1>',lambda event:peerpause(event,pause,label,0)) 
        label.config(fg="green",cursor="hand2")
      
        d=downloadfile(uri,pause)
        k=[]
        k.append(False)
        st=threading.Thread(target=update,args=(os.path.basename(name.name),label,d,k))
        st.setDaemon(True)
        st.start()
        thread=[]
        if d.er():
            k[0]=True
           # print("try later!:/")
            
            return
        d.namesize(os.path.basename(name.name))
        if d.er():
            k[0]=True
           # print("No file")
            return
        req=urllib.request.Request(uri)
        for i in range(0,d.notr):
            t=threading.Thread(target=d.downl,args=(i*d.schnk(),req))
            t.setDaemon(True)
            t.start()
            #print("started",i)
            thread.append(t)

        for i in thread:
            i.join()
        k[0]=True
        if d.er():
            
            print('ERROR 101:/')
            return
        else:
            d.savefile(name)
            label.bind('<Button-1>',lambda event:peer(event,name.name,1))
            tempn=os.path.basename(name.name)
            label.bind("<Button-3>",lambda event:peer(event,name.name,2))
            name.close()
            label.config(fg="blue",cursor="hand2")
    except:
        pass
    
        
class GUI(ttk.Frame):
  
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)   
         
        self.parent = parent
        self.songthreads=[]
        self.songlabels=[]
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Mpy3")
##        
##        self.style = ttk.Style()
##        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl =ttk. Label(self, text=" ")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        self.area = Text(self,state=DISABLED)
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        
        self.help = ttk.Button(self, text="Help",command=help)
        self.help.grid(row=1, column=3)

        cbtn = ttk.Button(self, text="Socks5",command=proxy)
        cbtn.grid(row=2, column=3, pady=4)        
        self.entry = Entry(self)
        self.entry.grid(row=5, column=0, padx=5,columnspan=3)

        obtn = ttk.Button(self, text="Go",command=self.startit)
        obtn.grid(row=5, column=3)
        self.parent.bind('<Return>',self.peertostart)

            
        
    def peertostart(self,event):
        self.startit()
    def startit(self):

        def startpeer(self):
             global dictlabel
             try:
                 s=song_emp3(self.entry.get())
             except:
                return
             if not s.error:
                 downuri,downame=self.getdownlink(s)
                 if downuri=="":
                     print("NO LINK FOUND ! :/")
                     return
                 if downame==None:
                     print("canceled!")
                     return
                 l=Label(self.area,text=str(os.path.basename(downame.name))+"-Connecting")
                 l.config(bg='white')  
                 t=threading.Thread(target=handlelink,args=(l,downuri,downame))
                 t.setDaemon(True)
                 self.songthreads.append(t)
                 t.start()
                 
                 l.pack()
        t=threading.Thread(target=startpeer,args=(self,))
        t.setDaemon(True)
        t.start()
        

    def getdownlink(self,sel):
         try:
             l=sel.givelinks()
             urlnames=sel.givenames()
             for i in range(0,len(l)):
                 print(str(i+1)+">"+urlnames[i])
         except:
             pass
         if(len(l)==0):
             return ("","")
         try:
             i=int(input("Which one?"))-1
         except:
             print("Invalid choice")
             return("","")
         f = tkinter.filedialog.asksaveasfile(mode='wb', defaultextension=".mp3")
         return (l[i],f)


     
def main():
  
    
    root.geometry("350x300+300+300")
    app = GUI(root)
    root.mainloop()


    


if __name__ == '__main__':
    main()  
