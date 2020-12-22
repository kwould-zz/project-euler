memo = {0: 0, 1:1}

def fib(val, memo):
    if val not in memo:
       memo[val] = fib(val-1, memo) + fib(val-2, memo)
       return memo[val]
    else:
        return memo[val]

def main():
    sum_ans = 0
    num = 0
    res = fib(0, memo)
    while res <= 4000000:
        if res % 2 == 0:
           sum_ans += res 
        num += 1 
        res = fib(num, memo)
    print(sum_ans)

main()