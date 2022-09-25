
# import tkinter and tkinter.ttk
from tkinter import *
from tkinter.ttk import *
from unicodedata import name

from weather import weather
from ip import ip
from location import ip2coordinates
from tid import tid

# class called GUI with one button update and print the weather, time and location in the GUI
class GUI:
    def __init__(self, name):
        self.root = Tk()
        self.name = name
        self.root.title(name)
        self.root.geometry("600x400")
        self.root.resizable(width=False, height=False)
        self.root.configure(background="white")

        self.start()

        self.root.mainloop()

    def start(self):
        self.my_ip = ip()
        self.my_coordinates = ip2coordinates(self.my_ip.ip)
        self.my_weather = weather(self.my_coordinates.lat, self.my_coordinates.lon)

        self.setup_gui(self.name)

    def update(self):
        self.my_ip = ip()
        self.my_coordinates = ip2coordinates(self.my_ip.ip)
        self.my_weather = weather(self.my_coordinates.lat, self.my_coordinates.lon)

        self.setup_gui(self.name)

    def setup_gui(self, name):
        self.root.update()

        self.root.title(name)

        self.root.geometry("600x400")
        self.root.resizable(width=False, height=False)

        self.root.configure(background="white")

        self.root.update

        self.label = Label(self.root, text="Weather", font=("Arial", 30))
        self.label.place(x=250, y=10)

        self.label = Label(self.root, text="City: " + self.my_coordinates.city, font=("Arial", 20))
        self.label.place(x=10, y=70)
                
        self.label = Label(self.root, text="Temperature: " + str(round(self.my_weather.get_temp_celsius(), 2)) + "°C", font=("Arial", 20))
        self.label.place(x=10, y=120)

        self.label = Label(self.root, text="Time: " + tid().time , font=("Arial", 20))
        self.label.place(x=10, y=190)

        self.label = Label(self.root, text="IP: " + self.my_ip.ip, font=("Arial", 20))
        self.label.place(x=10, y=230)

        self.button = Button(self.root, text="Update", command=self.update)
        self.button.place(x=10, y=10)
        
        # loop to update the GUI
        self.root.update()
        

        

# main function to test the program
if __name__ == "__main__":
    GUI("Weather")