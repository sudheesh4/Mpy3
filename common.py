from download3 import *
def printnames(url_names):
    for name in url_names:
        print(name)
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
    
def manual_down(tempfn,url_names,link):
    printnames(url_names)
    
    choice=input("\n Which one to Download (to exit type exit)?  ")
    while True:
        
        if choice=="exit":
            print("Exiting!")

            exit()
        choice=int(choice)
        print("Trying To download Link ->",url_names[choice-1])
        uri=link[choice-1]
        uri=uri.replace(" ","%20")
        j=interact(uri,tempfn)
        if j=="404":
            print("Link ",choice , " could not be downladed! Try some other link")
            printnames(url_names)
            choice=input("\n Which one to try next ?  ")
            continue
        print("Downloaded!")

        
        choice="exit"
