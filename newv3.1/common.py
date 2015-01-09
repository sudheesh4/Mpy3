from download3 import *
from tkinter import *
from mssgboxes import *
import threading
root=Tk()
root.title('links')
root.withdraw()
##root.minsize(width=666, height=550)
##root.maxsize(width=666, height=550)

def peer(event,name,tempfn):
##    i=0
##    for names in urinam:
##        if names==name:
##            break
##        i=i+1
    te=[]
    d=SOMEMSG(root,"Save as?",te)
    root.wait_window(d.top)
    tempfn=te[0]
    tempfn=tempfn+".mp3"
    name=name.replace(" ","%20")
    t=threading.Thread(target=interact,args=(name,tempfn))
    t.start()
    
    
    
def peer2(tempfn,url_names,link):
    index=0
    to=Toplevel(root)
    to.iconbitmap('favicon.ico')
    to.title('Mpy3-Links')
##    for i in range(0,int(10)):##This doesnt work
##        ttk.Button(to,text="DOWNLOAD",command=lambda:peer(link[i],tempfn)).grid(row=i,column=0)
##        Label(to, text=url_names[i], fg="Blue", cursor="hand2").grid(row=i,column=1)
    l=Label(to, text=url_names[0], fg="Blue", cursor="hand2")
    l.bind("<Button-1>",lambda event: peer(event,link[0],tempfn))
    l.pack()
    l=Label(to, text=url_names[1], fg="Blue", cursor="hand2")
    l.bind("<Button-1>",lambda event: peer(event,link[1],tempfn))
    l.pack()
    l=Label(to, text=url_names[2], fg="Blue", cursor="hand2")
    l.bind("<Button-1>",lambda event: peer(event,link[2],tempfn))
    l.pack()
    try:
        l=Label(to, text=url_names[3], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[3],tempfn))
        l.pack() 
        l=Label(to, text=url_names[4], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[4],tempfn))
        l.pack()
        l=Label(to, text=url_names[5], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[5],tempfn))
        l.pack()
        l=Label(to, text=url_names[6], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[6],tempfn))
        l.pack()
        l=Label(to, text=url_names[7], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[7],tempfn))
        l=Label(to, text=url_names[8], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[8],tempfn))
        l.pack()
        l=Label(to, text=url_names[9], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[9],tempfn))
        l.pack()
        l=Label(to, text=url_names[10], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[10],tempfn))
        l.pack()
        l=Label(to, text=url_names[11], fg="Blue", cursor="hand2")
        l.bind("<Button-1>",lambda event: peer(event,link[11],tempfn))
    except:
        pass

    root.wait_window(to)

def manual_down(tempfn,url_names,link):
    peer2(tempfn,url_names,link)
    root.mainloop()
    
def auto_down(tempfn,url_names,link):
    print("Trying First link! ")
    
    for i in range(0,len(link)):
        uri=link[0]
        
        uri=uri.replace(" ","%20")#as all space are replaced by %20 while requesting!no whitepace!
        
        j=interact(uri,tempfn)
        if j=='404':
            print("Link "+str(i+1)+" Failed! Trying Next")
            continue
        print("DOWNLOADED!")
        break
    if i==len(link):
        print("COULD'NT DOWNLOAD! SORRY! :/")
        return "404"
    return "400"
 
##def manual_down(tempfn,url_names,link):
##    global tempna,linkn,urinam
##    urinam=url_names
##    linkn=link
##    temna=tempfn
##    printnames(url_names)
##    root.mainloop()
##    
##    choice=input("\n Which one to Download (to exit type exit)?  ")
##    while True:
##        
##        if choice=="exit":
##            print("Exiting!")
##
##            exit()
##        choice=int(choice)
##        print("Trying To download Link ->",url_names[choice-1])
##        uri=link[choice-1]
##        uri=uri.replace(" ","%20")
##        j=interact(uri,tempfn)
##        if j=="404":
##            print("Link ",choice , " could not be downladed! Try some other link")
##            printnames(url_names)
##            choice=input("\n Which one to try next ?  ")
##            continue
##        print("Downloaded!")
##
##        
##        choice="exit"
