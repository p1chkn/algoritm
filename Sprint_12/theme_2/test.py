n = int(input())
cnt1 = cnt2 = cnt3 = 1
lst = [1]
for i in range(n-1):
    f1, f2, f3 = cnt1*2, cnt2*3, cnt3*5
    min_f = min(f1, f2, f3)
    if min_f == f1:
        cnt1 += 1
    if min_f == f2:
        cnt2 += 1
    if min_f == f3:
        cnt3 += 1
    lst.append(min_f)
print(lst[-1])
