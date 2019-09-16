

def two_stones(state):
    if state % 2 == 0:
        return "Bob"
    else:
        return "Alice"



def main():
    start_state = int(input())

    print(two_stones(start_state))



if __name__ == "__main__":
    main()