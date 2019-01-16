
def running_sum(l):
    """ Calculate running sum of list l"""
    ret_list = [] 
    ret_list = [sum(l[:i + 1]) for i in range(len(l))] 
    return ret_list

def main():
    test = [10, 20, 30, 40, 50]
    print(running_sum(test))




if __name__ == '__main__':
    main()