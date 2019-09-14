import tkinter as tk

base=tk.Tk()
frame=tk.Frame(base)
entryList = list()
stringList = list()

class Entry:
    type=""
    entry=None
    sv=tk.StringVar()
    def __init__(self,base, type):
        self.type = type
        if type=='p':
            print('p')
            self.entry=tk.Text(base)
        elif type=='code':
            print('code')
            self.entry=tk.Text(base)
        else:
            print('other')
            sv=tk.StringVar()
            sv.set('')
            self.entry=tk.Entry(base,textvariable=sv)

    def writeToFile(self):
        if type=="p":
            string=self.entry.get('1.0', 'end -1c')
        elif type=="code":
            string=self.entry.get('1.0', 'end -1c')
        else:
            string=self.sv.get()
        return string

    def getEntry(self):
        return self.entry

    def hide(self):
        print("hide is called")
        stringList=self.writeToFile()
        for s in stringList:
            print(s)
            print('\n')
        self.entry.destroy()

def makeFile():
    with open("test.txt",'a')as f:
        for s in stringList:
            f.write(s)
            f.flush()
    base.destroy()

def buttonAction(entry):
    entry.hide()

def makeEntry(string):
    # print("hello"+str)
    # textBox=tk.Text(frame).pack()
    # return textBox
    entry=Entry(frame,string)
    if len(entryList) !=0:
        # print("makeEntry : "+str(len(entryList)))
        pre = entryList[-1]
        pre.hide()
    entryList.append(entry)
    entry.getEntry().pack()
    button= tk.Button(frame,text="b",command=lambda: buttonAction(entry)).pack()

if __name__ == '__main__':
    frame.pack()
    # textBox= tk.Text(frame)
    # textBox.pack()
    sv1 = tk.StringVar()
    sv1.set('')
    option= tk.OptionMenu(base,sv1, 'h1', 'h2','h3','h4','h5','p','code',command=makeEntry).pack()
    # button = tk.Button(base,text='Run',command= lambda: makeFile(textBox.get('1.0', 'end -1c'))).pack()
    button = tk.Button(base,text='Run',command= lambda: makeFile()).pack()
    base.mainloop()
