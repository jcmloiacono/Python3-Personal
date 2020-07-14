
time = input()
time = time.split()

def am_converter(time):
    time = time[0].split(':')
    if int(time[0]) < 10:
        time = "0" + time[0] + ':' + time[1]
    elif int(time[0]) == 12 :
        time = '00' + ':' + time[1]
    else:
         time = time[0] + ':' + time[1]
    return time
    
def pm_converter(time):
    time = time[0].split(':')
    if time[0] == '12':
        time = time[0] + ':' + time[1]
    else: 
        time_start = (12 + int(time[0]))
        time_end = time[1]
        time = str(time_start) + ":" + time_end
    return time      
      
def military_time(time):
    if time[1] == "PM":
        print(pm_converter(time))
    else:
        print(am_converter(time))

military_time(time)