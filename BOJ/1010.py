import sys
input = sys.stdin.readline
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans

for i in range(int(input())):
    n, m = map(int, input().split())
    ans = factorial(m)//(factorial(m-n)*factorial(n))
    print(ans)