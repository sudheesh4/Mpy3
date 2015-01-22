from tkinter import *
from tkinter import ttk
class SOMEMSG:
    def __init__(self, parent,txt,temp):

        top = self.top = Toplevel(parent)
     #  self.top.iconbitmap('favicon.ico')
        self.top.title('Mpy3')
        Label(top, text=txt).pack()
        self.temp=temp
        self.e = Entry(top)
        self.e.pack(padx=5)
        b = ttk.Button(top, text="OK",command=self.ok)
        
        b.pack(pady=5)

    def ok(self):
        self.temp.append(self.e.get())

        self.top.destroy()


class MSSG:
    def __init__(self, parent,txt):

        top = self.top = Toplevel(parent)

        Label(top, text=txt).pack()

        b = ttk.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        self.top.destroy()


class justmssg:
    def __init__(self, parent,txt):

        top = self.top = Toplevel(parent)

        Label(top, text=txt).pack()

        b = ttk.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        pass

class Linkmssg:
    def __init__(self,parent,name,temp):
        try:
            
            self.top=Toplevel(parent)
            self.top.minsize(width=400, height=300)
            self.top.maxsize(width=400, height=300)
            self.txtarea=Text(self.top,state=DISABLED,height=15,width=55)
            self.txtarea.pack()
            scroll=Scrollbar(self.txtarea)
            scroll.pack(side=RIGHT,fill=Y)
            scroll.config(command=self.txtarea.yview)
            self.txtarea.config(yscrollcommand=scroll.set)
            self.entry=Entry(self.top)
            self.entry.pack()
            self.temp=temp
            i=0
            for n in name:
                n=str(i)+">"+n
                self.txtarea["state"]=NORMAL
                self.txtarea.insert(END,"\n"+n)
                self.txtarea["state"]=DISABLED

                i=i+1
            self.ok=ttk.Button(self.top,text="ok!",command=self.OK)
            self.ok.pack()
            inf=Label(self.top,text="(Enter the number corresponding to desired choice)")
            inf.pack()
        except:
            pass
    def OK(self):
        self.temp.append(self.entry.get())
        self.top.destroy()
