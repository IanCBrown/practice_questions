import sys 

def relationships(num_of_characters):
    
    if num_of_characters == 0 or num_of_characters == 1:
        return 0
    elif num_of_characters == 2:
        return 1
    else:
        # power set - 1
        return (2 ** num_of_characters) - num_of_characters - 1
        

def main():
    num_of_characters = int(input())
    print(relationships(num_of_characters))


if __name__ == "__main__":
    main()

