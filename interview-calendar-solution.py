## Google Coding Interview: Create an algorithm that takes two people's calendars and returns free slots of time to schedule a meeting.
## Assume time is represented in military time separated by a colon, where possible times are in between 0:00 and 23:59.
## The first line of input contains three integers M, A, and B that denote the meeting duration in minutes and the number of time slots in the two people's calendars.
## The following 2A lines contain sorted strings representing the start time and end time for each time slot in the first person's calendar.
## The following two lines then contain strings representing the daily bounds of when the first person can have the meeting.
## The following 2B lines contain sorted strings representing the start time and end time for each time slot in the second person's calendar.
## The following two lines then contain strings representing the daily bounds of when the second person can have the meeting.
## Output a list containing lists with length two that display the start time and end time of available slots when a meeting can be scheduled.
## Sample input:
## 30
## 3
## 4
## 9:00
## 10:30
## 12:00
## 13:00
## 16:00
## 18:00
## 9:00
## 20:00
## 9:00
## 11:30
## 12:30
## 14:30
## 14:30
## 15:00
## 16:00
## 17:00
## 10:00
## 18:30
## Sample output:
## [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

def military_time_to_minutes(time):
    time = time.split(":")
    minutes = int(time[0]) * 60 + int(time[1])
    return minutes

def minutes_to_military_time(minutes):
    hours = minutes // 60
    if minutes - hours * 60 < 10:
        minutes = "0" + str(minutes - hours * 60)
    else:
        minutes = str(minutes - hours * 60)
    time = str(hours) + ":" + minutes
    return time

def create_timeslot(time1, time2):
    start = military_time_to_minutes(time1)
    end = military_time_to_minutes(time2)
    return [start, end]

#input number of timeslots and meeting duration
meeting_duration = int(input())
timeslots_count1 = int(input())
timeslots_count2 = int(input())

#create list of unavailable times
unavailable_times = []

#add timeslots of first person to unavailable times
for i in range(timeslots_count1):
    start = input()
    end = input()
    slot = create_timeslot(start, end)
    unavailable_times.append(slot)

#add bounds of first person to unavailable times
bounds1_start = input()
bounds1_end = input()
bounds1_start_adjusted = create_timeslot("0:00", bounds1_start)
bounds1_end_adjusted = create_timeslot(bounds1_end, "23:59")
unavailable_times.append(bounds1_start_adjusted)
unavailable_times.append(bounds1_end_adjusted)

#add timeslots of second person to unavailable times
for i in range(timeslots_count2):
    start = input()
    end = input()
    slot = create_timeslot(start, end)
    unavailable_times.append(slot)

#add bounds of second person to unavailable times
bounds2_start = input()
bounds2_end = input()
bounds2_start_adjusted = create_timeslot("0:00", bounds2_start)
bounds2_end_adjusted = create_timeslot(bounds2_end, "23:59")
unavailable_times.append(bounds2_start_adjusted)
unavailable_times.append(bounds2_end_adjusted)

#optimize unavailable times
unavailable_times.sort()
i = 0
while i < len(unavailable_times) - 1:
    if unavailable_times[i][1] >= unavailable_times[i + 1][0]:
        if unavailable_times[i][1] < unavailable_times[i + 1][1]:
            unavailable_times[i][1] = unavailable_times[i + 1][1]
        unavailable_times.pop(i + 1)
    else:
        i += 1

#find available times and convert back to military time
available_times = []
for i in range(len(unavailable_times) - 1):
    if(unavailable_times[i + 1][0] - unavailable_times[i][1] >= meeting_duration):
        slot = [minutes_to_military_time(unavailable_times[i][1]), minutes_to_military_time(unavailable_times[i + 1][0])]
        available_times.append(slot)

#print available times in a list
print(available_times)
