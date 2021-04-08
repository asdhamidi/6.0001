s = "A_ pp_ e"
s1 = "Apple"

count = 0
for r in range(len(s)):
    if s[r] == '_':
        count += 1

if (len(s) - (2 * count)) != len(s1):
    print("yes")