import sys 
# original problem 
# https://open.kattis.com/problems/modulo

def mod_42(num_list):
    mods = set() 
    for int in num_list:
        mods.add(int % 42)
    return len(mods)



def main():
    l = sys.stdin.readlines()
    l = [int(i.strip()) for i in l]
    print(mod_42(l))


if __name__ == "__main__":
    main()