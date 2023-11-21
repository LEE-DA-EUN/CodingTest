n, k = map(int, input().split())
def factorial(t):
    ans = 1
    for i in range(1, t+1):
        ans = ans * i
    return ans
num = factorial(n) // (factorial(n-k)*factorial(k))
print(num)