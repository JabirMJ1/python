import datetime

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __add__(self, obj):
        return datetime.timedelta(hours = self.hours, minutes= self.minutes, seconds = self.seconds) + datetime.timedelta(hours = obj.hours, minutes= obj.minutes, seconds = obj.seconds)
        
obj1 = Time(1,3,24)
obj2 = Time(0,2,0)
print(obj1+obj2)
        