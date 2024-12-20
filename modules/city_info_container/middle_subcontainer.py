import customtkinter as ctk
from .info_container import info_cont

import os
import json

class Middle_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master, city_name, temp, condition, min_max):
        ctk.CTkFrame.__init__(
            self,
            master=child_master,
            fg_color = "#91bdc7"
        )
        self.grid(row = 0, column = 1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.position = ctk.CTkLabel(
            master = self,
            text = "Поточна позиція",
            font = ("Arial", 35, 'bold'),
            text_color="white"
        )
        self.position.grid(row = 0, column = 0)

        self.position1 = ctk.CTkLabel(
            master = self,
            text = city_name,
            font = ("Arial", 22),
            text_color="white"
        )
        self.position1.grid(row = 1, column = 0)

        self.position2 = ctk.CTkLabel(
            master = self,
            text = temp,
            font = ("Arial", 80),
            text_color="white"
        )
        self.position2.grid(row = 2, column = 0)

        self.position3 = ctk.CTkLabel(
            master = self,
            text = condition,
            font = ("Arial", 30),
            text_color="white"
        )
        self.position3.grid(row = 3, column = 0)

        self.position4 = ctk.CTkLabel(
            master = self,
            text = min_max,
            font = ("Arial", 30),
            text_color="white"
        )
        self.position4.grid(row = 4, column = 0)
    

my_path = os.path.abspath(__file__)
my_dir = os.path.dirname(my_path)
my_db = my_dir + "\\..\\..\\data_base.json"

with open(my_db, "r") as file:
    json_dict = json.load(file)
    my_city = list(json_dict.keys())[0]
    my_temp = json_dict[my_city]["api_data"]["current_condition"][0]["temp_C"] + "°"
    my_condition = json_dict[my_city]["api_data"]["current_condition"][0]["weatherDesc"][0]["value"]
    my_min = json_dict[my_city]["api_data"]["weather"][0]["mintempC"]
    my_max = json_dict[my_city]["api_data"]["weather"][0]["maxtempC"]
    
    my_min_max = f"↓ {my_min}° ↑ {my_max}°"
    # print(json_dict)

middle_subcont = Middle_Subcontainer(info_cont, my_city, my_temp, my_condition, my_min_max)
