# class called time and a variable called time in format hh:mm:ss
import tid
import datetime

# class time and function called now ti get the current time in format hh:mm:ss and saved it in variable called time
class tid:
    # init function with self
    def __init__(self):
        self.time = self.now()
    
    def now(self):
        # variable called time in format hh:mm:ss
        self.time = datetime.datetime.now().strftime("%H:%M:%S")
        return self.time

# main function
if __name__ == "__main__":
    print(tid().time)
    
    