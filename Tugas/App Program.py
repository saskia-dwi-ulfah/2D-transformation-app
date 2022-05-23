# SASKIA DWI ULFAH
# 19/439822/TK/48552
# TUGAS TRANSFORMASI 2D

# Import package yang diperlukan
from tkinter import *
import math
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure 

# fungsi ketika tombol 'Translation' dipencet
def openTranslation():
    global window_Translation
    window_Translation = Toplevel(root)
    window_Translation.title("2D Transformation - Translation")
    window_Translation.geometry("500x500")
    window_Translation.resizable(False, False)
    
    tx_label = Label(window_Translation, text="Komponen x vektor translasi (Tx):")
    tx_label.place(x=110, y=330)
    ty_label = Label(window_Translation, text="Komponen y vektor translasi (Ty):")
    ty_label.place(x=110, y=360)
    
    tx = Entry(window_Translation, width=8, borderwidth=3)
    tx.place(x=295, y=330)
    ty = Entry(window_Translation, width=8, borderwidth=3)
    ty.place(x=295, y=360)

    btn_plot = Button(
        window_Translation, 
        text="Plot", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white", 
        command=lambda: plot(x+float(tx.get()), y+float(ty.get()), window_Translation, "Setelah Translasi"))
    btn_plot.place(x=190, y=395)

    btn_back = Button(
        window_Translation, 
        text="Kembali", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white", 
        command=lambda: window_Translation.destroy())
    btn_back.place(x=190, y=425)

    nama = Label(window_Translation, text="Saskia Dwi Ulfah")
    nama.place(x=431, y=475, anchor ='se')
    nim = Label(window_Translation, text="19/439822/TK/48552")
    nim.place(x=450, y=495, anchor ='se')

# fungsi ketika tombol 'Scaling' dipencet
def openScaling():
    global window_Scaling
    window_Scaling = Toplevel(root)
    window_Scaling.title("2D Transformation - Scaling")
    window_Scaling.geometry("500x500")
    window_Scaling.resizable(False, False)

    x_factor_label = Label(window_Scaling, text="Faktor Penskalaan x:")
    x_factor_label.place(x=145, y=330)
    y_factor_label = Label(window_Scaling, text="Faktor Penskalaan y:")
    y_factor_label.place(x=145, y=360)

    x_scaling_factor = Entry(window_Scaling, width=8, borderwidth=3)
    x_scaling_factor.place(x=260, y=330)
    y_scaling_factor = Entry(window_Scaling, width=8, borderwidth=3)
    y_scaling_factor.place(x=260, y=360)

    btn_plot = Button(
        window_Scaling, 
        text="Plot", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white", 
        command=lambda: plot(x*float(x_scaling_factor.get()), y*float(y_scaling_factor.get()), window_Scaling, "Setelah Penskalaan"))
    btn_plot.place(x=190, y=395)

    btn_back = Button(
        window_Scaling, 
        text="Kembali", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white", 
        command=lambda: window_Scaling.destroy())
    btn_back.place(x=190, y=425)

    nama = Label(window_Scaling, text="Saskia Dwi Ulfah")
    nama.place(x=431, y=475, anchor ='se')
    nim = Label(window_Scaling, text="19/439822/TK/48552")
    nim.place(x=450, y=495, anchor ='se')

# fungsi ketika tombol 'Rotation' dipencet
def openRotation():
    global window_Rotation
    window_Rotation = Toplevel(root)
    window_Rotation.title("2D Transformation - Rotation")
    window_Rotation.geometry("500x500")
    window_Rotation.resizable(False, False)

    degree_label = Label(window_Rotation, text="Sudut putar (derajat):")
    degree_label.place(x=80, y=330)
    arah_rotasi_label = Label(window_Rotation, text="Arah rotasi:")
    arah_rotasi_label.place(x=80, y=370)
    sumbu_rotasi_label = Label(window_Rotation, text="Sumbu rotasi:")
    sumbu_rotasi_label.place(x=80, y=420)

    degree = Entry(window_Rotation, width=8, borderwidth=3)
    degree.place(x=80, y=350)

    arah_rotasi = ['Berlawanan jarum jam', 'Searah jarum jam']
    clicked= StringVar()
    clicked.set(arah_rotasi[0])

    dropdown = OptionMenu(window_Rotation, clicked, *arah_rotasi)
    dropdown.place(x=80, y=390)

    sumbu_rotasi_x = Entry(window_Rotation, width=8, borderwidth=3)
    sumbu_rotasi_x.place(x=80, y=440)
    sumbu_rotasi_y = Entry(window_Rotation, width=8, borderwidth=3)
    sumbu_rotasi_y.place(x=138, y=440)

    btn_plot = Button(
        window_Rotation, 
        text="Plot", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white",
        command= lambda: doRotation(degree.get(), clicked.get(), sumbu_rotasi_x.get(), sumbu_rotasi_y.get()))
    btn_plot.place(x=300, y=370)

    btn_back = Button(
        window_Rotation, 
        text="Kembali", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white", 
        command=lambda: window_Rotation.destroy())
    btn_back.place(x=300, y=400)

    nama = Label(window_Rotation, text="Saskia Dwi Ulfah")
    nama.place(x=431, y=475, anchor ='se')
    nim = Label(window_Rotation, text="19/439822/TK/48552")
    nim.place(x=450, y=495, anchor ='se')

# fungsi ketika tombol 'Shearing' dipencet
def openShearing():
    global window_Shearing
    window_Shearing = Toplevel(root)
    window_Shearing.title("2D Transformation - Shearing")
    window_Shearing.geometry("500x500")
    window_Shearing.resizable(False, False)

    shearing_mode_label = Label(window_Shearing, text="Shearing mode:")
    shearing_mode_label.place(x=160, y=320)
    Shx_label = Label(window_Shearing, text="Shx:")
    Shx_label.place(x=160, y=350)
    Shy_label = Label(window_Shearing, text="Shy:")
    Shy_label.place(x=250, y=350)
 
    shearing_mode= ['X Shear', 'Y Shear', 'XY Shear']
    clicked= StringVar()
    clicked.set(shearing_mode[0])

    dropdown = OptionMenu(window_Shearing, clicked, *shearing_mode)
    dropdown.place(x=250, y=315)

    Shx = Entry(window_Shearing, width=8, borderwidth=3)
    Shx.place(x=190, y=350)
    Shy = Entry(window_Shearing, width=8, borderwidth=3)
    Shy.place(x=280, y=350)

    btn_plot = Button(
        window_Shearing, 
        text="Plot", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white",
        command= lambda: doShearing(clicked.get(), float(Shx.get()), float(Shy.get())))
    btn_plot.place(x=190, y=390)

    btn_back = Button(
        window_Shearing, 
        text="Kembali", 
        relief="ridge", 
        height=1, 
        width=15, 
        bg="white", 
        command=lambda: window_Shearing.destroy())
    btn_back.place(x=190, y=420)

    nama = Label(window_Shearing, text="Saskia Dwi Ulfah")
    nama.place(x=431, y=475, anchor ='se')
    nim = Label(window_Shearing, text="19/439822/TK/48552")
    nim.place(x=450, y=495, anchor ='se')

# fungsi untuk plot hasil transformasi
def plot(x, y, master, title):
    figure = Figure(figsize=(4.5,3), dpi=100)
    
    ax = figure.add_subplot(111, title=title)
    ax.plot(x,y, marker='o')
    
    canvas = FigureCanvasTkAgg(figure, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

# fungsi untuk melakukan rotasi
def doRotation(sudut_putar, arah_rotasi, sumbu_rotasi_x, sumbu_rotasi_y):
    rad = float(sudut_putar) * (math.pi/180)
    px = float(sumbu_rotasi_x)
    py = float(sumbu_rotasi_y)

    if arah_rotasi=='Berlawanan jarum jam':
        teta = rad
    elif arah_rotasi=='Searah jarum jam':
        teta = -rad
    
    x_aksen = x*math.cos(teta)-y*math.sin(teta)-px*math.cos(teta)+py*math.sin(teta)+px
    y_aksen = x*math.sin(teta)+y*math.cos(teta)-px*math.sin(teta)-py*math.cos(teta)+py
    
    plot(x_aksen, y_aksen, window_Rotation, "Setelah Rotasi")

# fungsi untuk melakukan shearing
def doShearing(shearing_mode, shx, shy):
    if shearing_mode=='X Shear':
        x_aksen = x + shx*y
        y_aksen = y
    elif shearing_mode=='Y Shear':
        x_aksen = x
        y_aksen = y + shy*x
    elif shearing_mode=='XY Shear':
        x_aksen = x + shx*y
        y_aksen = y + shy*x

    plot(x_aksen, y_aksen, window_Shearing, "Setelah Shearing")

#-------------------------------------------------------------------------------------------------------------------------------------
#MAIN PROGRAM 

# window utama
root = Tk()
root.title("2D Transformation")
root.geometry("500x500")
root.resizable(False, False)

# koordinat geometri
x = np.array(([1,3,1,1]))
y = np.array(([2,6,6,2]))

# konfigurasi tampilan window utama
bt_translation = Button(root, text="Translation", relief="ridge", height=1, width=15, bg="white", command=openTranslation)
bt_translation.place(x=125, y=350)

bt_scaling = Button(root, text="Scaling", relief="ridge", height=1, width=15, bg="white", command=openScaling)
bt_scaling.place(x=245, y=350)

bt_rotation = Button(root, text="Rotation", relief="ridge", height=1, width=15, bg="white", command=openRotation)
bt_rotation.place(x=125, y=380)

bt_shearing = Button(root, text="Shearing", relief="ridge", height=1, width=15, bg="white", command=openShearing)
bt_shearing.place(x=245, y=380)

nama = Label(root, text="Saskia Dwi Ulfah")
nama.place(x=431, y=475, anchor ='se')
nim = Label(root, text="19/439822/TK/48552")
nim.place(x=450, y=495, anchor ='se')

figure = Figure(figsize=(4.5,3), dpi=100)

plot1 = figure.add_subplot(111, title="Gambar Awal")
plot1.plot(x,y, marker='o')

canvas = FigureCanvasTkAgg(figure, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=25)

root.mainloop()