class time:
    def __init__(obj,h,m,s):
        obj.hour = h
        obj.minute = m
        obj.second = s
    def show(obj,ruz):
        obj.date = ruz
        return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
    def sanieshomar(obj):
        return obj.minute*60+obj.hour*3600+obj.second

    def sub(obj,newtime):
        obj.hour -= newtime.hour
        obj.minute -= newtime.minute
        obj.second -= newtime.second

    def kam_kardan(obj,hh,mm,ss):
        obj.hour -= hh
        obj.minute -= mm
        obj.second -= ss

    def __add__(obj, obj2):
        obj.hour += obj2.hour
        obj.minute += obj2.minute
        obj.second += obj2.second
        if obj.second>60:
            obj.second=obj.second-60
            obj.minute=obj.minute+1
        if obj.minute>60:
            obj.minute = obj.minute - 60
            obj.hour = obj.hour + 1
    def __ge__(obj, obj2):
        if obj.minute*60+obj.hour*3600+obj.second>=obj2.minute*60+obj2.hour*3600+obj2.second:
            return True
        else:
            return False

    def __gt__(obj, obj2):
        if obj.minute*60+obj.hour*3600+obj.second>obj2.minute*60+obj2.hour*3600+obj2.second:
            return True
        else:
            return False

    def __le__(obj, obj2):
        if obj.minute*60+obj.hour*3600+obj.second<=obj2.minute*60+obj2.hour*3600+obj2.second:
            return True
        else:
            return False

    def __gt__(obj, obj2):
        if obj.minute*60+obj.hour*3600+obj.second<obj2.minute*60+obj2.hour*3600+obj2.second:
            return True
        else:
            return False
    def __sub__(obj, obj2):
        obj.hour -= obj2.hour
        obj.minute -= obj2.minute
        obj.second -= obj2.second
        if obj.second>60:
            obj.second=obj.second-60
            obj.minute=obj.minute+1
        if obj.minute>60:
            obj.minute = obj.minute - 60
            obj.hour = obj.hour + 1


