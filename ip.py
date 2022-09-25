# import json, requests and sys
import json
import requests



# class to get ip address
class ip:
    def __init__(self):
        self.ip = self.get_ip()

    def get_ip(self):
        # get current ip address and location from ipinfo.io
        url = "https://ipinfo.io/json"
        response = requests.get(url)
        data = json.loads(response.text)
        ip = data['ip']
        return ip
    
# main function to test the program
if __name__ == "__main__":
    # make object from ip class
    my_ip = ip()
    print("IP: " + my_ip.ip)
