# original problem 
# https://open.kattis.com/problems/aaah

def go_or_no_go(max_capable, doctors_req): 
    if len(max_capable) >= len(doctors_req):
        return "go"
    else:
        return "no"


def main():
    jons_max = input()
    doctors_req = input()
    print(go_or_no_go(jons_max, doctors_req))


if __name__ == "__main__":
    main()




