import sys 

def main():
    num_of_contests = int(input()) 

    # dictionary mapping participant name to their preferred language
    # {participant name : programming language}
    participants = {} 
    # lists for each language option 
    python_list = []
    java_list = [] 
    cpp_list = [] 
    ret_list = []

    while num_of_contests > 0:
        line = input().split(",") 
        # print(line)
        # populate dictionary 
        for name in line:
            name = name.split()
            participants[name[0]] = name[1]

        # for each key, value pair in dictionary,  
        # add to the corresponding language list 
        for name, language in participants.items():
            if language == "python":
                python_list.append(name + " " + language)
            elif language == "java":
                java_list.append(name + " " + language)
            elif language == "cpp":
                cpp_list.append(name + " " + language)
        
        # combine list into return list 
        ret_list = python_list + java_list + cpp_list
        # print each item in the return list
        num_of_contests -= 1
        # after each contest, clear the data structures 
        # participants = {}
        # python_list = [] 
        # java_list = [] 
        # cpp_list = [] 
        
        

    for string in ret_list:
        print(string, end=',')

    print()

if __name__ == "__main__": 
    main() 