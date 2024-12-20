import customtkinter as ctk
from .info_container import info_cont
import os
from PIL import Image
import json

class Left_Subcontainer(ctk.CTkFrame):
    def __init__(self, child_master, condition):
        ctk.CTkFrame.__init__(
            self,
            master=child_master,
            fg_color = "#91bdc7"
        )
        self.grid(row = 0, column = 0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        
        self.condition = condition.lower().replace(" ", '')

        self.my_path = os.path.abspath(__file__)
        self.my_dir = os.path.dirname(self.my_path)
        # self.my_icon = self.my_dir + "\\..\\..\\icons\\" + "sunny.png"
        self.my_icon = self.set_condition()
        
        self.image = ctk.CTkImage(
            Image.open(self.my_icon),
            size = (150, 150)
        )

        self.image_text = ctk.CTkLabel(
            master = self,
            text = "",
            font = ("Arial", 15),
            image = self.image
        )        
        self.image_text.grid(row = 1, column = 0)

    def set_condition(self):
        if self.condition == "cloudy":
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "cloudy.png"
        elif self.condition == "rainy":
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "rainy.png"
        elif self.condition == "snowy":
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "snowy.png"
        elif self.condition == "sunny":
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "sunny.png"
        elif self.condition == "partlycloudy":
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "partlycloudy.png"      
        elif self.condition == "mist":
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "mist.png"
        elif self.condition == "overcast":
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "overcast.png"
        else:
            my_icon = self.my_dir + "\\..\\..\\icons\\" + "question.png"
        return my_icon

my_path = os.path.abspath(__file__)
my_dir = os.path.dirname(my_path)
my_db = my_dir + "\\..\\..\\data_base.json"

with open(my_db, "r") as file:
    city_data = json.load(file)
    my_city = city_data[list(city_data.keys())[0]] #достаем нулевой ключ
    my_hour_data = my_city["api_data"]["weather"][0]["hourly"][0]["weatherDesc"][0]['value']
    
    print(my_hour_data)

left_subcont = Left_Subcontainer(info_cont, my_hour_data)