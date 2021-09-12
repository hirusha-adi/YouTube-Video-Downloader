#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Sep 02, 2021 09:00:01 AM +0530  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import home_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    home_support.set_Tk_var()
    top = MainWindowHome (root)
    home_support.init(root, top)
    root.mainloop()

w = None
def create_MainWindowHome(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_MainWindowHome(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    home_support.set_Tk_var()
    top = MainWindowHome (w)
    home_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_MainWindowHome():
    global w
    w.destroy()
    w = None

class MainWindowHome:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("705x487+731+179")
        top.minsize(117, 1)
        top.maxsize(4644, 1274)
        top.resizable(1,  1)
        top.title("Downloader by ZeaCeR")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Topic = tk.Label(top)
        self.Topic.place(relx=-0.014, rely=0.021, height=65, width=721)
        self.Topic.configure(activebackground="#ffffff")
        self.Topic.configure(activeforeground="#fd0006")
        self.Topic.configure(background="#ffffff")
        self.Topic.configure(disabledforeground="#a3a3a3")
        self.Topic.configure(font="-family {Snap ITC} -size 24")
        self.Topic.configure(foreground="#ff2227")
        self.Topic.configure(highlightbackground="#d9d9d9")
        self.Topic.configure(highlightcolor="black")
        self.Topic.configure(text='''Downloader''')

        self.urlhere = tk.Entry(top)
        self.urlhere.place(relx=0.033, rely=0.257, height=50, relwidth=0.63)
        self.urlhere.configure(background="#eeeeee")
        self.urlhere.configure(disabledforeground="#a3a3a3")
        self.urlhere.configure(font="-family {Courier New} -size 17")
        self.urlhere.configure(foreground="#000000")
        self.urlhere.configure(highlightbackground="#d9d9d9")
        self.urlhere.configure(highlightcolor="black")
        self.urlhere.configure(insertbackground="black")
        self.urlhere.configure(selectbackground="blue")
        self.urlhere.configure(selectforeground="white")

        self.btnpaste = tk.Button(top)
        self.btnpaste.place(relx=0.681, rely=0.259, height=44, width=147)
        self.btnpaste.configure(activebackground="#ececec")
        self.btnpaste.configure(activeforeground="#000000")
        self.btnpaste.configure(background="#1abe07")
        self.btnpaste.configure(disabledforeground="#4646ff")
        self.btnpaste.configure(font="-family {Yu Gothic UI Semilight} -size 16")
        self.btnpaste.configure(foreground="#ffffff")
        self.btnpaste.configure(highlightbackground="#d2dcdf")
        self.btnpaste.configure(highlightcolor="#000000")
        self.btnpaste.configure(pady="0")
        self.btnpaste.configure(text='''+ Paste''')

        self.btndownload = tk.Button(top)
        self.btndownload.place(relx=0.709, rely=0.493, height=184, width=187)
        self.btndownload.configure(activebackground="#f00006")
        self.btndownload.configure(activeforeground="white")
        self.btndownload.configure(activeforeground="#000000")
        self.btndownload.configure(background="#1681c0")
        self.btndownload.configure(disabledforeground="#a3a3a3")
        self.btndownload.configure(font="-family {Showcard Gothic} -size 18")
        self.btndownload.configure(foreground="#ffffff")
        self.btndownload.configure(highlightbackground="#d9d9d9")
        self.btndownload.configure(highlightcolor="black")
        self.btndownload.configure(pady="0")
        self.btndownload.configure(text='''⬇ Download''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.894, rely=0.259, height=44, width=57)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff5155")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Showcard Gothic} -size 17")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''X''')

        self.Topic_1 = tk.Label(top)
        self.Topic_1.place(relx=0.028, rely=0.179, height=33, width=61)
        self.Topic_1.configure(activebackground="#ffffff")
        self.Topic_1.configure(activeforeground="#fd0006")
        self.Topic_1.configure(background="#ffffff")
        self.Topic_1.configure(disabledforeground="#a3a3a3")
        self.Topic_1.configure(font="-family {Yu Gothic UI Semilight} -size 17")
        self.Topic_1.configure(foreground="#ff2227")
        self.Topic_1.configure(highlightbackground="#d9d9d9")
        self.Topic_1.configure(highlightcolor="black")
        self.Topic_1.configure(text='''Link''')

        self.p1080 = tk.Radiobutton(top)
        self.p1080.place(relx=0.057, rely=0.696, relheight=0.055, relwidth=0.123)

        self.p1080.configure(activebackground="#ececec")
        self.p1080.configure(activeforeground="#000000")
        self.p1080.configure(background="#ffffff")
        self.p1080.configure(disabledforeground="#a3a3a3")
        self.p1080.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p1080.configure(foreground="#000000")
        self.p1080.configure(highlightbackground="#d9d9d9")
        self.p1080.configure(highlightcolor="black")
        self.p1080.configure(justify='left')
        self.p1080.configure(text='''1080p''')
        self.p1080.configure(variable=home_support.selectedButton)

        self.p720 = tk.Radiobutton(top)
        self.p720.place(relx=0.057, rely=0.795, relheight=0.055, relwidth=0.123)
        self.p720.configure(activebackground="#ececec")
        self.p720.configure(activeforeground="#000000")
        self.p720.configure(background="white")
        self.p720.configure(disabledforeground="#a3a3a3")
        self.p720.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p720.configure(foreground="#000000")
        self.p720.configure(highlightbackground="#d9d9d9")
        self.p720.configure(highlightcolor="black")
        self.p720.configure(justify='left')
        self.p720.configure(text='''720p''')
        self.p720.configure(variable=home_support.selectedButton)

        self.p480 = tk.Radiobutton(top)
        self.p480.place(relx=0.199, rely=0.497, relheight=0.055, relwidth=0.122)
        self.p480.configure(activebackground="#ececec")
        self.p480.configure(activeforeground="#000000")
        self.p480.configure(background="white")
        self.p480.configure(disabledforeground="#a3a3a3")
        self.p480.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p480.configure(foreground="#000000")
        self.p480.configure(highlightbackground="#d9d9d9")
        self.p480.configure(highlightcolor="black")
        self.p480.configure(justify='left')
        self.p480.configure(text='''480p''')
        self.p480.configure(variable=home_support.selectedButton)

        self.p360 = tk.Radiobutton(top)
        self.p360.place(relx=0.199, rely=0.595, relheight=0.057, relwidth=0.123)
        self.p360.configure(activebackground="#ececec")
        self.p360.configure(activeforeground="#000000")
        self.p360.configure(background="white")
        self.p360.configure(disabledforeground="#a3a3a3")
        self.p360.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p360.configure(foreground="#000000")
        self.p360.configure(highlightbackground="#d9d9d9")
        self.p360.configure(highlightcolor="black")
        self.p360.configure(justify='left')
        self.p360.configure(text='''360p''')
        self.p360.configure(variable=home_support.selectedButton)

        self.p240 = tk.Radiobutton(top)
        self.p240.place(relx=0.199, rely=0.696, relheight=0.055, relwidth=0.123)
        self.p240.configure(activebackground="#ececec")
        self.p240.configure(activeforeground="#000000")
        self.p240.configure(background="white")
        self.p240.configure(disabledforeground="#a3a3a3")
        self.p240.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p240.configure(foreground="#000000")
        self.p240.configure(highlightbackground="#d9d9d9")
        self.p240.configure(highlightcolor="black")
        self.p240.configure(justify='left')
        self.p240.configure(text='''240p''')
        self.p240.configure(variable=home_support.selectedButton)

        self.p144 = tk.Radiobutton(top)
        self.p144.place(relx=0.199, rely=0.795, relheight=0.055, relwidth=0.123)
        self.p144.configure(activebackground="#ececec")
        self.p144.configure(activeforeground="#000000")
        self.p144.configure(background="white")
        self.p144.configure(disabledforeground="#a3a3a3")
        self.p144.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p144.configure(foreground="#000000")
        self.p144.configure(highlightbackground="#d9d9d9")
        self.p144.configure(highlightcolor="black")
        self.p144.configure(justify='left')
        self.p144.configure(text='''144p''')
        self.p144.configure(variable=home_support.selectedButton)

        self.f64kbps = tk.Radiobutton(top)
        self.f64kbps.place(relx=0.525, rely=0.591, relheight=0.055
                , relwidth=0.149)
        self.f64kbps.configure(activebackground="#ececec")
        self.f64kbps.configure(activeforeground="#000000")
        self.f64kbps.configure(background="#ffffff")
        self.f64kbps.configure(disabledforeground="#a3a3a3")
        self.f64kbps.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.f64kbps.configure(foreground="#000000")
        self.f64kbps.configure(highlightbackground="#d9d9d9")
        self.f64kbps.configure(highlightcolor="black")
        self.f64kbps.configure(justify='left')
        self.f64kbps.configure(text='''64kbps''')
        self.f64kbps.configure(variable=home_support.selectedButton)

        self.f32kbps = tk.Radiobutton(top)
        self.f32kbps.place(relx=0.525, rely=0.69, relheight=0.055
                , relwidth=0.148)
        self.f32kbps.configure(activebackground="#ececec")
        self.f32kbps.configure(activeforeground="#000000")
        self.f32kbps.configure(background="#ffffff")
        self.f32kbps.configure(disabledforeground="#a3a3a3")
        self.f32kbps.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.f32kbps.configure(foreground="#000000")
        self.f32kbps.configure(highlightbackground="#d9d9d9")
        self.f32kbps.configure(highlightcolor="black")
        self.f32kbps.configure(justify='left')
        self.f32kbps.configure(text='''32kbps''')
        self.f32kbps.configure(variable=home_support.selectedButton)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.335, rely=0.48,  relheight=0.398)
        self.TSeparator1.configure(orient="vertical")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="File")
        self.sub_menu.add_command(
                label="Paste URL")
        self.sub_menu.add_command(
                label="Exit")
        self.menubar.add_separator(
)
        self.sub_menu1 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="Others")
        self.sub_menu1.add_command(
                label="Credits")

        self.TSeparator1_1 = ttk.Separator(top)
        self.TSeparator1_1.place(relx=0.044, rely=0.476,  relheight=0.398)
        self.TSeparator1_1.configure(orient="vertical")

        self.Lcreditsbottom = tk.Label(top)
        self.Lcreditsbottom.place(relx=0.014, rely=0.947, height=25, width=687)
        self.Lcreditsbottom.configure(activebackground="#f9f9f9")
        self.Lcreditsbottom.configure(activeforeground="black")
        self.Lcreditsbottom.configure(background="#ffffff")
        self.Lcreditsbottom.configure(disabledforeground="#a3a3a3")
        self.Lcreditsbottom.configure(foreground="#000000")
        self.Lcreditsbottom.configure(highlightbackground="#d9d9d9")
        self.Lcreditsbottom.configure(highlightcolor="black")
        self.Lcreditsbottom.configure(text='''Downloader by ZeaCeR#5641 - v0.3''')

        self.p1080_1 = tk.Radiobutton(top)
        self.p1080_1.place(relx=0.057, rely=0.595, relheight=0.057
                , relwidth=0.123)
        self.p1080_1.configure(activebackground="#ececec")
        self.p1080_1.configure(activeforeground="#000000")
        self.p1080_1.configure(background="#ffffff")
        self.p1080_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p1080_1.configure(foreground="#000000")
        self.p1080_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1.configure(highlightcolor="black")
        self.p1080_1.configure(justify='left')
        self.p1080_1.configure(text='''1440p''')
        self.p1080_1.configure(variable=home_support.selectedButton)

        self.p1080_1_1 = tk.Radiobutton(top)
        self.p1080_1_1.place(relx=0.057, rely=0.497, relheight=0.057
                , relwidth=0.123)
        self.p1080_1_1.configure(activebackground="#ececec")
        self.p1080_1_1.configure(activeforeground="#000000")
        self.p1080_1_1.configure(background="#ffffff")
        self.p1080_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1.configure(font="-family {Yu Gothic UI Semilight} -size 12")
        self.p1080_1_1.configure(foreground="#000000")
        self.p1080_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1.configure(highlightcolor="black")
        self.p1080_1_1.configure(justify='left')
        self.p1080_1_1.configure(text='''2160p''')
        self.p1080_1_1.configure(variable=home_support.selectedButton)

        self.f128kbps = tk.Radiobutton(top)
        self.f128kbps.place(relx=0.525, rely=0.497, relheight=0.055
                , relwidth=0.148)
        self.f128kbps.configure(activebackground="#ececec")
        self.f128kbps.configure(activeforeground="#000000")
        self.f128kbps.configure(background="#ffffff")
        self.f128kbps.configure(disabledforeground="#a3a3a3")
        self.f128kbps.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.f128kbps.configure(foreground="#000000")
        self.f128kbps.configure(highlightbackground="#d9d9d9")
        self.f128kbps.configure(highlightcolor="black")
        self.f128kbps.configure(justify='left')
        self.f128kbps.configure(text='''128kbps''')
        self.f128kbps.configure(variable=home_support.selectedButton)

        self.f160kbps = tk.Radiobutton(top)
        self.f160kbps.place(relx=0.355, rely=0.795, relheight=0.055
                , relwidth=0.149)
        self.f160kbps.configure(activebackground="#ececec")
        self.f160kbps.configure(activeforeground="#000000")
        self.f160kbps.configure(background="#ffffff")
        self.f160kbps.configure(disabledforeground="#a3a3a3")
        self.f160kbps.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.f160kbps.configure(foreground="#000000")
        self.f160kbps.configure(highlightbackground="#d9d9d9")
        self.f160kbps.configure(highlightcolor="black")
        self.f160kbps.configure(justify='left')
        self.f160kbps.configure(text='''160kbps''')
        self.f160kbps.configure(variable=home_support.selectedButton)

        self.f192kbps = tk.Radiobutton(top)
        self.f192kbps.place(relx=0.355, rely=0.696, relheight=0.055
                , relwidth=0.149)
        self.f192kbps.configure(activebackground="#ececec")
        self.f192kbps.configure(activeforeground="#000000")
        self.f192kbps.configure(background="#ffffff")
        self.f192kbps.configure(disabledforeground="#a3a3a3")
        self.f192kbps.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.f192kbps.configure(foreground="#000000")
        self.f192kbps.configure(highlightbackground="#d9d9d9")
        self.f192kbps.configure(highlightcolor="black")
        self.f192kbps.configure(justify='left')
        self.f192kbps.configure(text='''192kbps''')
        self.f192kbps.configure(variable=home_support.selectedButton)

        self.f256kbps = tk.Radiobutton(top)
        self.f256kbps.place(relx=0.355, rely=0.595, relheight=0.057
                , relwidth=0.149)
        self.f256kbps.configure(activebackground="#ececec")
        self.f256kbps.configure(activeforeground="#000000")
        self.f256kbps.configure(background="#ffffff")
        self.f256kbps.configure(disabledforeground="#a3a3a3")
        self.f256kbps.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.f256kbps.configure(foreground="#000000")
        self.f256kbps.configure(highlightbackground="#d9d9d9")
        self.f256kbps.configure(highlightcolor="black")
        self.f256kbps.configure(justify='left')
        self.f256kbps.configure(text='''256kbps''')
        self.f256kbps.configure(variable=home_support.selectedButton)

        self.f320kbps = tk.Radiobutton(top)
        self.f320kbps.place(relx=0.355, rely=0.497, relheight=0.057
                , relwidth=0.149)
        self.f320kbps.configure(activebackground="#ececec")
        self.f320kbps.configure(activeforeground="#000000")
        self.f320kbps.configure(background="#ffffff")
        self.f320kbps.configure(disabledforeground="#a3a3a3")
        self.f320kbps.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.f320kbps.configure(foreground="#000000")
        self.f320kbps.configure(highlightbackground="#d9d9d9")
        self.f320kbps.configure(highlightcolor="black")
        self.f320kbps.configure(justify='left')
        self.f320kbps.configure(text='''320kbps''')
        self.f320kbps.configure(variable=home_support.selectedButton)

        self.p1080_1_1_1 = tk.Radiobutton(top)
        self.p1080_1_1_1.place(relx=0.028, rely=0.38, relheight=0.06
                , relwidth=0.18)
        self.p1080_1_1_1.configure(activebackground="#ececec")
        self.p1080_1_1_1.configure(activeforeground="#000000")
        self.p1080_1_1_1.configure(background="#ffffff")
        self.p1080_1_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1_1.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p1080_1_1_1.configure(foreground="#000000")
        self.p1080_1_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1_1.configure(highlightcolor="black")
        self.p1080_1_1_1.configure(justify='left')
        self.p1080_1_1_1.configure(text='''Playlist''')
        self.p1080_1_1_1.configure(variable=home_support.selectedButton)

        self.p1080_1_1_1_1 = tk.Radiobutton(top)
        self.p1080_1_1_1_1.place(relx=0.255, rely=0.38, relheight=0.06
                , relwidth=0.18)
        self.p1080_1_1_1_1.configure(activebackground="#ececec")
        self.p1080_1_1_1_1.configure(activeforeground="#000000")
        self.p1080_1_1_1_1.configure(background="#ffffff")
        self.p1080_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1_1_1.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p1080_1_1_1_1.configure(foreground="#000000")
        self.p1080_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1_1_1.configure(highlightcolor="black")
        self.p1080_1_1_1_1.configure(justify='left')
        self.p1080_1_1_1_1.configure(text='''Video''')
        self.p1080_1_1_1_1.configure(variable=home_support.selectedButton)

        self.p1080_1_1_1_1_1 = tk.Radiobutton(top)
        self.p1080_1_1_1_1_1.place(relx=0.482, rely=0.38, relheight=0.06
                , relwidth=0.18)
        self.p1080_1_1_1_1_1.configure(activebackground="#ececec")
        self.p1080_1_1_1_1_1.configure(activeforeground="#000000")
        self.p1080_1_1_1_1_1.configure(background="#ffffff")
        self.p1080_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1_1_1_1.configure(font="-family {Yu Gothic UI Semilight} -size 13")
        self.p1080_1_1_1_1_1.configure(foreground="#000000")
        self.p1080_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1_1_1_1.configure(highlightcolor="black")
        self.p1080_1_1_1_1_1.configure(justify='left')
        self.p1080_1_1_1_1_1.configure(text='''Channel''')
        self.p1080_1_1_1_1_1.configure(variable=home_support.selectedButton)

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.681, rely=0.476,  relheight=0.4)
        self.TSeparator2.configure(orient="vertical")

if __name__ == '__main__':
    vp_start_gui()




