def f(s):
    c = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            c += 1
    return c

s = input()
c = f(s)
if c == 1:
    print("YES")
else:
    print("NO")
