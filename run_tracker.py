'''
Connor Kissack
Running Tracker
'''
from matplotlib import pyplot as pl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import exp
import tkinter as tk
import tkinter.font as ft
import csv
# ============================
main = tk.Tk()
main.title('Running Tracker')
main.geometry('280x106')
# ============================
def infoWin():
    global entry_bmi, entry_goalBmi, entry_time, entry_user, entry_pass
    main.withdraw()
    infoWin = tk.Toplevel(main)
    infoWin.geometry("280x170")

    bmi = tk.Label(infoWin, text='BMI:')
    bmi.grid(column=1, row=1)
    goalBmi = tk.Label(infoWin, text='Goal BMI:')
    goalBmi.grid(column=1, row=2)
    time = tk.Label(infoWin, text='Free time:')
    time.grid(column=1, row=3)
    userNew = tk.Label(infoWin, text='Username:')
    userNew.grid(column=1, row=4)
    passNew = tk.Label(infoWin, text='Password:')
    passNew.grid(column=1, row=5)

    entry_bmi = tk.Entry(infoWin)
    entry_bmi.grid(column=2, row=1)
    entry_goalBmi = tk.Entry(infoWin)
    entry_goalBmi.grid(column=2, row=2)

    entry_time = tk.Entry(infoWin)
    entry_time.grid(column=2, row=3)

    entry_user = tk.Entry(infoWin)
    entry_user.grid(column=2, row=4)
    entry_pass = tk.Entry(infoWin)
    entry_pass.grid(column=2, row=5)

    info_submit = tk.Button(infoWin, text='Submit', command=addinfo)
    info_submit.grid(column=1, row=6)
# ============================
def mainWin():
    main.withdraw()
    mainWin = tk.Toplevel(main)
    mainWin.geometry("200x120")
    # Exit
    Font = ft.Font(family="Calibre", size=12)
    Exit1 = tk.Button(mainWin, text="Exit", borderwidth=0.5, relief="solid", font=Font, command=exit)
    Font.configure(size="14")
    Exit1.grid(column=0, row=0, ipadx=16, ipady=12, sticky="NE")
    # Routine
    Routine4 = tk.Button(mainWin, text="Routine", borderwidth=0.5, relief="solid", font=Font)
    Routine4.grid(column=1, row=0, pady=60, ipadx=16, ipady=12)
    # Weather
    Weather5 = tk.Button(mainWin, text='Weather', borderwidth=0.5, relief="solid", font=Font)
    Weather5.grid(column=0, row=1, ipadx=47, ipady=12, sticky="NW")
    # Date & Time
    Date7 = tk.Button(mainWin, text="Date & Time", borderwidth=0.5, relief="solid", font=Font)
    Date7.grid(column=1, row=1, pady=30, ipady=66, ipadx=12)
# ============================
def getinfo():
    with open('profile_checker.csv', 'r') as f:
        user_pass_read = csv.reader(f)
        for row in user_pass_read:
            if User1.get() == row[0] and Pass1.get() == row[1]:
                mainWin()
            elif User1.get() == row[3] and Pass1.get() == row[4]:
                mainWin()
            else:
                print("User and Pass Not Found")
# ============================
def addinfo():
    with open('profile_checker.csv', 'a') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        write.writerow(
            [entry_bmi.get(), entry_goalBmi.get(), entry_time.get(), entry_user.get(), entry_pass.get()])
        mainWin()
# ============================
def weatherWin():
    weatherWin = tk.Toplevel(main)
    weatherWin.geometry("300x450")
    api = "a54836296ddaf31d028e513b43163ebe"
    city_name = tk.Label(weatherWin, text="Houston")

# ============================
def Profile():
    global Pass1, User1
    # ============================
    User = tk.Label(main, text='Username')
    User.grid(column=1, row=2)
    Pass = tk.Label(main, text='Password')
    Pass.grid(column=1, row=3)
    # Username
    User1 = tk.Entry(main)
    User1.grid(column=2, row=2)
    # Password
    Pass1 = tk.Entry(main, show="*")
    Pass1.grid(column=2, row=3)
    # ============================
    submit_profile = tk.Button(main, text='Submit', command=getinfo)
    submit_profile.grid(column=1, row=4, ipadx=13)

    new_profile = tk.Button(main, text='New Profile', command=infoWin)
    new_profile.grid(column=1, row=6)
Profile()
# ============================
def graph_layout():
    print("Hello World Pt1")
graph_layout()
# ============================
def free_time_checker():
    print("Hello World Pt2")
free_time_checker()
# ============================
def exit():
    main.destroy()


# ============================
main.mainloop()