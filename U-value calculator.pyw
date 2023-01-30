#U-value calculator
#By student UNNC
#Python 3.11.1 using Pycharm Editor
#Windows10 (Linux and Mac compatible)
#Module tkinter imported

import tkinter as tk

window = tk.Tk() #create a window
window.title('U value calculator') #set up title name
window.geometry('600x400+460+240') #set up window size
window['background'] = 'LightCyan'#set up window background color

#define the floaterface of material layer selection
def General_calculation_select():
    window_Gc = tk.Toplevel() #create a window
    window_Gc.focus_force() #bring the window to focus
    window_Gc.title('Material number') #set up title name
    window_Gc.geometry('185x200+710+320') #set up window size
    window_Gc['background'] = 'LightCyan' #set up window background color
    text_Gc = tk.Label(window_Gc,text='Number of material layer',bg='white').grid(row=0,pady=10,padx=15,columnspan=2)
    button_Gc1 = tk.Button(window_Gc,text='1 Layer',command=General_calculation1).grid(row=1,column=0,pady=5)
    button_Gc2 = tk.Button(window_Gc,text='2 Layer',command=General_calculation2).grid(row=2,pady=5,padx=5,column=0)
    button_Gc3 = tk.Button(window_Gc,text='3 Layer',command=General_calculation3).grid(row=3,pady=5,padx=5,column=0)
    button_Gc3 = tk.Button(window_Gc,text='4 Layer',command=General_calculation4).grid(row=1,pady=5,column=1)
    button_Gc3 = tk.Button(window_Gc,text='5 Layer',command=General_calculation5).grid(row=2,pady=5,column=1)
    button_Gc3 = tk.Button(window_Gc,text='6 Layer',command=General_calculation6).grid(row=3,pady=5,column=1)
    #define window contents (title and buttons)

#define single-layer material calculation function
def General_calculation1():
    window_GC = tk.Toplevel() #create a window
    window_GC.focus_force() #bring the window to focus
    window_GC.title('General calculation') #set up title name
    window_GC.geometry('430x300+660+300') #set up window size
    window_GC['background'] = 'LightCyan' #set up window background color

    text1_GC = tk.Label(window_GC,text='R_si',bg='LightCyan',font=15).\
        grid(padx=25,pady=30,column=0,row=0)
    text2_GC = tk.Label(window_GC, text='λ', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=1, row=0)
    text3_GC = tk.Label(window_GC, text='d', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=1, row=2)
    text4_GC = tk.Label(window_GC, text='R_se', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=2, row=0)
    #define the text content in the window

    R_si = tk.StringVar()
    R_se = tk.StringVar()
    λ = tk.StringVar()
    d = tk.StringVar()
    #obtain entry box string variable

    #define calculating function
    def calculation():
        Rsi = R_si.get()
        Rse = R_se.get()
        λ_ = λ.get()
        d_ = d.get()
        #define formula variables and obtain the strings

        Rsi = float(Rsi)
        Rse = float(Rse)
        λ_ = float(λ_)
        d_ = float(d_)
        #convert string value to floating point number

        R = λ_/d_
        U = 1/(Rsi+Rse+R)
        #define calculation formula

        Answer = tk.Label(window_GC,text=f'U-value={"%.5f"%U}',font=20,bg='white').\
            grid(padx=15, pady=15,column=1, row=5)
        #define the result display

    entry1_GC = tk.Entry(window_GC,textvariable=R_si,width=12).grid(padx=15,pady=0,column=0,row=1)
    entry2_GC = tk.Entry(window_GC,textvariable=λ,width=12).grid(padx=50,pady=0,column=1,row=1)
    entry3_GC = tk.Entry(window_GC,textvariable=R_se,width=12).grid(padx=15,pady=0,column=2,row=1)
    entry4_GC = tk.Entry(window_GC,textvariable=d,width=12).grid(padx=50, pady=0,column=1, row=3)
    #define the entry box in the interface
    Calculate = tk.Button(window_GC,text='Calculate',command=calculation).grid(padx=20, pady=10,column=1, row=4)
    #define the button to start calculation

#define the two-layer material calculation function
#basically the same as the single-layer material function, but with an additional value of λ and d
#please consult the annotation of single-layer material calculation function
def General_calculation2():
    window_GC = tk.Toplevel()
    window_GC.focus_force()
    window_GC.title('General calculation')
    window_GC.geometry('493x300+660+300')
    window_GC['background'] = 'LightCyan'

    text1_GC = tk.Label(window_GC,text='R_si',bg='LightCyan',font=15).\
        grid(padx=25,pady=30,column=0,row=0)
    text2_GC = tk.Label(window_GC, text='λ', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=1, row=0)
    text3_GC = tk.Label(window_GC, text='d', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=1, row=2)
    text4_GC = tk.Label(window_GC, text='λ_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=2, row=0)
    text5_GC = tk.Label(window_GC, text='d_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=2, row=2)
    text6_GC = tk.Label(window_GC, text='R_se', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=3, row=0)

    R_si = tk.StringVar()
    R_se = tk.StringVar()
    λ = tk.StringVar()
    d = tk.StringVar()
    λ2 = tk.StringVar()
    d2 = tk.StringVar()

    def calculation():
        Rsi = R_si.get()
        Rse = R_se.get()
        λ_ = λ.get()
        d_ = d.get()
        λ_2 = λ2.get()
        d_2 = d2.get()

        Rsi = float(Rsi)
        Rse = float(Rse)
        λ_ = float(λ_)
        d_ = float(d_)
        λ_2 = float(λ_2)
        d_2 = float(d_2)

        R = (λ_/d_)+(λ_2/d_2)
        U = 1/(Rsi+Rse+R)
        Answer = tk.Label(window_GC,text=f'U-value={"%.5f"%U}',font=20,bg='white').\
            grid(padx=15, pady=15,column=1, row=5,columnspan=2)

    entry1_GC = tk.Entry(window_GC,textvariable=R_si,width=12).grid(padx=15,pady=0,column=0,row=1)
    entry2_GC = tk.Entry(window_GC,textvariable=λ,width=12).grid(padx=20,pady=0,column=1,row=1)
    entry3_GC = tk.Entry(window_GC,textvariable=d,width=12).grid(padx=20, pady=0,column=1,row=3)
    entry4_GC = tk.Entry(window_GC,textvariable=λ2,width=12).grid(padx=20, pady=0,column=2,row=1)
    entry5_GC = tk.Entry(window_GC,textvariable=d2,width=12).grid(padx=20, pady=0,column=2,row=3)
    entry6_GC = tk.Entry(window_GC,textvariable=R_se,width=12).grid(padx=15,pady=0,column=3,row=1)
    Calculate = tk.Button(window_GC,text='Calculate',command=calculation).\
        grid(padx=20, pady=10,column=1,row=4,columnspan=2)

#define the third-layer material calculation function
#please consult the annotation of single-layer material calculation function
def General_calculation3():
    window_GC = tk.Toplevel()
    window_GC.focus_force()
    window_GC.title('General calculation')
    window_GC.geometry('623x300+660+300')
    window_GC['background'] = 'LightCyan'

    text1_GC = tk.Label(window_GC,text='R_si',bg='LightCyan',font=15).\
        grid(padx=25,pady=30,column=0,row=0)
    text2_GC = tk.Label(window_GC, text='λ', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=1, row=0)
    text3_GC = tk.Label(window_GC, text='d', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=1, row=2)
    text4_GC = tk.Label(window_GC, text='λ_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=2, row=0)
    text5_GC = tk.Label(window_GC, text='d_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=2, row=2)
    text6_GC = tk.Label(window_GC, text='λ_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=3, row=0)
    text7_GC = tk.Label(window_GC, text='d_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=3, row=2)
    text8_GC = tk.Label(window_GC, text='R_se', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=4, row=0)

    R_si = tk.StringVar()
    R_se = tk.StringVar()
    λ = tk.StringVar()
    d = tk.StringVar()
    λ2 = tk.StringVar()
    d2 = tk.StringVar()
    λ3 = tk.StringVar()
    d3 = tk.StringVar()

    def calculation():
        Rsi = R_si.get()
        Rse = R_se.get()
        λ_ = λ.get()
        d_ = d.get()
        λ_2 = λ2.get()
        d_2 = d2.get()
        λ_3 = λ3.get()
        d_3 = d3.get()

        Rsi = float(Rsi)
        Rse = float(Rse)
        λ_ = float(λ_)
        d_ = float(d_)
        λ_2 = float(λ_2)
        d_2 = float(d_2)
        λ_3 = float(λ_3)
        d_3 = float(d_3)

        R = (λ_/d_)+(λ_2/d_2)+(λ_3/d_3)
        U = 1/(Rsi+Rse+R)
        Answer = tk.Label(window_GC,text=f'U-value={"%.5f"%U}',font=20,bg='white').\
            grid(padx=15, pady=15,column=1,row=5,columnspan=3)

    entry1_GC = tk.Entry(window_GC,textvariable=R_si,width=12).grid(padx=15,pady=0,column=0,row=1)
    entry2_GC = tk.Entry(window_GC,textvariable=λ,width=12).grid(padx=20,pady=0,column=1,row=1)
    entry3_GC = tk.Entry(window_GC,textvariable=d,width=12).grid(padx=20, pady=0,column=1, row=3)
    entry4_GC = tk.Entry(window_GC,textvariable=λ2,width=12).grid(padx=20, pady=0,column=2,row=1)
    entry5_GC = tk.Entry(window_GC,textvariable=d2,width=12).grid(padx=20, pady=0,column=2,row=3)
    entry6_GC = tk.Entry(window_GC, textvariable=λ3, width=12).grid(padx=20, pady=0, column=3, row=1)
    entry7_GC = tk.Entry(window_GC, textvariable=d3, width=12).grid(padx=20, pady=0, column=3, row=3)
    entry8_GC = tk.Entry(window_GC,textvariable=R_se,width=12).grid(padx=15,pady=0,column=4,row=1)
    Calculate = tk.Button(window_GC, text='Calculate', command=calculation).\
        grid(padx=20, pady=10, column=2, row=4)

#define the fourth-layer material calculation function
#please consult the annotation of single-layer material calculation function
def General_calculation4():
    window_GC = tk.Toplevel()
    window_GC.focus_force()
    window_GC.title('General calculation')
    window_GC.geometry('753x300+660+300')
    window_GC['background'] = 'LightCyan'

    text1_GC = tk.Label(window_GC,text='R_si',bg='LightCyan',font=15).\
        grid(padx=25,pady=30,column=0,row=0)
    text2_GC = tk.Label(window_GC, text='λ', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=1, row=0)
    text3_GC = tk.Label(window_GC, text='d', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=1, row=2)
    text4_GC = tk.Label(window_GC, text='λ_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=2, row=0)
    text5_GC = tk.Label(window_GC, text='d_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=2, row=2)
    text6_GC = tk.Label(window_GC, text='λ_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=3, row=0)
    text7_GC = tk.Label(window_GC, text='d_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=3, row=2)
    text8_GC = tk.Label(window_GC, text='λ_4', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=4, row=0)
    text9_GC = tk.Label(window_GC, text='d_4', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=4, row=2)
    text10_GC = tk.Label(window_GC, text='R_se', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=5, row=0)

    R_si = tk.StringVar()
    R_se = tk.StringVar()
    λ = tk.StringVar()
    d = tk.StringVar()
    λ2 = tk.StringVar()
    d2 = tk.StringVar()
    λ3 = tk.StringVar()
    d3 = tk.StringVar()
    λ4 = tk.StringVar()
    d4 = tk.StringVar()

    def calculation():
        Rsi = R_si.get()
        Rse = R_se.get()
        λ_ = λ.get()
        d_ = d.get()
        λ_2 = λ2.get()
        d_2 = d2.get()
        λ_3 = λ3.get()
        d_3 = d3.get()
        λ_4 = λ4.get()
        d_4 = d4.get()

        Rsi = float(Rsi)
        Rse = float(Rse)
        λ_ = float(λ_)
        d_ = float(d_)
        λ_2 = float(λ_2)
        d_2 = float(d_2)
        λ_3 = float(λ_3)
        d_3 = float(d_3)
        λ_4 = float(λ_4)
        d_4 = float(d_4)

        R = (λ_/d_)+(λ_2/d_2)+(λ_3/d_3)+(λ_4/d_4)
        U = 1/(Rsi+Rse+R)
        Answer = tk.Label(window_GC,text=f'U-value={"%.5f"%U}',font=20,bg='white').\
            grid(padx=15, pady=15,column=2,row=5,columnspan=2)

    entry1_GC = tk.Entry(window_GC,textvariable=R_si,width=12).grid(padx=15,pady=0,column=0,row=1)
    entry2_GC = tk.Entry(window_GC,textvariable=λ,width=12).grid(padx=20,pady=0,column=1,row=1)
    entry3_GC = tk.Entry(window_GC,textvariable=d,width=12).grid(padx=20, pady=0,column=1, row=3)
    entry4_GC = tk.Entry(window_GC,textvariable=λ2,width=12).grid(padx=20, pady=0,column=2,row=1)
    entry5_GC = tk.Entry(window_GC,textvariable=d2,width=12).grid(padx=20, pady=0,column=2,row=3)
    entry6_GC = tk.Entry(window_GC, textvariable=λ3, width=12).grid(padx=20, pady=0, column=3, row=1)
    entry7_GC = tk.Entry(window_GC, textvariable=d3, width=12).grid(padx=20, pady=0, column=3, row=3)
    entry8_GC = tk.Entry(window_GC, textvariable=λ4, width=12).grid(padx=20, pady=0, column=4, row=1)
    entry9_GC = tk.Entry(window_GC, textvariable=d4, width=12).grid(padx=20, pady=0, column=4, row=3)
    entry10_GC = tk.Entry(window_GC,textvariable=R_se,width=12).grid(padx=15,pady=0,column=5,row=1)
    Calculate = tk.Button(window_GC, text='Calculate', command=calculation).\
        grid(padx=20,pady=10,column=2,row=4,columnspan=2)

#define the fifth-layer material calculation function
#please consult the annotation of single-layer material calculation function
def General_calculation5():
    window_GC = tk.Toplevel()
    window_GC.focus_force()
    window_GC.title('General calculation')
    window_GC.geometry('883x300+660+300')
    window_GC['background'] = 'LightCyan'

    text1_GC = tk.Label(window_GC,text='R_si',bg='LightCyan',font=15).\
        grid(padx=25,pady=30,column=0,row=0)
    text2_GC = tk.Label(window_GC, text='λ', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=1, row=0)
    text3_GC = tk.Label(window_GC, text='d', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=1, row=2)
    text4_GC = tk.Label(window_GC, text='λ_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=2, row=0)
    text5_GC = tk.Label(window_GC, text='d_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=2, row=2)
    text6_GC = tk.Label(window_GC, text='λ_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=3, row=0)
    text7_GC = tk.Label(window_GC, text='d_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=3, row=2)
    text8_GC = tk.Label(window_GC, text='λ_4', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=4, row=0)
    text9_GC = tk.Label(window_GC, text='d_4', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=4, row=2)
    text10_GC = tk.Label(window_GC, text='λ_5', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=5, row=0)
    text11_GC = tk.Label(window_GC, text='d_5', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=5, row=2)
    text12_GC = tk.Label(window_GC, text='R_se', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=6, row=0)

    R_si = tk.StringVar()
    R_se = tk.StringVar()
    λ = tk.StringVar()
    d = tk.StringVar()
    λ2 = tk.StringVar()
    d2 = tk.StringVar()
    λ3 = tk.StringVar()
    d3 = tk.StringVar()
    λ4 = tk.StringVar()
    d4 = tk.StringVar()
    λ5 = tk.StringVar()
    d5 = tk.StringVar()

    def calculation():
        Rsi = R_si.get()
        Rse = R_se.get()
        λ_ = λ.get()
        d_ = d.get()
        λ_2 = λ2.get()
        d_2 = d2.get()
        λ_3 = λ3.get()
        d_3 = d3.get()
        λ_4 = λ4.get()
        d_4 = d4.get()
        λ_5 = λ5.get()
        d_5 = d5.get()

        Rsi = float(Rsi)
        Rse = float(Rse)
        λ_ = float(λ_)
        d_ = float(d_)
        λ_2 = float(λ_2)
        d_2 = float(d_2)
        λ_3 = float(λ_3)
        d_3 = float(d_3)
        λ_4 = float(λ_4)
        d_4 = float(d_4)
        λ_5 = float(λ_5)
        d_5 = float(d_5)

        R = (λ_/d_)+(λ_2/d_2)+(λ_3/d_3)+(λ_4/d_4)+(λ_5/d_5)
        U = 1/(Rsi+Rse+R)
        Answer = tk.Label(window_GC,text=f'U-value={"%.5f"%U}',font=20,bg='white').\
            grid(padx=15, pady=15,column=2,row=5,columnspan=3)

    entry1_GC = tk.Entry(window_GC,textvariable=R_si,width=12).grid(padx=15,pady=0,column=0,row=1)
    entry2_GC = tk.Entry(window_GC,textvariable=λ,width=12).grid(padx=20,pady=0,column=1,row=1)
    entry3_GC = tk.Entry(window_GC,textvariable=d,width=12).grid(padx=20, pady=0,column=1, row=3)
    entry4_GC = tk.Entry(window_GC,textvariable=λ2,width=12).grid(padx=20, pady=0,column=2,row=1)
    entry5_GC = tk.Entry(window_GC,textvariable=d2,width=12).grid(padx=20, pady=0,column=2,row=3)
    entry6_GC = tk.Entry(window_GC, textvariable=λ3, width=12).grid(padx=20, pady=0, column=3, row=1)
    entry7_GC = tk.Entry(window_GC, textvariable=d3, width=12).grid(padx=20, pady=0, column=3, row=3)
    entry8_GC = tk.Entry(window_GC, textvariable=λ4, width=12).grid(padx=20, pady=0, column=4, row=1)
    entry9_GC = tk.Entry(window_GC, textvariable=d4, width=12).grid(padx=20, pady=0, column=4, row=3)
    entry8_GC = tk.Entry(window_GC, textvariable=λ5, width=12).grid(padx=20, pady=0, column=5, row=1)
    entry9_GC = tk.Entry(window_GC, textvariable=d5, width=12).grid(padx=20, pady=0, column=5, row=3)
    entry10_GC = tk.Entry(window_GC,textvariable=R_se,width=12).grid(padx=15,pady=0,column=6,row=1)
    Calculate = tk.Button(window_GC, text='Calculate', command=calculation).\
        grid(padx=20, pady=10,column=2,row=4,columnspan=3)

#define the sixth-layer material calculation function
#please consult the annotation of single-layer material calculation function
def General_calculation6():
    window_GC = tk.Toplevel()
    window_GC.focus_force()
    window_GC.title('General calculation')
    window_GC.geometry('1013x300+660+300')
    window_GC['background'] = 'LightCyan'

    text1_GC = tk.Label(window_GC, text='R_si', bg='LightCyan', font=15). \
        grid(padx=25, pady=30, column=0, row=0)
    text2_GC = tk.Label(window_GC, text='λ', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=1, row=0)
    text3_GC = tk.Label(window_GC, text='d', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=1, row=2)
    text4_GC = tk.Label(window_GC, text='λ_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=2, row=0)
    text5_GC = tk.Label(window_GC, text='d_2', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=2, row=2)
    text6_GC = tk.Label(window_GC, text='λ_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=3, row=0)
    text7_GC = tk.Label(window_GC, text='d_3', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=3, row=2)
    text8_GC = tk.Label(window_GC, text='λ_4', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=4, row=0)
    text9_GC = tk.Label(window_GC, text='d_4', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=4, row=2)
    text10_GC = tk.Label(window_GC, text='λ_5', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=5, row=0)
    text11_GC = tk.Label(window_GC, text='d_5', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=5, row=2)
    text12_GC = tk.Label(window_GC, text='λ_6', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=6, row=0)
    text13_GC = tk.Label(window_GC, text='d_6', bg='LightCyan', font=15). \
        grid(padx=20, pady=15, column=6, row=2)
    text14_GC = tk.Label(window_GC, text='R_se', bg='LightCyan', font=15). \
        grid(padx=20, pady=30, column=7, row=0)

    R_si = tk.StringVar()
    R_se = tk.StringVar()
    λ = tk.StringVar()
    d = tk.StringVar()
    λ2 = tk.StringVar()
    d2 = tk.StringVar()
    λ3 = tk.StringVar()
    d3 = tk.StringVar()
    λ4 = tk.StringVar()
    d4 = tk.StringVar()
    λ5 = tk.StringVar()
    d5 = tk.StringVar()
    λ6 = tk.StringVar()
    d6 = tk.StringVar()

    def calculation():
        Rsi = R_si.get()
        Rse = R_se.get()
        λ_ = λ.get()
        d_ = d.get()
        λ_2 = λ2.get()
        d_2 = d2.get()
        λ_3 = λ3.get()
        d_3 = d3.get()
        λ_4 = λ4.get()
        d_4 = d4.get()
        λ_5 = λ5.get()
        d_5 = d5.get()
        λ_6 = λ6.get()
        d_6 = d6.get()

        Rsi = float(Rsi)
        Rse = float(Rse)
        λ_ = float(λ_)
        d_ = float(d_)
        λ_2 = float(λ_2)
        d_2 = float(d_2)
        λ_3 = float(λ_3)
        d_3 = float(d_3)
        λ_4 = float(λ_4)
        d_4 = float(d_4)
        λ_5 = float(λ_5)
        d_5 = float(d_5)
        λ_6 = float(λ_6)
        d_6 = float(d_6)

        R = (λ_/d_)+(λ_2/d_2)+(λ_3/d_3)+(λ_4/d_4)+(λ_5/d_5)+(λ_6/d_6)
        U = 1/(Rsi+Rse+R)
        Answer = tk.Label(window_GC, text=f'U-value={"%.5f"%U}',font=20,bg='white').\
            grid(padx=15,pady=15,column=3,row=5,columnspan=3)

    entry1_GC = tk.Entry(window_GC, textvariable=R_si, width=12).grid(padx=15, pady=0, column=0, row=1)
    entry2_GC = tk.Entry(window_GC, textvariable=λ, width=12).grid(padx=20, pady=0, column=1, row=1)
    entry3_GC = tk.Entry(window_GC, textvariable=d, width=12).grid(padx=20, pady=0, column=1, row=3)
    entry4_GC = tk.Entry(window_GC, textvariable=λ2, width=12).grid(padx=20, pady=0, column=2, row=1)
    entry5_GC = tk.Entry(window_GC, textvariable=d2, width=12).grid(padx=20, pady=0, column=2, row=3)
    entry6_GC = tk.Entry(window_GC, textvariable=λ3, width=12).grid(padx=20, pady=0, column=3, row=1)
    entry7_GC = tk.Entry(window_GC, textvariable=d3, width=12).grid(padx=20, pady=0, column=3, row=3)
    entry8_GC = tk.Entry(window_GC, textvariable=λ4, width=12).grid(padx=20, pady=0, column=4, row=1)
    entry9_GC = tk.Entry(window_GC, textvariable=d4, width=12).grid(padx=20, pady=0, column=4, row=3)
    entry8_GC = tk.Entry(window_GC, textvariable=λ5, width=12).grid(padx=20, pady=0, column=5, row=1)
    entry9_GC = tk.Entry(window_GC, textvariable=d5, width=12).grid(padx=20, pady=0, column=5, row=3)
    entry8_GC = tk.Entry(window_GC, textvariable=λ6, width=12).grid(padx=20, pady=0, column=6, row=1)
    entry9_GC = tk.Entry(window_GC, textvariable=d6, width=12).grid(padx=20, pady=0, column=6, row=3)
    entry10_GC = tk.Entry(window_GC, textvariable=R_se, width=12).grid(padx=15, pady=0, column=7, row=1)
    Calculate = tk.Button(window_GC, text='Calculate', command=calculation). \
        grid(padx=20, pady=10, column=3, row=4, columnspan=2)

def prompt():
    Box = tk.Toplevel()
    Box.title('Tips')
    Box.geometry('200x100+660+300')
    Box['background'] = 'LightCyan'
    prompt = tk.Label(Box,bg='LightCyan',text='More functions on the way,\nthanks for your patience!')\
        .pack(pady=25)

button1 = tk.Button(window,text='General calculate',font=30,bg='Moccasin',command=General_calculation_select).\
    grid(row=0, column=1,padx=50,pady=50)
button2 = tk.Button(window,text='Wall',font=20,bg='Moccasin',command=prompt).\
    grid(row=1, column=0,padx=50,pady=50)
button3 = tk.Button(window,text='Roof',font=20,bg='Moccasin',command=prompt).\
    grid(row=1, column=1,padx=50,pady=50)
button4 = tk.Button(window,text='Floor',font=20,bg='Moccasin',command=prompt).\
    grid(row=1, column=2,padx=50,pady=50)
#Define main window button
#only the general computing part is open at present
#other functions are still under development,please wait and it will be available soon!

window.mainloop()