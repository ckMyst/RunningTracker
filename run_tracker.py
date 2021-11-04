'''
Connor Kissack
Running Tracker
'''
import csv
import json
import time
import random
import numpy as np
import requests
import matplotlib
import pandas as pd
import tkinter as tk

matplotlib.use('TkAgg')
from matplotlib import style
import matplotlib.pyplot as plt
from tkinter import messagebox
# ========================
main = tk.Tk()
main.title('Running Tracker')
main.geometry('280x106')


# ========================
# Called when new profile button is clicked, allowing user to input new information about
# weight, goal weight, free time
def infoWin():
    global infoWin, entry_user, entry_pass, entry_maxRun, entry_mileTime
    main.withdraw()
    infoWin = tk.Toplevel(main)
    infoWin.geometry("290x120")

    userNew = tk.Label(infoWin, text='Username:')
    userNew.grid(column=1, row=1)
    passNew = tk.Label(infoWin, text='Password:')
    passNew.grid(column=1, row=2)
    largeRun = tk.Label(infoWin, text='Max Miles:')
    largeRun.grid(column=1, row=3)
    mileTime = tk.Label(infoWin, text='Mile Time: ')
    mileTime.grid(column=1, row=4)
    # TODO: move inputted strings to next row

    entry_user = tk.Entry(infoWin)
    entry_user.grid(column=2, row=1)
    entry_pass = tk.Entry(infoWin, show="•")
    entry_pass.grid(column=2, row=2)

    entry_maxRun = tk.Entry(infoWin)
    entry_maxRun.grid(column=2, row=3)

    entry_mileTime = tk.Entry(infoWin)
    entry_mileTime.grid(column=2, row=4)

    info_submit = tk.Button(infoWin, text='Submit', command=add_profile_info)
    info_submit.grid(column=1, row=5)


# ========================
# Opens window with accessible data of progress, weather, date, routine
def mainWin():
    main.withdraw()
    mainWin = tk.Toplevel(main)
    mainWin.geometry("438x245")
    # Exit (Closes & terminates the running program)
    exit1 = tk.Button(mainWin, text="Exit", borderwidth=0.5, relief="solid", command=exit)
    exit1.grid(column=1, row=1, ipadx=46, ipady=12, padx=10, pady=10, sticky="N")
    # Routine
    routine4 = tk.Button(mainWin, text="Routine", borderwidth=0.5, relief="solid", command=specific_routine)
    routine4.grid(column=1, row=1, ipadx=34, ipady=12, padx=10, pady=10, sticky="S")
    # User Welcome
    welcome5 = tk.Label(mainWin, text=(User1.get() or entry_user.get()), borderwidth=0.5, relief="solid")
    welcome5.grid(column=2, row=1, ipadx=30, ipady=12, padx=10, pady=10, sticky="N")
    # Weather
    weather6 = tk.Button(mainWin, text='Weather', borderwidth=0.5, relief="solid", command=weatherWin)
    weather6.grid(column=2, row=2, ipadx=30, ipady=40, padx=10, pady=10)
    # Date & Time (inclusion of calendar)
    date7 = tk.Button(mainWin, text="Date & Time", borderwidth=0.5, relief="solid", command=calendarWin)
    date7.grid(column=1, row=2, ipady=40, ipadx=20, padx=10)
    # Progress
    progress8 = tk.Button(mainWin, text="Progress", borderwidth=0.5, relief="solid", command=progressWin)
    progress8.grid(column=3, row=1, ipadx=30, ipady=40, padx=10, pady=10)
    # Weight Fluctuation Graph
    graph9 = tk.Button(mainWin, text="Weight Tracker", borderwidth=0.5, relief="solid", command=graphWin)
    graph9.grid(column=3, row=2, ipadx=10, ipady=40, padx=10)


# ========================
# Checks whether the inputted user and pass are correct then calls 'mainWin'
def get_profile_info():
    with open('profile_checker.csv', 'r') as f:
        user_pass_read = csv.reader(f)
        for column in user_pass_read:
            if User1.get() == column[0] and Pass1.get() == column[1]:
                mainWin()


# ========================
# Imports data from new user into profile csv then calls 'mainWin'
def add_profile_info():
    file_name = entry_user.get()
    with open(file_name + '.csv', 'a') as f:
        profile_write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        profile_write.writerow(['Days', 'Weight'])

    with open('profile_checker.csv', 'a') as f:
        write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        write.writerow([entry_user.get(), entry_pass.get(), entry_maxRun.get(), entry_mileTime.get()])
        infoWin.withdraw()
        mainWin()
# ========================


# ========================
# Imports data from progress entry into graph csv
def add_graph_info():
    file_name = User1.get()
    with open(file_name + '.csv', 'a') as f:
        graph_write = csv.writer(f, quoting=csv.QUOTE_NONE)
        graph_write.writerow([progress_ent.get(), current_weight_ent.get()])


# ========================
def add_mile_info():
    file_name = User1.get()
    with open(file_name + '.csv', 'a') as f:
        mile_write = csv.writer(f, quoting=csv.QUOTE_NONE)
        mile_write.writerow([])


# ========================
def time_info():
    time_period.grid(column=1, row=1)
    moment = time.strftime('Today is: %m/%d/%y and the time is: %H:%M:%S')
    time_period.config(text=moment)
    time_period.after(1000, time_info)


# ========================
def routine_info(max_miles, mile_time):
    mile_amount = random.randint(1, max_miles)
    mile_amount_str = str(mile_amount)
    availability = messagebox.askyesno(title='Running Availability', message='Are you able to run today?')
    if availability:
        messagebox.showinfo('information', 'Today you should run: ' + mile_amount_str + ' miles.'
                            + ' Remember, your average mile time is: ' + mile_time)
    else:
        extra_miles = str(mile_amount + 2)
        messagebox.showinfo('information', 'Tomorrow you should run: ' + extra_miles + ' miles.'
                            + ' Remember, your average mile time is: ' + mile_time)


# ========================
def specific_routine():
    user_routine = User1.get() or entry_user.get()

    with open('profile_checker.csv', 'r') as f:
        profile_read = csv.reader(f)
        for row in profile_read:
            if user_routine == row[0]:
                print((row[2]))
                routine_info(int(row[2]), row[3])


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
        # Description indicated by the website about the weather
        weather = ter[0]["description"]
        weatherShown = tk.Label(weatherWin, text='Description: ' + str(weather))
        weatherShown.grid(column=1, row=3, sticky="W")
        temp_f = (round((temperature - 273.15) * 1.8 + 32))
        tempShown = tk.Label(weatherWin, text='Temperature: ' + str(temp_f) + ' ˚F')
        tempShown.grid(column=1, row=2, sticky="W")
        # An array for the rain condition that states if the user 
        rain_cond = np.array(["thunderstorm with light rain", "thunderstorm with rain", "light thunderstorm",
                              "thunderstorm", "heavy thunderstorm", "ragged thunderstorm",
                              "thunderstorm with light drizzle", "thunderstorm with drizzle", "moderate rain",
                              "heavy intensity rain", "very heavy rain", "extreme rain"])
        # Checks whether the weather condition is indicated (as a string) in the "rain_cond" then creates
        # a label which states if the user should run today
        if str(weather) in rain_cond:
            wea_na = tk.Label(weatherWin, text='Currently, it is not ideal for you to run')
            wea_na.grid(column=1, row=5, sticky="NW")
        else:
            wea_a = tk.Label(weatherWin, text='Currently, it is ideal for you to run')
            wea_a.grid(column=1, row=4, sticky="NW")


# ========================
# Primary window: user inputs existing data (reads csv) or creates a profile (writes to csv).
def Profile():
    global Pass1, User1

    User = tk.Label(main, text='Username')
    User.grid(column=1, row=2)
    Pass = tk.Label(main, text='Password')
    Pass.grid(column=1, row=3)
    # Username box: accessor can input username
    User1 = tk.Entry(main)
    User1.grid(column=2, row=2)
    # Password box: accessor can input password
    Pass1 = tk.Entry(main, show="•")
    Pass1.grid(column=2, row=3)
    # Button, once pressed, checks if the info provided in both boxes is correct (within csv).
    # Then, opens the main window if info is valid. If not, won't respond.
    submit_profile = tk.Button(main, text='Submit', command=get_profile_info)
    submit_profile.grid(column=1, row=4, ipadx=13)
    # Allows user to access a new window to input new data then exported to csv 
    new_profile = tk.Button(main, text='New Profile', command=infoWin)
    new_profile.grid(column=1, row=6)


Profile()


# ========================
# Data inputted moved to csv which is accessed by graphical visualizer
# TODO: (2 options): solely export "entry_maxRun" into file_name + '.csv' OR have the "entry box for
# "entry_maxRun" be with the progress window. THIS IS IMPORTANT AS THE ROUTINE WINDOW WILL CALL FROM
# EITHER CSV TO MAKE A RANDOM AMOUNT OF MILES THE USER NEEDS TO RUN FOR THE DAY

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


def graphWin():
    # User's data from 'profile_checker' is exported to the user's specific
    # csv file where the data is then input into a graph
    file_name = User1.get() + '.csv'
    plt.figure('Weight Tracker')
    style.use('grayscale')
    graph_plot = pd.read_csv(file_name)
    day = graph_plot['Days']
    weight = graph_plot['Weight']
    x = list(day)
    y = list(weight)
    plt.plot(x, y)
    plt.title('Weight Per Day')
    plt.xlabel('Days of Progress')
    plt.ylabel('Weight (in lbs)')
    plt.show()


# ========================
# TODO: create real-time calendar
def calendarWin():
    global time_period
    calendarWin = tk.Toplevel(main)
    calendarWin.geometry("280x40")

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
