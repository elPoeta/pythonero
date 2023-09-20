import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    pattern = f"^{regex} to {regex}$"
    match = re.search(pattern, s)
    if match:
        from_time_m = sanitize_group(match.group(2),"00")
        from_time_format = sanitize_group(match.group(3),"")
        from_time = sanitize_time(f"{match.group(1)}:{from_time_m} {from_time_format}")
        
        to_time_m = sanitize_group(match.group(5),"00")
        to_time_format = sanitize_group(match.group(6),"")
        to_time = sanitize_time(f"{match.group(4)}:{to_time_m} {to_time_format}")
        
        return f"{from_time} to {to_time}"
    else:
        raise ValueError
    
    
def sanitize_group(group, default):
    return group if group is not None else default


def sanitize_time(time):
    splitedTime = time.split(' ')
    hour, minutes = splitedTime[0].split(':')
    hour = int(hour)
    minutes = int(minutes)

    if (len(splitedTime) == 2):
        formatTime = splitedTime[-1]
        if formatTime == 'AM':
            if hour == 12:
              hour = 0
            elif hour == 24:
               hour = 12        
        elif formatTime == 'PM':
            if hour < 12:
                hour += 12   
                   
    return f"{hour:02}:{minutes:02}"

if __name__ == "__main__":
    main()