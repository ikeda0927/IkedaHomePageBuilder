import tkinter as tk
import re
import datetime

base=tk.Tk()
base.title('Ikeda HomePage Builder(beta)')
base.geometry("600x400")
base.configure(bg='skyblue')
canvas=tk.Canvas(base,bg='#FFFFFF',width=570,height=400)
frame=tk.Frame(canvas,bg='#A0A0A0')
frame1=tk.Frame(frame,bg='#FFFFFF')
frame2=tk.Frame(frame,bg='#A0A0A0')
frame3=tk.Frame(canvas)
window1=None
window1Geometry=None
entryList = list()
stringList = list()

class Entry:
    type=None
    entry=None
    sv=None
    def __init__(self,base, type):
        self.type = type
        if type=='p':
            self.entry=tk.Text(base,width=40, height=20)
        elif type=='code':
            self.entry=tk.Text(base,width=40, height=20)
        else:
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
        elif self.type=='h1':
            if self.sv.get()!='':
                string='<h1>'+self.sv.get()+'</h1>\n'
            else:
                string=None
        elif self.type=='h2':
            if self.sv.get()!='':
                string='<h2>'+self.sv.get()+'</h2>\n'
            else:
                string=None
        elif self.type=='h3':
            if self.sv.get()!='':
                string='<h3>'+self.sv.get()+'</h3>\n'
            else:
                string=None
        elif self.type=='h4':
            if self.sv.get()!='':
                string='<h4>'+self.sv.get()+'</h4>\n'
            else:
                string=None
        elif self.type=='h5':
            if self.sv.get()!='':
                string='<h5>'+self.sv.get()+'</h5>\n'
            else:
                string=None
        else:
            string=self.sv.get()
        return string

    def getEntry(self):
        return self.entry

    def hide(self):
        print("hide is called")
        text=self.writeToFile()
        if(text != None):
            stringList.append(text)
        for s in stringList:
            print(s)
            print('\n')
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
    if window1 != None:
        window1.destroy()
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

def insertSubTitle(subtitle):
    stringList.insert(1,'''</head>
    <body>
    <div id="top">
       <div id="header">
         <h1><a href="index.html">IkeLog</a>_<a href="">'''+subtitle+'''</a>()</h1>
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
    <h3>_</h3>
    </div>
    <div>
      <ol>
        <li><a href="#heading1">_</a></li>
        <li><a href="#heading2">_</a></li>
        <li><a href="#heading3">_</a></li>
        <li><a href="#heading4">_</a></li>
      </ol>
    </div>
     <div id="main">''')

def makeEntry(string):
    entry=Entry(frame2,string)
    if len(entryList) !=0:
        pre = entryList[-1]
        pre.hide()
    entryList.append(entry)
    entry.getEntry().pack(padx=5,pady=5)
    showLabel()

def window1OnClosing():
    global window1
    window2=window1
    window1=None
    window2.destroy()

def showLabel():
    global frame3
    global window1
    if window1 != None:
        window1Geometry=window1.geometry()
        window1Geometry=re.sub('[0-9.]+x[0-9.]+','',window1.geometry())
        window1.destroy()
    else:
        window1Geometry='+100+100'
    window1=tk.Tk()
    window1.title('View')
    window1.protocol("WM_DELETE_WINDOW", window1OnClosing)
    window1.geometry(window1Geometry)#'200x200'+
    window1Frame=tk.Frame(window1,bg='#FF0000')
    # window1Scrollbar=tk.Scrollbar(window1, orient=tk.VERTICAL,bg='#FF0000')
    window1Canvas= tk.Canvas(window1,bg='#FFFF00')#,width=170,height=200
    window1Canvas.create_window((0,0), anchor=tk.NW, width=window1Canvas.cget('width'), height=window1Canvas.cget('height'))
    window1Frame.pack(anchor=tk.N,side='left')
    # window1Canvas.config(scrollregion=window1Canvas.bbox('all'))
    # window1Canvas.config(yscrollcommand=window1Scrollbar.set)
    # window1Scrollbar.config(command=window1Canvas.yview)
    # window1Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    window1Canvas.pack()
    # labelHeight=0
    for string in stringList:
        label= tk.Label(window1Canvas,text=string).pack()#,width=20,height=1 padx=1,pady=1
        # labelHeight=labelHeight+2
    # window1Frame.update()
    # window1Canvas.config(scrollregion=(0,0,0,labelHeight))


def funcManager(string1,string2,string3 ):
    insertTitle(string1)
    insertSubTitle(string2)
    makeFile(string3)

if __name__ == '__main__':
    canvas.pack(side='left',expand = True, fill = tk.BOTH)
    print('width:'+str(canvas.cget('width'))+' height:'+str(canvas.cget('height')))
    canvas.create_window((0,0), window=frame, anchor=tk.NW, width=canvas.cget('width'), height=canvas.cget('height'))
    frame1.pack(anchor=tk.N,side='left')
    frame2.pack(anchor=tk.N,side='left')
    frame3.pack(anchor=tk.N,side='left')
    scrollbar = tk.Scrollbar(base, orient=tk.VERTICAL)
    scrollbar.config(command=canvas.yview)
    canvas.config(scrollregion=canvas.bbox('all'))
    canvas.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    sv=tk.StringVar()
    sv.set('File name')
    fnameEntry=tk.Entry(frame1,textvariable=sv).pack()
    sv1=tk.StringVar()
    sv1.set('Title')
    fnameEntry=tk.Entry(frame1,textvariable=sv1).pack()
    sv2=tk.StringVar()
    sv2.set('Sub title')
    fnameEntry=tk.Entry(frame1,textvariable=sv2).pack()
    sv3 = tk.StringVar()
    sv3.set('')
    option= tk.OptionMenu(frame1,sv3, 'h1', 'h2','h3','h4','h5','p','code',command=makeEntry).pack()
    button = tk.Button(frame1,text='Run',command= lambda: funcManager(sv1.get(),sv2.get(),sv.get())).pack()
    base.mainloop()
