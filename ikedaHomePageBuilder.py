import tkinter as tk
import re
import datetime

base=tk.Tk()
base.title('Ikeda HomePage Builder(beta)')
base.geometry("700x400")
base.configure(bg='skyblue')
canvas=tk.Canvas(base,bg='#FFFFFF',width=700,height=400)#for scrollbar
frame=tk.Frame(canvas,bg='#A0A0A0')
frame1=tk.Frame(frame,bg='#FFFFFF')
frame2=tk.Frame(frame,bg='#A0A0A0')
frame3=tk.Frame(frame1,bg='#FFFFFF')
frame4=tk.Frame(frame,bg='#FFFFFF')
entryList = list()
stringList = list()
headingDict= {}
listsv = None
listbox=None

class Entry:
    type=None
    entry=None
    id=None
    sv0=None
    sv=None
    label1=None
    label2=None
    selectedListIndex=None
    def __init__(self,base, type):
        self.type = type
        if type=='p':
            self.entry=tk.Text(base,width=40, height=20)
        elif type=='code':
            self.entry=tk.Text(base,width=40, height=20)
        else:
            self.label1=tk.Label(base,text='ID')
            self.label2=tk.Label(base,text='Text')
            self.sv0=tk.StringVar()
            self.sv0.set('')
            self.id=tk.Entry(base,textvariable=self.sv0,width=31)
            self.sv=tk.StringVar()
            self.sv.set('')
            self.entry=tk.Entry(base,textvariable=self.sv,width=31)

    def writeToFile(self):
        if self.type=='p':
            if self.entry.get('1.0', 'end -1c')!='':
                string='<p>'+self.entry.get('1.0', 'end -1c').replace('\n','\n<br/>\n')+'</p>\n'
            else:
                string=None
        elif self.type=='code':
            if self.entry.get('1.0', 'end -1c')!='':
                string='<code><pre class="prettyprint linenums">'+self.entry.get('1.0', 'end -1c')+'</pre></code>\n'
            else:
                string=None
        elif self.type[0]=='h':
            if self.sv0.get()!='':
                headingDict[self.sv0.get()]=self.sv.get()
                string='<h'+self.type[1]+' id="'+self.sv0.get()+'">'
            else:
                string='<h'+self.type[1]+'>'
            if self.sv.get()!='':
                string=string+self.sv.get()+'</h'+self.type[1]+'>\n'
            else:
                string=None
        else:
            string=self.sv.get()
        return string

    def getCurrentString(self):
        if self.type=='p':
            if self.entry.get('1.0', 'end -1c')!='':
                string=self.entry.get('1.0', 'end -1c')
            else:
                string=None
        elif self.type=='code':
            if self.entry.get('1.0', 'end -1c')!='':
                string=self.entry.get('1.0', 'end -1c')
            else:
                string=None
        elif self.type[0]=='h':
            if self.sv.get()!='':
                string=string+self.sv.get()
            else:
                string=None
        else:
            string=self.sv.get()
        return string

    def setText(self):
        global stringList
        if self.selectedListIndex != None:
            self.entry.insert(tk.END,stringList[self.selectedListIndex])

    def getEntry(self):
        return self.entry

    def getIDEntry(self):
        return self.id

    def getLabel1(self):
        return self.label1

    def getLabel2(self):
        return self.label2

    def setSelectedListIndex(self,int):
        self.selectedListIndex=int

    def hide(self):
        global stringList
        text=self.writeToFile()
        if(text != None):
            if self.selectedListIndex != None:
                stringList[self.selectedListIndex]=text
            else:
                stringList.append(text)
        if self.label1 != None:
            self.label1.destroy()
        if self.label2 != None:
            self.label2.destroy()
        if self.id != None:
            self.id.destroy()
        self.entry.destroy()

def makeFile(fname):
    if len(entryList) !=0:
        last=entryList[-1]
        last.hide()
    with open(fname+'.html','a')as f:
        for s in stringList:
            f.write(s)
            f.flush()
        f.write('<h6>作成日</h6>\n')
        f.write('<p>'+datetime.date.today().strftime('%Y/%m/%d')+'</p>\n')
        f.write('''<br/>
<h6>更新日</h6>
<p>//</p>
</div><!-- /#main -->
<div id="sub">
 <div class="section">
    <h2>---</h2>
    <ul>
      <li><a href="" style="color: #0000ff;">1:</a></li>
      <!--
    <li><a href="index.html">MENU1</a></li>
    <li><a href="index.html">MENU2</a></li>
    <li><a href="index.html">MENU3</a></li>
    <li><a href="index.html">MENU4</a></li>
    <li><a href="index.html">MENU5</a></li>
    <li><a href="index.html">MENU6</a></li> -->
    </ul>
 </div><!-- /.section -->
 <!--
 <div class="section">
    <h2>趣味のこと</h2>
    <ul>
    <li><a href="index.html">MENU1</a></li>
    <li><a href="index.html">MENU2</a></li>
    <li><a href="index.html">MENU3</a></li>
    <li><a href="index.html">MENU4</a></li>
    <li><a href="index.html">MENU5</a></li>
    <li><a href="index.html">MENU6</a></li>
    </ul>
 </div>
-->
</div><!-- /#sub -->
</div><!-- /#contents -->
<div id="pageTop">
<a href="#top">ページのトップへ戻る</a>
</div><!-- /#pageTop -->
<div id="footer">
<div class="copyright">Copyright &copy; 2019 IkeLog All Rights Reserved.</div>
</div><!-- /#footer -->
</div><!-- /#top -->
<script type="text/javascript" src="js/prettify.js"></script>
<script type="text/javascript" src="js/lang-css.js"></script>
<script>
prettyPrint();
</script>
</body>
</html>''')
    base.destroy()

def insertTitle(title):
    stringList.insert(0,'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <meta http-equiv="imagetoolbar" content="no" />
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <link rel="stylesheet" href="css/common.css" type="text/css" />'''+'<title>'+title+'</title>\n')

def insertSubTitle(subtitle1,subtitle2):
    stringList.insert(1,'''</head>
    <body>
    <div id="top">
       <div id="header">
         <h1><a href="index.html">IkeLog</a>_<a href="">'''+subtitle1+'''</a>()</h1>
  </div><!-- /#header -->
  <div id="menu">
     <ul>

       <!--//タブを作る
     <li><a href="index.html">MENU1</a></li>
     <li><a href="index.html">MENU2</a></li>
     <li><a href="index.html">MENU3</a></li>
     <li><a href="index.html">MENU4</a></li>
     <li><a href="index.html">MENU5</a></li>
     <li><a href="index.html">MENU6</a></li>-->
     </ul>
  </div><!-- /#menu -->
  <div id="contents">
    <div id="subtitle">
    <h3>'''+subtitle2+'''</h3>
    </div>
    <div>
      <ol>
        '''+agenda()+'''
      </ol>
    </div>
     <div id="main">''')

def agenda():
    string=''
    for heading in headingDict.keys():
        string=string+'        <li><a href="#'+heading+'">'+headingDict[heading]+'</a></li>\n'
    return string

def makeEntry(string):
    entry=Entry(frame2,string)
    if len(entryList) !=0:
        pre = entryList[-1]
        pre.hide()
    entryList.append(entry)
    idEntry=entry.getIDEntry()
    if idEntry != None:
        entry.getLabel1().pack()
        idEntry.pack(padx=5,pady=5)
        entry.getLabel2().pack()
    entry.getEntry().pack(padx=5,pady=5)
    showLabel()

def updateEntry(string,index):
    entry=Entry(frame2,string)
    entry.setSelectedListIndex(index)
    entry.setText()
    if len(entryList) !=0:
        pre = entryList[-1]
        pre.hide()
    entryList.append(entry)
    idEntry=entry.getIDEntry()
    if idEntry != None:
        entry.getLabel1().pack()
        idEntry.pack(padx=5,pady=5)
        entry.getLabel2().pack()
    entry.getEntry().pack(padx=5,pady=5)
    showLabel()

def showLabel():
    global frame4
    global window1
    global stringList
    global window1Geometry
    global listbox
    frame5=frame4
    frame5.destroy()
    frame4=tk.Frame(frame)
    frame4.pack(anchor=tk.N,side='left',padx=5,pady=5)
    listsv=tk.StringVar(value=stringList)
    listbox=tk.Listbox(frame4,listvariable = listsv,selectmode = 'extended',height = len(stringList))
    listbox.bind("<<ListboxSelect>>", listboxSelected)
    listbox.pack()

def addTag(tag):
    if len(entryList) != 0:
        entry= entryList[-1]
        if tag == 'a':
            entry.getEntry().insert(tk.INSERT,'<a href="" target="_blank"></a>')
        elif tag == 'img':
            entry.getEntry().insert(tk.INSERT,'<a href="" target="_blank"><img src="d"/></a>')
        elif tag == 'list':
            entry.getEntry().insert(tk.INSERT,'''<ol>
     <li></li>
     <li></li>
     <li></li>
</ol>''')
        else:
            None

def listboxSelected(arg):
    global listbox
    if listbox != None:
        selectedListNum=listbox.curselection()
        string=stringList[selectedListNum[0]][0:3]
        if string=='<p>':
            updateEntry('p',selectedListNum[0])
        elif string=='<co':
            updateEntry('code',selectedListNum[0])
        elif string=='<h1':
            updateEntry('h1',selectedListNum[0])
        elif string=='<h2':
            updateEntry('h2',selectedListNum[0])
        elif string=='<h3':
            updateEntry('h3',selectedListNum[0])
        elif string=='<h4':
            updateEntry('h4',selectedListNum[0])
        elif string=='<h5':
            updateEntry('h5',selectedListNum[0])
        else:
            print(string)

def funcManager(string1,string2,string3,string4 ):
    insertTitle(string1)
    insertSubTitle(string2,string3)
    makeFile(string4)

if __name__ == '__main__':
    canvas.pack(side='left',expand = True, fill = tk.BOTH)
    canvas.create_window((0,0), window=frame, anchor=tk.NW, width=canvas.cget('width'), height=canvas.cget('height'))
    frame1.pack(anchor=tk.N,side='left',padx=5,pady=5)
    frame2.pack(anchor=tk.N,side='left')
    frame4.pack(anchor=tk.N,side='left')
    sv=tk.StringVar()
    sv.set('File name')
    fnameEntry=tk.Entry(frame1,textvariable=sv).pack()
    sv1=tk.StringVar()
    sv1.set('Title')
    fnameEntry=tk.Entry(frame1,textvariable=sv1).pack()
    sv2=tk.StringVar()
    sv2.set('Sub title')
    fnameEntry=tk.Entry(frame1,textvariable=sv2).pack()
    sv3=tk.StringVar()
    sv3.set('Sub title2')
    fnameEntry=tk.Entry(frame1,textvariable=sv3).pack()
    sv4 = tk.StringVar()
    sv4.set('')
    option= tk.OptionMenu(frame1,sv4, 'h1', 'h2','h3','h4','h5','p','code',command=makeEntry).pack()
    button = tk.Button(frame1,text='Run',command= lambda: funcManager(sv1.get(),sv2.get(),sv3.get(),sv.get())).pack()
    frame3.pack()
    button = tk.Button(frame3,text='a',command= lambda: addTag('a')).pack(anchor=tk.N,side='left')
    button = tk.Button(frame3,text='img',command= lambda: addTag('img')).pack(anchor=tk.N,side='left')
    button = tk.Button(frame3,text='list',command= lambda: addTag('list')).pack(anchor=tk.N,side='left')
    base.mainloop()
