second = float(input("Enter a number of seconds: "))

if second < 0:
    print("Error. Enter a number above 0")
else:
    if second >= 0 and second < 60:
        seconds = second % 6
        print("Seconds = ",seconds)
    elif second >= 60 and second < 3600:
        minutes = second // 60
        seconds = second % 60
        print(second," seconds is",minutes,"minute(s) and ",seconds,"second(s)")
    elif second >=3600 and second < 86400:
        hours = second // 3600
        minutes = (second % 3600) // 60
        seconds = (second % 3600) % 60
        print(second,"seconds is", hours, "hour(s)",minutes,"minute(s) and ",seconds,"second(s)")
    elif second >= 86400:
        days = second // 86400
        hours = (second % 86400) // 3600
        minutes = (((second % 86400) % 3600) // 60)
        seconds = (((second % 86400) % 3600) % 60)
        print(second,"seconds is",days,'day(s)', hours, "hour(s)",minutes,"minute(s) and ",seconds,"second(s)")