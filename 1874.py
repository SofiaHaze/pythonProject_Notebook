n = int(input())

indicate = 1
s = []
r = []
no_message = True


for i in range(0,n):
    x = int(input())

    #x와 같은 값을 s리스트에 넣은후 pop해야하므로 같거나 작을때까지
    while indicate <= x:
        s.append(indicate)
        r.append("+")
        indicate += 1

    if s[-1] == x:
        s.pop()
        r.append("-")
    else:
        no_message = False
        break

if no_message == False:
    print("NO")
else:
    print("\n".join(r))