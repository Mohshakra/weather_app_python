# class ip2coordinates - get coordinates from ip address and city name
# 
import requests
import json
import ip as ip


# ip2coordinates class with ip as argument to get coordinates
class ip2coordinates:
    def __init__(self, ip):
        self.ip = ip
        self.lat = self.get_lat()
        self.lon = self.get_lon()
        self.city = self.get_city()

    def get_lat(self):
        # get current ip address and location from ipinfo.io
        url = "https://ipinfo.io/" + self.ip + "/json"
        response = requests.get(url)
        data = json.loads(response.text)
        lat = data['loc'].split(",")[0]
        return lat

    def get_lon(self):
        # get current ip address and location from ipinfo.io
        url = "https://ipinfo.io/" + self.ip + "/json"
        response = requests.get(url)
        data = json.loads(response.text)
        lon = data['loc'].split(",")[1]
        return lon

    def get_city(self):
        # get current ip address and location from ipinfo.io
        url = "https://ipinfo.io/" + self.ip + "/json"
        response = requests.get(url)
        data = json.loads(response.text)
        city = data['city']
        return city
    
    

    
    
# call main function to start the program
if __name__ == "__main__":
    # make object from ip class and ip2coordinates class
    my_ip = ip.ip()
    my_coordinates = ip2coordinates(my_ip.ip)
    print("IP: " + my_ip.ip)
    print("Lat: " + my_coordinates.lat)
    print("Lon: " + my_coordinates.lon)
    print("City: " + my_coordinates.city)
    
    
# end of program
