n = int(input())

text = ""

for i in range(n):
    text += " " + input()

t = int(input())

for i in range(t):
    a = input()
    b = a[:-2] + 'se'
    count = text.count(a) + text.count(b)
    print(count)
