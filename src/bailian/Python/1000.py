s = input().split()
print(int(s[0]) + int(s[1]))
#以下代码也能通过
while True:
    try:
        s = input().split()
        print(int(s[0]) + int(s[1]))
    except:
        break
