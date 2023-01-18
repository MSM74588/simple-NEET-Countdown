
import tkinter
from tkinter import *
import subprocess
from tkcalendar import Calendar
import os
  

import datetime

import sv_ttk
# tk.Tk().

# import os
examname = "NEET 2023"

day = 7
month = 5
year = 2023
# examdate = "MandraSaptak Mandal"



def examdate():
    today = datetime.date.today()
    future = datetime.date(year,month,day)
    diff = future - today
    return diff

def weeksleft():
    weeks = int((examdate().days % 365) / 7)
    return weeks
#### tk parameters

todays_date = datetime.date.today()



windowroot = Tk()
windowroot.geometry("-40+90")
windowroot.title(f"{examname} target")
# windowroot.attributes('-topmost',True, '-type','dock')
windowroot.attributes('-topmost',True)
windowroot.resizable(False,False)
windowroot.config(borderwidth=20)
# windowroot.protocol("WM_DELETE_WINDOW", windowroot.iconify())
        

# label = tk.Label(windowroot, text=examdate, font=('Rubik', 20))
# sidebar = tk.Frame(windowroot, bg="#ccccff").pack()
# # #### SIDE BAR
# icon1 = tk.Label(sidebar, text="MSM").pack()

# end SIDEBAR
rightframe = Frame(windowroot).pack()

label = Label(rightframe, text="Days left for:", font=('Rubik', 20)).pack()
# label.pack()
#### RIGHT FRAME ######
label2 = Label(rightframe, text=examname, font=('Rubik', 35)).pack()
# label2.pack()

countdown =Label(rightframe, text=f"{examdate().days} days", font=('Rubik', 50)).pack()
# countdown.pack()

weeks = Label(rightframe, text=f"{weeksleft()} weeks left", font=('Rubik', 20)).pack()

cal = Calendar(windowroot, selectmode = 'day', year = todays_date.year, month = todays_date.month, day = todays_date.day, firstweekday = "sunday").pack(pady= 20)

# weeks.pack()

final_label = Label(rightframe, text="Final date:", font=('Rubik', 15))
final_label.pack(side="left")

monthname = datetime.date(year,month,day).strftime("%B")


if day == 1:
    abbr = "st"
elif day == 2:
    abbr = "nd"
elif day == 3:
    abbr = "rd"
else:
    abbr = "th"
# later write a function to convert this to an ordinal number


final_label_date = Label(rightframe, text=f"{day}{abbr} {monthname} {year}", font=('Rubik', 15))
final_label_date.pack(pady=5)


# leftframe = Frame(windowroot).pack()
# note_label = Label(leftframe, text="Pradipta already Read Physics and Chemistry. You are far behind.", font=('Rubik', 15)).pack()
# textbox = tk.Text(windowroot, font=("Comic Sans MS", 30))
# textbox.pack(padx=10, pady=10, expand=False)


# widget = tk.Button(windowroot, text='Mouse Clicks')
# widget.pack()
##### Main Tk loop


# m = Menu(windowroot, tearoff=0)
# m.add_command(label="Close counter")

# def do_popup(event):
#     try:
#         m.tk_popup(event.x_root, event.y_root)
#     finally:
#         m.grab_release()

# windowroot.bind("<Button-3>", do_popup)
# filename = os.getcwd() + "/" +os.path.basename(__file__)





filename = "/home/msm/Desktop/msm-projects/msm-wallpaper-tk-gui/main.py"
def openfile():
    print(filename)
    # os.startfile(filename)
    os.system("code " + filename + "&")
    # ... do other things while notepad is running

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)

my_menu = Menu(windowroot, tearoff=False)
my_menu.add_command(label="Made by MSM")
my_menu.add_command(label="Open Script in VS code", command=openfile)
my_menu.add_separator()

my_menu.add_command(label="Close window", command=windowroot.quit)
windowroot.bind("<Button-3>", my_popup)



# sv_ttk.set_theme("dark")
windowroot.mainloop()


#### MAIN LOOP #####

        