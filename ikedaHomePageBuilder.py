import tkinter as tk


base=tk.Tk()
textBox= tk.Text(base)

def makeFile():
    with open("test.txt",'a')as f:
        f.write(textBox.get('1.0', 'end -1c'))
        f.flush()
    base.destroy()

if __name__ == '__main__':
    textBox.pack()
    button = tk.Button(base,text='Run',command=makeFile).pack()
    base.mainloop()