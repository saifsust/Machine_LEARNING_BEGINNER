# string reverse
def reverse(str):
    temp = ''
    for x in range(len(str)):
        temp += str[-x - 1]
    return temp


def reverse(s):
    return s[::-1]


# main function
def main():
    while True:
        str = input('enter string : ')
        print(reverse(str))
    return 0


if __name__ == '__main__':
    main()
