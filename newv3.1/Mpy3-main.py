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
    text="""Enter name of song you want to download and Go!
    Select which song to download from List
    Green -Downloading;Red -Error
    Orange-Paused;Blue-Completed
    To pause a download or resume a
    paused link just click on the link
    Once Download is complete Left click
    on the link to play it , and Right Click
    to open the file location!
    """
    Label(top,text=text,fg="red",font = "Verdana 8 bold").grid(row=1,column=0,sticky=W)

def proxy():
    pass
def about():
    top=Toplevel(root)
    top.title('Mpy3- About')
##    img=ImageTk.PhotoImage(Image.open('info.png'))
##    w = img.width()
##    h = img.height()
##    top.geometry('%dx%d+0+0' % (w,h))
## #   Label(top,image=img).grid(row=0,column=1)
##    background_label = Label(top, image=img)
##    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    text="""Mpy3!
    No more need to search through
    out Google to download a song!
    Download quick and Fast!
    I hope it helps you! :)
    Report errors/bugs at -
    sud4decrypt@gmail.com"""
    Label(top,text=text,fg="green",font = "Verdana 8 bold").grid(row=1,column=0,sticky=W)

    Label(top,text="jointedace_s4", fg="blue",font = "Verdana 6 bold").grid(row=5,column=0,sticky=E)
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
            label.config(fg="orange",cursor="hand2")
        if c==1:
            pause[0]=False
            label.bind('<Button-1>',lambda event:peerpause(event,pause,label,0)) 
            label.config(fg="green",cursor="hand2")
    except:
        pass
    


##def handlelink(label,uri,name):
##    try:
##        uri=uri.replace(' ','%20')
##        pause=[]
##        pause.append(False)
##        label.bind('<Button-1>',lambda event:peerpause(event,pause,label,0))
##        label.config(fg="green",cursor="hand2")
##        d=downloadfile(uri,pause)
##        k=[]
##        k.append(False)
##        st=threading.Thread(target=update,args=(os.path.basename(name.name),label,d,k))
##        st.setDaemon(True)
##        st.start()
##        if d.er():
##            k[0]=True
##            return
##        req=urllib.request.Request(uri)
##        d.simpledown(req,name)
##        k[0]=True
##        label.config(fg="blue")
##        name.close()
##        return
##    except:
##        print("ERROR")
##        pass
def justrandom(ev):
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
            label.config(fg="red",cursor="hand2")
            label.bind('<Button-1>',lambda event:justrandom(event))
            name.close()            
            return
        d.namesize(os.path.basename(name.name))
        
        if d.er():
           # d.simpledown(req,name)
            k[0]=True
           # print("No file")
            label.config(fg="red",cursor="hand2")
            label.bind('<Button-1>',lambda event:justrandom(event))
            name.close()           
            return
        req=urllib.request.Request(uri)
        tr=req
        tr.headers['Range']='bytes=%s-%s'% (0,512)
        tempf=urllib.request.urlopen(tr)
        print(tempf.code)
        
        if int(str(tempf.code))==200:
            d.downlauto(tempf,name)
            if d.er():
                print('error!:/')
                label.config(fg="red",cursor="hand2")
                label.bind('<Button-1>',lambda event:justrandom(event))
                name.close()
                return
            else:
                label.bind('<Button-1>',lambda event:peer(event,name.name,1))
                tempn=os.path.basename(name.name)
                label.bind("<Button-3>",lambda event:peer(event,name.name,2))
                name.close()
                label.config(fg="blue",cursor="hand2")
            return
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
            label.config(fg="red",cursor="hand2")
            label.bind('<Button-1>',lambda event:justrandom(event))
            name.close()
            return
        else:
            d.savefile(name)
            label.bind('<Button-1>',lambda event:peer(event,name.name,1))
            tempn=os.path.basename(name.name)
            label.bind("<Button-3>",lambda event:peer(event,name.name,2))
            name.close()
            label.config(fg="blue",cursor="hand2")
    except:
        print('c')
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

        cbtn = ttk.Button(self, text="About",command=about)
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
             to=Toplevel(root)
             nameofsong=self.entry.get()
             to.title(nameofsong+'~Status')
             statlab=Label(to,text="Connecting..")
             statlab.pack()
             try:
                 s=song_emp3(nameofsong)
             except:
                to.destroy()
                return
             ""
             
             if not s.error:
                 try:
                    statlab['text']="Connected!Parsing links.."
                 except:
                    pass                 
                 downuri,downame=self.getdownlink(s)
                 if downuri=="":
                     try:
                         statlab['text']="Got no link here! :/"
                     except:
                         pass
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
                 return
             try:
                 statlab['text']="Not able to connect!"
             except:
                 pass
        t=threading.Thread(target=startpeer,args=(self,))
        t.setDaemon(True)
        t.start()
        

    def getdownlink2(self,sel):
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
    def getdownlink(self,sel):
         try:
            l=sel.givelinks()
            urlnames=sel.givenames()
            temp=[]
            from mssgboxes import Linkmssg
            root.withdraw()
            lm=Linkmssg(root,urlnames,temp)
            root.wait_window(lm.top)
            root.update()
            root.deiconify()
            i=int(temp[0])
            if i<0:
                i=i*-1
            "asgfa"
            if i<len(l):
                f=tkinter.filedialog.asksaveasfile(mode="wb",defaultextension=".mp3")
                return(l[i],f)
            return("","")
         except:
            return("","")
    
                
    
def main():
  
    
    root.geometry("350x300+300+300")
    app = GUI(root)
    root.mainloop()


    


if __name__ == '__main__':
    main()  
