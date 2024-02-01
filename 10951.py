while True:
    try:
        map(int,input().split())
        print(sum(map(int,input().split())))
    except:
        break