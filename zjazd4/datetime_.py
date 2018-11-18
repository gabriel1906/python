import datetime

now = datetime.datetime.today()
print(now.day)
print(now.weekday())


my_birthady = datetime.datetime(1974, 6, 19)
print(my_birthady.weekday())

print(datetime.datetime.today() - my_birthady)
