n = int(input("Enter count V"))

V = []

for i in range(n):
    e1 = input() #вершина 1
    e2 = input() #вершина 2
    w = int(input()) #вес ребера
    V.append((e1, e2, w))
    n = n - 1

V.sort(key=lambda v: v[2])

for item in V:
    print(item)

listSet = []
listSet.append(set(V[0][0]))
(listSet[0]).add(V[0][1])

print("\n")
print("просто первое ребро, ", V[0])

n = len(V) - 1 #так как максильное количество ребер на n вершинах меньше на 1.(дерево)

k = 0
isNew = True
aMemoryCheck = False
bMemoryCheck = False
summa = V[0][2]

for rebro in V:
    if n == 0:
        break
    n = n - 1
    for item in listSet:
        if (rebro[0] in item) and (rebro[1] in item):
            isNew = False
            break

        for a in listSet:
            if (rebro[0] in a):
                aMemory = a
                aMemoryCheck = True

        for b in listSet:
            if (rebro[1] in b):
                bMemory = b
                bMemoryCheck = True
        
        if (aMemoryCheck and bMemoryCheck):
            for p in listSet:
                if (p == aMemory):
                    listSet.append(set.union(aMemory, bMemory))
                    listSet.remove(bMemory)
                    listSet.remove(aMemory)
            aMemoryCheck = False
            bMemoryCheck = False
            print("объединили множества ребер, ", rebro)
            summa += rebro[2]
            break



        if (rebro[0] in item) or (rebro[1] in item):
            isNew = False
            item.add(rebro[0])
            item.add(rebro[1])  
            print("добавили ребро в множество, ", rebro)
            summa += rebro[2]
            break
    if isNew:
        if (not (rebro[0] in item)) and not ((rebro[1] in item)):
            k = k + 1
            listSet.append(set(rebro[0]))
            listSet[k].add(rebro[1])
            print("новое множество ребер, ",rebro)
            summa += rebro[2]
    isNew = True
    aMemoryCheck = False
    bMemoryCheck = False

print("Его длина равна = ", summa)