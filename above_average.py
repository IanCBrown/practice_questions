import sys

# original problem 
# https://open.kattis.com/problems/aboveaverage



def percent_above_average(_class):
    # remove the first element
    _class.pop(0)
    class_mean = float(sum(_class) / len(_class))
    num_above_average = 0
    percentage = 0

    # for each student in the class that is above average, increment counter
    for student_score in _class:
        if student_score > class_mean:
            num_above_average += 1
    
    percentage = float(num_above_average / len(_class)) * 100
    return "{0:.3f}".format(percentage) + "%\n"
    

def main():
    ret_string = ""
    num_of_cases = int(input())
    list_of_classes = []
    while num_of_cases > 0:
        list_of_classes.append(sys.stdin.readline().split())
        num_of_cases -= 1
    # nested list comprehension to convert each element to an int 
    list_of_classes = [[int(i) for i in grade] for grade in list_of_classes]

    for _class in list_of_classes:
        ret_string += percent_above_average(_class)
    
    print(ret_string)


if __name__ == "__main__":
    main()