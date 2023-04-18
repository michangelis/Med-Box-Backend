from datetime import datetime
from playsound import playsound
def alarm():
    #alarmHour = int(input("Enter hour: "))
    #alarmMin = int(input("Enter minute: "))
    #alarmAm = input("am/pm")
    #if alarmAm == "pm":
    #    alarmHour += 12
    now = datetime.now()
    current_day = now.strftime('%A')
    current_time = now.time()
    minute = current_time.minute

    print(current_day)
    print(current_time)# Output: Tuesday
    print(minute)

    playsound('/Users/michael/Desktop/alarm.wav')