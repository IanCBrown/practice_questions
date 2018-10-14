import sys

# original problem 
# https://open.kattis.com/problems/akcija
def minimal_price(price_list):
    price_list.sort(reverse=True)
    # split list in to chunks of size 3
    price_list = chunks(price_list, 3)
    total = 0 
    for group in price_list:
        if len(group) == 3:
            total += group[0] + group[1]
        else:
            total += sum(group)
    return total


# helper function to split price list into evenly sized chunks of size N
# inspired by:
# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(arr, n):
    ret_list = []
    for i in range(0, len(arr), n):
        ret_list.append(arr[i:i + n])
    return ret_list


def main():
    # gathering input 
    num_of_books = int(input())
    prices = []
    while num_of_books > 0:
        prices.append(int(sys.stdin.readline().strip()))
        num_of_books -= 1
    
    print(minimal_price(prices))

if __name__ == "__main__":
    main()