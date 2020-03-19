n = int(input())
listq = list(map(int, input().split()))
res = []
for i in range(len(listq)-1):
    for j in range(i+1, len(listq)):
        lista = listq[:]
        lista[i], lista[j] = lista[j], lista[i]
        res.append(lista)
print(res)
ans = list(set([tuple(_) for _ in res]))
print(ans)

print(len(ans))