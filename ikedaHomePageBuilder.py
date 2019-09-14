import tkinter as tk

base=tk.Tk()
base.geometry("400x200")
canvas=tk.Canvas(base)
frame=tk.Frame(canvas)
entryList = list()
stringList = list()

class Entry:
    type=None
    entry=None
    sv=None
    def __init__(self,base, type):
        self.type = type
        if type=='p':
            print('p')
            self.entry=tk.Text(base,width=20, height=6)
        elif type=='code':
            print('code')
            self.entry=tk.Text(base,width=20, height=6)
        else:
            print('other')
            self.sv=tk.StringVar()
            self.sv.set('')
            self.entry=tk.Entry(base,textvariable=self.sv)

    def writeToFile(self):
        if self.type=='p':
            string='<p>'+self.entry.get('1.0', 'end -1c').replace('\n','\n<br/>\n')+'</p>\n'
        elif self.type=='code':
            string='<code><pre class="prettyprint linenums">'+self.entry.get('1.0', 'end -1c')+'</pre></code>\n'
        elif self.type=='h1':
            string='<h1>'+self.sv.get()+'</h1>\n'
        elif self.type=='h2':
            string='<h2>'+self.sv.get()+'</h2>\n'
        elif self.type=='h3':
            string='<h3>'+self.sv.get()+'</h3>\n'
        elif self.type=='h4':
            string='<h4>'+self.sv.get()+'</h4>\n'
        elif self.type=='h5':
            string='<h5>'+self.sv.get()+'</h5>\n'
        else:
            string=self.sv.get()
        return string

    def getEntry(self):
        return self.entry

    def hide(self):
        print("hide is called")
        stringList.append(self.writeToFile())
        for s in stringList:
            print(s)
            print('\n')
        self.entry.destroy()

def makeFile(fname):
    if len(entryList) !=0:
        last=entryList[-1]
        last.hide()
    with open(fname,'a')as f:
        for s in stringList:
            f.write(s)
            f.flush()
        f.write('''<h6>作成日</h6>
<p>//</p>
<br/>
<h6>更新日</h6>
<p>//</p>
</div><!-- /#main -->
<div id="sub">
 <div class="section">
    <h2>Android</h2>
    <ul>
      <li><a href="android1.html">1:導入</a></li>
      <li><a href="android2.html">2:新しいプロジェクトを作る</a></li>
      <li><a href="android3.html" style="color: #0000ff;">3:SurfaceViewをつかってみる</a></li>
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
<div class="copyright">Copyright &copy; 2018 IkeLog All Rights Reserved.</div>
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

def buttonAction(entry):
    entry.hide()

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
    entry=Entry(frame,string)
    if len(entryList) !=0:
        pre = entryList[-1]
        pre.hide()
    entryList.append(entry)
    entry.getEntry().pack()

def funcManager(string1,string2,string3 ):
    insertTitle(string1)
    insertSubTitle(string2)
    makeFile(string3)

if __name__ == '__main__':
    canvas.pack(side=tk.LEFT, fill=tk.BOTH)
    # frame.pack()
    canvas.create_window((0,0), window=frame, anchor=tk.NW, width=canvas.cget('width'))
    scrollbar = tk.Scrollbar(base, orient=tk.VERTICAL)
    # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar.config(command=canvas.yview)
    canvas.config(scrollregion=(0,0,400,400))
    canvas.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    sv=tk.StringVar()
    sv.set('File name')
    fnameEntry=tk.Entry(frame,textvariable=sv).pack()
    sv1=tk.StringVar()
    sv1.set('Title')
    fnameEntry=tk.Entry(frame,textvariable=sv1).pack()
    sv2=tk.StringVar()
    sv2.set('Sub title')
    fnameEntry=tk.Entry(frame,textvariable=sv2).pack()
    sv3 = tk.StringVar()
    sv3.set('')
    option= tk.OptionMenu(frame,sv3, 'h1', 'h2','h3','h4','h5','p','code',command=makeEntry).pack()
    # button = tk.Button(base,text='Run',command= lambda: makeFile(textBox.get('1.0', 'end -1c'))).pack()
    # button = tk.Button(frame,text='Run',command= lambda: makeFile(sv.get())).pack()
    button = tk.Button(frame,text='Run',command= lambda: funcManager(sv1.get(),sv2.get(),sv.get())).pack()
    base.mainloop()
