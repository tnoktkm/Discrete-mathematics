count_edge = int(input("Enter count Edge - "))
Edges = []

for i in range(count_edge):
    first_vertice, second_vertice, weight = input().split()
    weight = int(weight)

    Edges.append((first_vertice, second_vertice, weight))
    n -= 1



    

SERIAL_WEIGHT = 2
Edges.sort(key=lambda v: v[SERIAL_WEIGHT])

Sets = []
SERIAL_FIRST_VERTICE = 0
SERIAL_SECOND_VERTICE = 1
FIRST_EDGE = 0
Sets.append(set(Edges[FIRST_EDGE][SERIAL_FIRST_VERTICE]).union(Edges[FIRST_EDGE][SERIAL_SECOND_VERTICE]))

print("\n")
print("Just first edge = ", Edges[FIRST_EDGE])

COUNT_ALREADY_ADDED_EDGE = 1
count_edge = len(Edges) - COUNT_ALREADY_ADDED_EDGE

count_set = 0
is_cycle = False
is_a = False
is_b = False
sum_weight = Edges[FIRST_EDGE][SERIAL_WEIGHT]

for edge in Edges:
    if count_edge == 0:
        break
    count_edge -= 1

    for i_set in Sets:
        if (edge[SERIAL_FIRST_VERTICE] in i_set) and (edge[SERIAL_SECOND_VERTICE] in i_set):
            is_cycle = True
            break

        for a in Sets:
            if (edge[SERIAL_FIRST_VERTICE] in a):
                aMemory = a
                aMemoryCheck = True

        for b in Sets:
            if (rebro[SERIAL_SECOND_VERTICE] in b):
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
    if not isNew:
        if (not (rebro[0] in item)) and not ((rebro[1] in item)):
            COUNT_SET += 1
            listSet.append(set(rebro[0]))
            listSet[k].add(rebro[1])
            print("новое множество ребер, ",rebro)
            summa += rebro[2]
    isNew = True
    aMemoryCheck = False
    bMemoryCheck = False

print("Его длина равна = ", summa)