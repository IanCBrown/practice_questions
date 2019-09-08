def centuryFromYear(year):
    # not optimal. 
    year_str = str(year)
    if year_str == "":
        return 1
    cen_range = 0
    if len(year_str) == 3:
        cen = int(year_str[0])
        cen_range = int(year_str[1:])
    elif len(year_str) <= 2:
        return 1
    else:
        cen = int(year_str[:2])
        cen_range = int(year_str[2:])
    if cen_range != 0:
        cen += 1
    return cen


def main():
    inn = input()
    print(centuryFromYear(inn))

if __name__ == "__main__":
    main()
