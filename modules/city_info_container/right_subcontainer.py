import customtkinter as ctk
from .info_container import info_cont

import os
import json
import datetime

class Right_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master, day_of_week, full_date, current_time):
        ctk.CTkFrame.__init__(
            self,
            master=child_master,
            fg_color = "#91bdc7"
        )
        self.grid(row = 0, column = 2)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.position = ctk.CTkLabel(
            master = self,
            text = day_of_week,
            font = ("Arial", 18, 'bold'),
            text_color = "white"
        )
        self.position.grid(row = 0, column = 0)

        self.position1 = ctk.CTkLabel(
            master = self,
            text = full_date,
            font = ("Arial", 40),
            text_color = "white"
        )
        self.position1.grid(row = 1, column = 0)

        self.position2 = ctk.CTkLabel(
            master = self,
            text = current_time,
            font = ("Arial", 30),
            text_color = "white",
            
        )
        self.position2.grid(row = 2, column = 0)
     


my_path = os.path.abspath(__file__)
my_dir = os.path.dirname(my_path)
my_db = my_dir + "\\..\\..\\data_base.json"

with open(my_db, "r") as file:
    json_dict = json.load(file)
    
    my_city = json_dict[list(json_dict.keys())[0]]
    
    day_of_week = my_city["day_of_week"]
    if day_of_week == 'Monday':
        day_of_week = "Понеділок"
    elif day_of_week == 'Tuesday':
        day_of_week = "Вівторок"
    elif day_of_week == 'Wednesday':
        day_of_week = 'Середа'
    elif day_of_week == 'Thursday':
        day_of_week = 'Четвер'
    elif day_of_week == 'Friday':
        day_of_week = "П'ятниця"
    elif day_of_week == "Saturday":
        day_of_week = 'Субота'
    elif day_of_week == 'Sunday':
        day_of_week = "Неділя"
    
    full_date = my_city["date_data"]
    time = my_city["time_data"]


right_subcont = Right_Subcontainer(info_cont, day_of_week, full_date, time)