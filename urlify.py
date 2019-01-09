

def urlify(string_in):
    l = string_in.split(' ')

    for i in range(0, len(l) - 1):
        l[i] = l[i] + "%20"
    return ''.join(l)


def main():
    test_string = "urlify this string"
    print(urlify(test_string))

if __name__ == '__main__':
    main()

    