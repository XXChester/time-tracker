from datetime import datetime
"""
Feed the program date ranges like 9:30am-12:00pm	6:25pm-7:15pm	10:14am-10:54am and it will calculate the hours. Used for tracking my game dev projects
"""
def get_time(input):
    if ":" in input:
        return datetime.strptime(input, "%I:%M%p")
    else:
        return datetime.strptime(input, "%I%p")

def get_duration(range):
    sections = range.split("-")
    print(sections)
    start = get_time(sections[0])
    end = get_time(sections[1])
    print(end - start)
    duration = end - start
    return duration.seconds/60


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    times = input("Enter list of times")
    ranges = times.split()
    print (ranges)
    duration = [len(ranges)]
    for i in range(len(ranges)):
        duration.append(get_duration(ranges[i]))
#     duration array is in minutes
    total = sum(duration)
    print("minutes: " + str(total))
    print("hours: " + str(total / 60))
