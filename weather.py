# class weather with current position and temperature

import requests
import json
import os
import sys


class weather:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.temp = self.get_temp()

    def get_temp(self):
        # get current ip address and location from ipinfo.io
        
        # url for weather api
        # my api key 
        # get api key from text file
        # my_api_key = "01777b97a50888494397ea8201f1a653"
        
        my_api_key = open('api_key.txt', 'r').read()
        url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(self.lat, self.lon, my_api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        temp = data['main']['temp']
        return temp
    def get_temp_celsius(self):
        temp_celsius = self.temp - 273.15
        return temp_celsius
     
# main function to test the program
if __name__ == "__main__":
    # make object with fake coordinates
    my_weather = weather("55.676097", "12.568337")
    #
    print("Temp: " + str(my_weather.temp))
    print("Temp in celsius: " + str(my_weather.get_temp_celsius()))

