def fun():
    arr = []
    for x in range(0, 5):
        arr.append([])
        for y in range(0, 5):
            arr[x].append(y)
    print(arr)





def main(args=None):
    var = 10/0
    return 0

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)

