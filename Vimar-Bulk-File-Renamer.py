# Author: Viteac Marcin Witkowski
# Licence: MITM
# Release Date: 25.2.2021


from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import os
import shutil
import webbrowser

root = Tk()
root.title('Vimart-Bulk File Renamer 1.0')
root.resizable(0,0)

canvas=Canvas(root, bg='#06090f', width=960, height=540, bd =10)
canvas.grid(column=0,row=0)
backg = '#06090f'


def me():
    def callback(url):
        webbrowser.open_new(url)


    new=Toplevel(root)
    new.title('About Vimart')
    new.geometry('500x500')
    new.config(bg='#06090f', padx=70, pady=50,)
    new.resizable(0,0)
    napis=Label(new,text='Vimart',bg=backg, fg='white', font=('Ubuntu', 50, 'bold' )).grid(column=0, row=0)
    napis2 = Label(new, text='Bulk File Renamer', bg=backg, fg='white', font=('Ubuntu', 30, 'bold')).grid(column=0, row=1)
    napi3 = Label(new, text='1.0', bg=backg, fg='white', font=('Ubuntu', 20, 'bold')).grid(column=0, row=2)
    napi4 = Label(new, text='An open source tool for bulk file renaming for personal use.\n For commercial use contact: aceviu@gmail.com ', bg=backg, fg='white', font=('Ubuntu', 10)).grid(column=0, row=3)
    link1 = Label(new, text="\nWebsite", fg="red", bg=backg, cursor="hand2")
    link1.grid(column=0,row=4)
    link1.bind("<Button-1>", lambda e: callback("http://www.viteac.blogspot.com"))
    napi5 = Label(new, text='\n Copy right © 2020 Marcin Witkowski  ', bg=backg, fg='white', font=('Ubuntu', 12)).grid(column=0, row=5)


def direct():
    print(file_path.get())
    print(os.path.isdir(file_path.get()))
    if os.path.isdir(file_path.get()):
        l = filedialog.askdirectory(title='Move files to', initialdir=file_path.get())
    else:
        l = filedialog.askdirectory(title='Move files to', initialdir=os.path.expanduser('~'))
        file_path.delete(0,END)
        file_path.insert(0,l)

    folder_path.set(l)


def rename():
    brr = ext_choosen.get()
    folder = folder_path.get()
    file_list = os.listdir(folder)
    print('Folder to:', folder)
    suc = mb.showinfo('Succes', f'Your files are renamed')

    def enumeration():
        print('====== numerek')
        number = 0
        for element in file_list:
            print(element)
            number += 1
            numbero = str(number)
            m = os.path.splitext(element)
            shutil.move(f'{folder}/{element}', f'{folder}/{numbero}{m[1]}')

        file_list2 = os.listdir(folder)
        print(file_list2)
        suc
    def enumerate_name():
        pattern_name = dsa.get()


        number = 0
        for element in file_list:
            print(element)
            number += 1
            numbero = str(number)
            m = os.path.splitext(element)
            os.rename(f'{folder}/{element}', f'{folder}/{numbero}{pattern_name}{m[1]}')

        file_list2 = os.listdir(folder)
        print(file_list2)
        suc
    def name_enumerate():
        pattern_name = dsa.get()
        print('======= nazwa numer')
        print(file_path.get())
        # print(' Enter the file name you want to use for renaming your files.')
        # pattern_name = input('Enter name: ')
        number = 0
        if 'copy' not in os.listdir(folder):
            os.mkdir(f'{folder}/copy')

        for element in file_list:
            print(element)

            m = os.path.splitext(element)

            if os.path.isfile(f'{folder}/{element}'):
                number += 1
                numbero = str(number)
                shutil.copy2(f'{folder}/{element}', f'{folder}/copy')
                os.rename(f'{folder}/{element}', f'{folder}/{pattern_name}{numbero}{m[1]}')

        file_list2 = os.listdir(folder)
        print(file_list2)
        suc

    print('brr to:', brr)
    if brr == 'Enumerate':
        print('Enumerate')
        enumeration()
    elif brr == 'By Enumeration Name':
        print('By Enumeration Name')
        enumerate_name()
    else:
        print('name_numer')
        name_enumerate()

def moveq():
    print(f'to:{len(folder_tom.get())} From:{len(folder_path.get())} Ext: {len(ext_choosen.get())}')
    if len(ext_choosen.get()) < 1 or len(folder_path.get()) < 1:
        mb.showerror('Wrong', 'You\'ve to select Source and renaming pattern. ')
        return
    if mb.askyesno('sure?', f'Do you want to rename files in: {folder_path.get()}?'):
        rename()
    else:
        mb.showinfo('No', 'Renaming files has been canceled')


def forget():
    dsa.grid_remove()
    c.grid_remove()


def callbackFunc(n):
    brocha.set(n)

    if brr == 0 or brr == -1:
        forget()

    print(ext_choosen.current())
    if ext_choosen.current() > 0:
        dsa.grid(row=4, column=1)
        c.grid(row=4, column=0)


# ---------------------------


brocha=StringVar()
movefrom = Label(canvas,text=' Rename files in: ', fg='white', bg=backg, font=10)
movefrom.grid(column=0, row=0)

file_path = Entry(canvas,width=30)
file_path.grid(column=1,row=0)

butonem = Button(canvas,text='Directory', command=direct, fg='orange', bg='#0f2a52', highlightthickness=0)
butonem.grid(column=2, row=0, padx=10, pady=10)
folder_path = StringVar()
folder_tom = StringVar()
print('first>',folder_path.get())
print('first',len((folder_path.get())))

po = []
pliki=[]
bgs=Button(canvas,text="Vimart 1.0\n Bulk File Renamer",
          background = '#0f2a52', foreground ="orange",
          font = ("Times New Roman", 15, 'bold'),command=me).grid(column=1,row=2)

Label(canvas,text = "Choose the way you want to\n rename your files:" ,bg=backg, fg='white', font=10).grid(column = 0,row = 3, padx = 10, pady = 10)

kl = StringVar()
ext_choosen = ttk.Combobox(canvas,width = 27)
point= ['All files']
ext_choosen['values'] = ('Enumerate','By Enumaration Name', 'By name and Enumerate')

ext_choosen.grid(column=1, row=3)

print(po)
ext_choosen.bind("<<ComboboxSelected>>", callbackFunc)

# ----------------- Move to ---------------#


def ent(e):
    butone_to['background'] = '#0f2a52'


def leave(e):
    butone_to['background']='#0f2a52'

dsa = Entry(canvas, width=20)
dsa.grid(row=4, column=1)
c = Label(canvas,text='Enter pattern name', fg='white', font='bold', bg=backg)
c.grid(row=4, column=0, padx=10)

brr = ext_choosen.current()
if brr ==-1:
    forget()

a = Button(canvas,text='Rename', command= moveq).grid(column=1, row=8,pady=10)


root.mainloop()
