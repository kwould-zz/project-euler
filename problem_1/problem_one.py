



def main():
    res = 0
    for val in range(1000):
        if val % 3 == 0 or val % 5 == 0:
            res+=val
    print(res)
main()