import datetime

def datum(day, month):
    # manually 
    days = {1 : 31, 
            2 : 28, 
            3 : 31, 
            4 : 30, 
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
            10 : 31,
            11 : 30,
            12 : 31}

    remainders = {
        0 : "Thursday",
        1 : "Friday",
        2 : "Saturday",
        3 : "Sunday",
        4 : "Monday",
        5 : "Tuesday",
        6 : "Wednesday"
    }

    day_count = 0

    day_count += day
    month -= 1
    
    for i in range(month, 0, -1):
        day_count += days[i]

    rem = day_count % 7
    rem -= 1

    return remainders[rem]

def datum_datetime(day, month):
    # using datetime
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date = datetime.date(2009, month, day)
    return days[date.weekday()]


def main():
    i = input().split()
    day = i[0]
    month = i[1]

    print(datum_datetime(int(day), int(month)))


if __name__ == "__main__":
    main()