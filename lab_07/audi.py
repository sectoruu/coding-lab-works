import datetime

d = [1, 2, 3]
s = [5, 6, 7, 8]

def daysFromBirthday(d, m, y):
    return (datetime.datetime.now() - datetime.datetime(y, m, d)).days

