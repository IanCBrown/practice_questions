
def meow_factor(n):

    div_result = 0
    div_counter = 0
    max = 0
    for i in range (2, n):
        if n % i == 0:
            div_result = n / i
            div_counter += 1
            if div_result % i == 0:
                div_result = div_result / i
                div_counter += 1 
                if div_result % i == 0:
                    div_result = div_result / i
                    div_counter += 1 
                    if div_result % i == 0:
                        div_result = div_result / i
                        div_counter += 1 
                        if div_result % i == 0:
                            div_result = div_result / i
                            div_counter += 1 
                            if div_result % i == 0:
                                div_result = div_result / i
                                div_counter += 1 
                                if div_result % i == 0:
                                    div_result = div_result / i
                                    div_counter += 1 
                                    if div_result % i == 0:
                                        div_result = div_result / i
                                        div_counter += 1 
                                        if div_result % i == 0:
                                            div_result = div_result / i
                                            div_counter += 1 
                                            if i > max:
                                                max = i
        else:
            return i - 1
    return max


def main():
    m = int(input())
    print(meow_factor(m))


if __name__ == "__main__": 
    main()