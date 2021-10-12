'''
Connor Kissack
Running Tracker
'''
import csv
import json
# import random (Used in messagebox to show random amount of miles the user needs to run on the specific day)
import requests
import numpy as np
import tkinter as tk
import tkinter.font as ft
from matplotlib import style
from tkinter import messagebox
from matplotlib import pyplot as plt
# ========================
main = tk.Tk()
main.title('Running Tracker')
main.geometry('280x106')
# ========================
# Called when new profile button is clicked, allowing user to input new information about
# weight, goal weight, free time
def infoWin():
    global entry_weight, entry_goalWeight, entry_time, entry_user, entry_pass
    main.withdraw()
    infoWin = tk.Toplevel(main)
    infoWin.geometry("280x210")

    Weight = tk.Label(infoWin, text='Weight:')
    Weight.grid(column=1, row=1)
    goalWeight = tk.Label(infoWin, text='Goal Weight:')
    goalWeight.grid(column=1, row=2)
    time = tk.Label(infoWin, text='Free time:')
    time.grid(column=1, row=3)
    userNew = tk.Label(infoWin, text='Username:')
    userNew.grid(column=1, row=4)
    passNew = tk.Label(infoWin, text='Password:')
    passNew.grid(column=1, row=5)
    smallRun = tk.Label(infoWin, text='Smallest Mile:')
    smallRun.grid(column=1, row=6)
    largeRun = tk.Label(infoWin, text='Largest Mile:')
    largeRun.grid(column=1, row=7)
    # TODO: move inputted strings to next row
    entry_weight = tk.Entry(infoWin)
    entry_weight.grid(column=2, row=1)
    entry_goalWeight = tk.Entry(infoWin)
    entry_goalWeight.grid(column=2, row=2)

    entry_time = tk.Entry(infoWin)
    entry_time.grid(column=2, row=3)

    entry_user = tk.Entry(infoWin)
    entry_user.grid(column=2, row=4)
    entry_pass = tk.Entry(infoWin)
    entry_pass.grid(column=2, row=5)

    entry_smallRun = tk.Entry(infoWin)
    entry_smallRun.grid(column=2, row=6)
    entry_largeRun = tk.Entry(infoWin)
    entry_largeRun.grid(column=2, row=7)

    info_submit = tk.Button(infoWin, text='Submit', command=add_profile_info)
    info_submit.grid(column=1, row=8)
# ========================
# Opens window with accessible data of progress, weather, date, routine
def mainWin():
    main.withdraw()
    mainWin = tk.Toplevel(main)
    mainWin.geometry("450x300")
    # Exit
    Font = ft.Font(family="Calibre", size=12)
    Exit1 = tk.Button(mainWin, text="Exit", borderwidth=0.5, relief="solid", font=Font, command=exit)
    Font.configure(size="14")
    Exit1.grid(column=1, row=1, ipadx=10, ipady=10)
    # Routine
    Routine4 = tk.Button(mainWin, text="Routine", borderwidth=0.5, relief="solid", font=Font)
    Routine4.grid(column=1, row=2, pady=50, padx=10, ipadx=10, ipady=10)
    # Weather
    Weather5 = tk.Button(mainWin, text='Weather', borderwidth=0.5, relief="solid", font=Font, command=weatherWin)
    Weather5.grid(column=2, row=1, ipadx=10, ipady=10)
    # Date & Time
    Date7 = tk.Button(mainWin, text="Date & Time", borderwidth=0.5, relief="solid", font=Font)
    Date7.grid(column=2, row=2, pady=30, ipady=10, ipadx=10)

    Progress8 = tk.Button(mainWin, text="Progress", borderwidth=0.5, relief="solid", font=Font, command=progressWin)
    Progress8.grid(column=3, row=1, pady=10, ipadx=10, ipady=10)

    Graph9 = tk.Button(mainWin, text="Weight Tracker", borderwidth=0.5, relief="solid", font=Font, command=graphWin)
    Graph9.grid(column=3, row=2, pady=20, padx=20, ipadx=10, ipady=10)
# ========================
# Checks whether the inputted user and pass are correct then calls 'mainWin'
def get_profile_info():
    with open('profile_checker.csv', 'r') as f:
        user_pass_read = csv.reader(f)
        for row in user_pass_read:
            if User1.get() == row[3] and Pass1.get() == row[4]:
                mainWin()
            else:
                print("Unauthorized")
# ========================
# Imports data from new user into profile csv then calls 'mainWin'
def add_profile_info():
    with open('profile_checker.csv', 'a') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        write.writerow(
            [entry_weight.get(), entry_goalWeight.get(), entry_time.get(), entry_user.get(), entry_pass.get()])

        mainWin()
# ========================
# Exports data from graph csv to plot


# ========================
# Imports data from progress entry into graph csv
def add_graph_info():
    print("Hello World")
    with open('graph_data.csv', 'a') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        write.writerow(
        [progress_ent.get(), current_weight_ent.get()])

# ========================
# Exports real-time data (into string) of weather from 'openweathermap.org'
def weatherWin():
    weatherWin = tk.Toplevel(main)
    weatherWin.geometry("180x80")
    Font = ft.Font(family="Calibre", size=12)
    api = "a54836296ddaf31d028e513b43163ebe"
    city_name = tk.Label(weatherWin, text="Houston", font=Font)
    city_name.grid(column=1, row=1, sticky="W")
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Houston"
    weather_full = weather_url + "appid=" + api + "&q=" + city
    rsp = requests.get(weather_full)
    pro = rsp.json()
    if pro["cod"] != "404":
        sec = pro['main']
        temperature = sec['temp']
        ter = pro['weather']
        weather = ter[0]["description"]
        weatherShown = tk.Label(weatherWin, text='Description: ' + str(weather), font=Font)
        weatherShown.grid(column=1, row=3, sticky="W")
        tempShown = tk.Label(weatherWin, text='Temperature: ' + str(round(temperature - 273.15)) + ' ˚C', font=Font)
        tempShown.grid(column=1, row=2, sticky="W")
# ========================
# Primary window: user inputs existing data (reads csv) or creates a profile (writes to csv).
def Profile():
    global Pass1, User1

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

    submit_profile = tk.Button(main, text='Submit', command=get_profile_info)
    submit_profile.grid(column=1, row=4, ipadx=13)
    new_profile = tk.Button(main, text='New Profile', command=infoWin)
    new_profile.grid(column=1, row=6)
Profile()
# ========================
# Data inputted moved to csv which is accessed by graphical visualizer
# TODO: change string in csv to integer
def progressWin():
    global progress_ent, current_weight_ent

    progressWin = tk.Toplevel(main)
    progressWin.geometry("310x120")

    progress = tk.Label(progressWin, text="Day in Progress: ")
    progress.grid(column=1, row=1)
    current_weight = tk.Label(progressWin, text="Current Weight: ")
    current_weight.grid(column=1, row=2)

    progress_ent = tk.Entry(progressWin)
    progress_ent.grid(column=2, row=1)
    current_weight_ent = tk.Entry(progressWin)
    current_weight_ent.grid(column=2, row=2)

    graph_data_submit = tk.Button(progressWin, text='Submit', command=add_graph_info)
    graph_data_submit.grid(column=1, row=3, ipadx=28)
# ========================
# Graphical visualizer of weight loss per day (data from 'graph_data.csv')
# TODO: fix major error due to plt.show causing profile window to pop up once more
def graphWin():
    graphWin = tk.Toplevel(main)
    graphWin.geometry("800x800")
    style.use('grayscale')
    x, y = np.loadtxt('graph_data.csv', unpack=True, delimiter=",")
    plt.plot(x, y)
    plt.title('Weight Tracker')
    plt.xlabel('Days')
    plt.ylabel('Weight')

    plt.show(graphWin)
# ========================
# TODO: create real-time info for whether the user can run
def routineWin():
    # make if, elif, else statement for global variables that say whether the weather is optimal
    print("Hello World")
routineWin()
# ========================
# TODO: create real-time calendar
def calendarWin():
    print("Hello World")
calendarWin()
# ========================
# Ends the running program
def exit():
    main.destroy()
# ========================

main.mainloop()