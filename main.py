# text-box
# dropdown
# checkbox
# radio button

# open file dialog
# submit button -> all inputs need to be filled

# show data
# clear data
# about

# Saya Farhan Nurzaman mengerjakan evaluasi Tugas Praktikum 3 DPBO 
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. 
# Aamiin.

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image 
from Data import Data

imageFile = ""
data = []
gambar = []

def submit():
    global imageFile
    if input1.get() != "" and  input2.get() != "" and input3.get() != "" and imageFile != "":
        temp = Data(input1.get(),input2.get(),input3.get())
        input1.delete(0,'end')
        input2.delete(0,'end')
        input3.delete(0,'end')
        input1.focus()
        data.append(temp)
        img = ImageTk.PhotoImage(Image.open(imageFile).resize((400,400),Image.ANTIALIAS),'rb')
        gambar.append(img)
        messagebox.showinfo(message ="Success!")
        imageFile =""
    else :
        messagebox.showwarning(message ="Please input all fields")
    # label1 = Label(root, text = input1.get())
    # label1.grid(row=6,column=1)
    # label2 = Label(root, text = input2.get())
    # label2.grid(row=7,column=1)
    # label3 = Label(root, text = input3.get())
    # label3.grid(row=8,column=1)

def lihatGambar(index,nama):
    top = Toplevel()
    top.title("Viewing Picture : " + nama)
    b_exit = Button(top, text="Exit", command=top.destroy)
    b_exit.pack()
    canvas = Canvas(top)
    canvas.pack(fill="both",expand=True)

    canvas.create_image(0,0,anchor = "nw" , image = gambar[index])

def clearData():
    confirm = messagebox.askyesno("Are you sure?",message="You are about to clear all data, are you sure?")
    
    if len(data) != 0:
        if confirm:
            data.clear()
            messagebox.showinfo(message="All data has been cleared")
    else:
        messagebox.showwarning("No data", message="There is no available data.")

def showData():
    if len(data) != 0:
        top = Toplevel()
        top.title("Viewing Data")
        show = LabelFrame(top,text="Viewing Data:")
        show.pack(padx=10,pady=10)
        lblIndex = Label(show,text="No",borderwidth=1,relief="solid",width=5)
        lblIndex.grid(row = 0,column=1,pady = 5)

        lblNim = Label(show,text = "NIM",width = 15 , borderwidth=1,relief="solid").grid(row=0,column=2,pady = 5)
        lblNama = Label(show,text = "NAMA",width = 15 , borderwidth=1,relief="solid").grid(row=0,column=3,pady = 5)
        lblKelas = Label(show,text = "KELAS",width = 15 ,borderwidth=1, relief="solid").grid(row=0,column=4,pady = 5)
        
        for i,h in enumerate(data):
            lblIndex = Label(show,text=i+1,borderwidth=1,relief="solid",width=5)
            lblIndex.grid(row = i+1,column=1,pady = 5)

            lblNim = Label(show,text = h.getNim(),width = 15 , borderwidth=1,relief="solid").grid(row=i+1,column=2,pady = 5)
            lblNama = Label(show,text = h.getNama(),width = 15 , borderwidth=1,relief="solid").grid(row=i+1,column=3,pady = 5)
            lblKelas = Label(show,text = h.getKelas(),width = 15 ,borderwidth=1, relief="solid").grid(row=i+1,column=4,pady = 5)
            
            showPicture = Button(show,text = "Show Picture!",command=lambda index=i : lihatGambar(index,h.getNama()))
            showPicture.grid(row=i+1,column=5)


        b_exit = Button(show, text="Exit", command=top.destroy)
        b_exit.grid(row=len(data)+1, column=5)
    else:
        messagebox.showwarning("No data", message="There is no available data.")


def openFile():
    global imageFile
    imageFile = filedialog.askopenfilename(filetypes = (("All image files","*.jpg *.jpeg *.png"),("JPG/JPEG","*.jpg *.jpg"),("PNG","*.png")))
    

def about():
    top = Toplevel()
    top.title("About")
    frame = LabelFrame(top,text = "About",padx=50,pady=50)
    frame.pack(padx=50,pady=50)
    Nama = "Farhan Nurzaman"
    Nim = "1904908"
    tampilkanLabel = Label(frame,text = "Nama : " + Nama + "\n" + "NIM : " + Nim,anchor="w").grid(row=0,column=0,sticky="w")
    b_exit = Button(frame, text="Exit", command=top.destroy)
    b_exit.grid(row=5, column=1)

root = Tk()
root.title("Tugas Praktikum 3 - 1904908 Farhan Nurzaman")
# root.geometry("500x500")

inputLabels = ["Nama","NIM","Kelas"]

frameKiri = Frame(root)
frameKiri.grid(row=0,column=0)
frameKanan = Frame(root)
frameKanan.grid(row=0,column=1,padx=75)

input1 = Entry(frameKiri)
topPad = Label(frameKiri,text="",pady=10)
topPad.grid(row=0)
labelTop = Label(frameKiri,text="Input your data!",pady=10)
labelTop.grid(row=1,column=2)
input1.grid(row=2,column = 2, padx = 5,pady = 10)
lblInput1 = Label(frameKiri,text = inputLabels[0]).grid(row=2,column=1, sticky = "W")
input2 = Entry(frameKiri)
input2.grid(row=3,column = 2,padx = 5,pady = 10)
lblInput2 = Label(frameKiri,text = inputLabels[1]).grid(row=3,column=1, sticky = "W")
input3 = Entry(frameKiri)
input3.grid(row=4,column = 2,padx = 5,pady = 10)
lblInput3 = Label(frameKiri,text = inputLabels[2]).grid(row=4,column=1, sticky = "W")

openImage = Button(frameKiri,text="Open Image", command = openFile)
openImage.grid(row=5,column = 2,pady=5)
submit = Button(frameKiri, text="Submit", command = submit)
submit.grid(row=6,column=2,pady=5)

labelApp = Label(frameKanan,text ="Tugas Praktikum 3",  font = (44))
labelApp.grid(row=0,column=1)
show = Button(frameKanan, text="Show Data",command=showData)
show.grid(row=1,column=1,pady=5)
clear = Button(frameKanan, text="Clear Data",command=clearData)
clear.grid(row=2,column=1,pady=5)
about = Button(frameKanan, text="About",command=about)
about.grid(row=3,column=1,pady=5)

b_exit = Button(root, text="Exit", command=root.quit)
b_exit.grid(row=5, column=1,pady=15)
root.mainloop()