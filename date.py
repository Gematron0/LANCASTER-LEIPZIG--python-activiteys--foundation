from datetime import date, time

### python date class ###
my_date = date(2025,4,28)
print(f"date is: {my_date}")
# value error if the number of the year, month, day is to high or to low of a numbter
# type error if you enter a string, or anything that is not conciderd an int

today = date.today()
print(f"todays date: {today}")
# inbuild function to git todays date

print(f"{today.year}: {today.month}: {today.day}")

# converting a date into a string for easeyer menipulation using isoformat()
Str = date.isoformat(today)
print(Str)
print(type(Str))

### python time class ###
# this class allows you to input all data inside of the time class which would store and do all the data
# by defalt all of the time is set to 0

my_time = time(13,24,56)
print(f"my time: {my_time}")
my_time = time(minute=12)
print(f"my modified time with only miniuts: {my_time}")
# the same error messeges would apply hear as above

# printing the time currently
Time = time(13,24,56)
print(f"{Time.hour}: {Time.minute}: {Time.second}")

# converting time into string object
Time = time(12,24,36,1212)
Time_str = time.isoformat(Time)
print(Time_str)
print(type(Time_str))