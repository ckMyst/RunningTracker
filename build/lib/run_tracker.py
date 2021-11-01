'''
Connor Kissack
Running Tracker
'''
import csv
import json
import time
import random
# (Used in messagebox to show random amount of miles the user needs to run on the specific day)
import numpy as np
import requests
import matplotlib
import pandas as pd
import tkinter as tk
matplotlib.use('TkAgg')
from matplotlib import style
import matplotlib.pyplot as plt

# ========================
main = tk.Tk()
main.title('Running Tracker')
main.geometry('280x106')
# ========================
# Called when new profile button is clicked, allowing user to input new information about
# weight, goal weight, free time
def infoWin():
    global entry_weight, entry_goalWeight, entry_time, entry_user, entry_pass, entry_maxRun
    main.withdraw()
    infoWin = tk.Toplevel(main)
    infoWin.geometry("290x170")

    goalWeight = tk.Label(infoWin, text='Goal Weight:')
    goalWeight.grid(column=1, row=1)
    time = tk.Label(infoWin, text='Free time:')
    time.grid(column=1, row=2)
    userNew = tk.Label(infoWin, text='Username:')
    userNew.grid(column=1, row=3)
    passNew = tk.Label(infoWin, text='Password:')
    passNew.grid(column=1, row=4)
    largeRun = tk.Label(infoWin, text='Max Miles:')
    largeRun.grid(column=1, row=5)
    # TODO: move inputted strings to next row
    entry_goalWeight = tk.Entry(infoWin)
    entry_goalWeight.grid(column=2, row=1)

    entry_time = tk.Entry(infoWin)
    entry_time.grid(column=2, row=2)

    entry_user = tk.Entry(infoWin)
    entry_user.grid(column=2, row=3)
    entry_pass = tk.Entry(infoWin, show="•")
    entry_pass.grid(column=2, row=4)

    entry_maxRun = tk.Entry(infoWin)
    entry_maxRun.grid(column=2, row=5)

    info_submit = tk.Button(infoWin, text='Submit', command=add_profile_info)
    info_submit.grid(column=1, row=6)


# ========================
# Opens window with accessible data of progress, weather, date, routine
def mainWin():
    main.withdraw()
    mainWin = tk.Toplevel(main)
    mainWin.geometry("450x300")
    # Exit (Closes & terminates the running program)
    exit1 = tk.Button(mainWin, text="Exit", borderwidth=0.5, relief="solid", command=exit)
    exit1.grid(column=1, row=1, ipadx=10, ipady=10)
    # Routine
    routine4 = tk.Button(mainWin, text="Routine", borderwidth=0.5, relief="solid", command=routineWin)
    routine4.grid(column=1, row=2, pady=50, padx=10, ipadx=10, ipady=10)
    # Weather
    weather5 = tk.Button(mainWin, text='Weather', borderwidth=0.5, relief="solid", command=weatherWin)
    weather5.grid(column=2, row=1, ipadx=10, ipady=10)
    # Date & Time
    date7 = tk.Button(mainWin, text="Date & Time", borderwidth=0.5, relief="solid", command=calendarWin)
    date7.grid(column=2, row=2, pady=30, ipady=10, ipadx=10)
    # Progress
    progress8 = tk.Button(mainWin, text="Progress", borderwidth=0.5, relief="solid", command=progressWin)
    progress8.grid(column=3, row=1, pady=10, ipadx=10, ipady=10)
    # Weight Fluctuation Graph
    graph9 = tk.Button(mainWin, text="Weight Tracker", borderwidth=0.5, relief="solid", command=graphWin)
    graph9.grid(column=3, row=2, pady=20, padx=20, ipadx=10, ipady=10)


# ========================
# Checks whether the inputted user and pass are correct then calls 'mainWin'
def get_profile_info():
    with open('profile_checker.csv', 'r') as f:
        user_pass_read = csv.reader(f)
        for column in user_pass_read:
            if User1.get() == column[2] and Pass1.get() == column[3]:
                mainWin()


# ========================
# Imports data from new user into profile csv then calls 'mainWin'
def add_profile_info():
    with open('profile_checker.csv', 'a') as f:
        write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        wr = write.writerow(
            [entry_goalWeight.get(), entry_time.get(), entry_user.get(),
             entry_pass.get(), entry_maxRun.get()])

        mainWin()
    # TODO: Fix bug that does not delete integers in csv
    file = pd.DataFrame(columns=['Goal Weight', 'Free Time', 'User', 'Password', 'Maximum Miles'])
    file.empty
    new = []

    if wr != file.empty:
        graph = pd.read_csv('profile_checker.csv', sep=",")
        labels = graph.select_dtypes(exclude='string')
        graph.drop(labels, axis=1, inplace=True)
    else:
        with open('profile_checker.csv') as f:
            value_read = csv.reader(f, delimiter=",")
            for row in value_read:
                if row in new and row in value_read:
                    graph = pd.read_csv('graph_data.csv', sep=",")
                    labels = graph.select_dtypes(exclude='string')
                    graph.drop(labels, axis=1, inplace=True)
        # routineWin(wr)

# ========================
# Imports data from progress entry into graph csv
def add_graph_info():
    with open('graph_data.csv', 'a') as f:
        write = csv.writer(f, quoting=csv.QUOTE_NONE)
        write.writerow(
            [progress_ent.get(), current_weight_ent.get()])


# ========================
def time_info():
    time_period.grid(column=1, row=1)
    moment = time.strftime('%m/%d/%y %H:%M:%S')
    time_period.config(text=moment)
    time_period.after(1000, time_info)


# ========================
# Exports real-time data (into string) of weather from 'openweathermap.org'
def weatherWin():
    weatherWin = tk.Toplevel(main)
    weatherWin.geometry("226x96")
    api = "a54836296ddaf31d028e513b43163ebe"
    city_name = tk.Label(weatherWin, text="City: Houston")
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
        weatherShown = tk.Label(weatherWin, text='Description: ' + str(weather))
        weatherShown.grid(column=1, row=3, sticky="W")
        temp_f = (round((temperature - 273.15) * 1.8 + 32))
        tempShown = tk.Label(weatherWin, text='Temperature: ' + str(temp_f) + ' ˚F')
        tempShown.grid(column=1, row=2, sticky="W")
        rain_cond = np.array(["thunderstorm with light rain", "thunderstorm with rain", "light thunderstorm",
                              "thunderstorm", "heavy thunderstorm", "ragged thunderstorm",
                              "thunderstorm with light drizzle", "thunderstorm with drizzle", "moderate rain",
                              "heavy intensity rain", "very heavy rain", "extreme rain"])
        if str(weather) in rain_cond:
            not_free = tk.Label(weatherWin, text='Currently, it is not ideal for you to run')
            not_free.grid(column=1, row=5, sticky="NW")
        else:
            free = tk.Label(weatherWin, text='Currently, it is ideal for you to run')
            free.grid(column=1, row=4, sticky="NW")




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
    Pass1 = tk.Entry(main, show="•")
    Pass1.grid(column=2, row=3)
    # Opens main window if user & pass are correct
    submit_profile = tk.Button(main, text='Submit', command=get_profile_info)
    submit_profile.grid(column=1, row=4, ipadx=13)
    # Allows user to input new data then exported to csv
    new_profile = tk.Button(main, text='New Profile', command=infoWin)
    new_profile.grid(column=1, row=6)


Profile()


# ========================
# Data inputted moved to csv which is accessed by graphical visualizer
def progressWin():
    global progress_ent, current_weight_ent

    progressWin = tk.Toplevel(main)
    progressWin.geometry("310x85")

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
# Data from 'graph_data.csv' is exported to a graph that is updated when new progress is inputted
# TODO: Either reformat the new csv in a way where the specific user has their own days and weight progress
#       or somehow have the submit button in "new profile" create a personalized csv file for them. You could
#       evade the bug entirely by not having anything in 'graph_data.csv' initially and then it tracks it
#       the progress from the beginning. In the CS IA video, start by making a user first and emptying out
#       all the csv files from any information except for the excluding rows
def graphWin():
    plt.figure('Weight Tracker')
    style.use('grayscale')
    graph_plot = pd.read_csv('graph_data.csv')
    day = graph_plot["Days"]
    weight = graph_plot["Weight"]
    x = list(day)
    y = list(weight)
    plt.plot(x, y)
    plt.title('Weight Per Day')
    plt.xlabel('Days of Progress')
    plt.ylabel('Weight (in lbs)')
    plt.show()
# ========================
# TODO: create real-time info for whether the user can run
from tkinter import messagebox

def routineWin():
    #   with open('profile_checker.csv') as f:
    # mile_number = random.randint(1, 10), "Miles to run"
    messagebox.showinfo('information', 'Test')


#         mile_read = csv.DictReader(f)
#         for column in mile_read:
# TODO: Error - either want to pass the entries for goal weight, free time, and max miles from the profile_info function
#       to this function or just use DictReader and pass the specified values for a specific user
#       announcement = column['Goal Weight' 'Free Time' 'Maximum Miles']
# if wr == column[0] and column[1] and column[4]:
#   announcement = entry_goalWeight.get(), entry_time.get(), entry_maxRun.get()
#   messagebox.showinfo('information', announcement)
# make if, elif, else statement for global variables that say whether the weather is optimal
# ========================
# TODO: create real-time calendar
def calendarWin():
    global time_period
    calendarWin = tk.Toplevel(main)
    calendarWin.geometry("400x400")

    cal_title = tk.Label(calendarWin, text="calendar")
    cal_title.grid(column=1, row=1, stick="N")

    time_period = tk.Label(calendarWin)
    time_period.grid(column=1, row=2)

    time_info()
# ========================
# Ends the running program
def exit():
    main.destroy()


# ========================
main.mainloop()
