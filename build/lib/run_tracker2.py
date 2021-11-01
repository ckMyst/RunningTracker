'''
Ok I need to finish the announcement function which
indicates what amount of miles i need to run
(which will pick a random number of miles from 1 to
the highest amount issued by the user in the beginning).

Also, it needs to say whether the user can run depending
on the temperature and weather (if temperature is less than
or equal to 32 F then it will say to not run and stay indoors.
And it will say the same thing when it is raining).

Lastly, I just need to make a calendar the popups from the
button that has a real time counter as well

For bugs: I need to fix the graph and convert strings imported by the "process"
function into float integers or integers or it will not allow
the graph to work.

Withdraw windows!!!
'''
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import random
import csv

class Routine:
    def __init__(self, file1, file2, announcement, temperature, weather, miles):
        # Possibly use functions weatherShown and tempShown to allow arguments to be passed through GUI
        self.file1 = file1
        self.file2 = file2
        self.announcement = announcement
        self.temperature = temperature
        self.weather = weather
        self.miles = miles

    def user_routine(self):
        pd.read_csv(self.file1)
        messagebox.showinfo("information", self.announcement + self.temperature + self.weather)

        with open(self.file2) as f:
            miles = csv.reader(f, delimitir=",")
            for column in self.file2:
                random.randint(1, self.miles)








