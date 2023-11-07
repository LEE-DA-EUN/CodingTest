from string import ascii_lowercase
ls = list(ascii_lowercase)
s = list(input())
ans = [0 for i in range(len(ls))]
for i in range(len(s)):
    index = ls.index(s[i])
    ans[index] += 1
print(*ans)