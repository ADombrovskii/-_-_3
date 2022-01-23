max_l_a = {8: 0, 9: 0, 10: 0, 11: 0}
max_l_g = {8: 0, 9: 0, 10: 0, 11: 0}
max_a = 0
max_g = 0

with open("mat_dv.txt", "r") as f:
    for i in f:
        l = i.split()

        for j in range(4):
            if int(l[2]) == 8 + j:
                if l[3] > max_l_a[8 + j]:
                    max_l_a[8 + j] = l[3]
                if l[4] > max_l_g[8 + j]:
                    max_l_g[8 + j] = l[4]

        max_a = max(max_l_a[8], max_l_a[9], max_l_a[10], max_l_a[11])
        max_b = max(max_l_g[8], max_l_g[9], max_l_g[10], max_l_g[11])

with open("mat_dv.txt", "r") as f:
    for i in f:
        l = i.split()

        for j in range(4):
            if max_l_a[8 + j] == int(l[3]):
                print('Победитель по алгебре в ', 8 + j, 'классе -', l[0], l[1])
            if max_l_g[8 + j] == int(l[4]):
                print('Победитель по геометрии в ', 8 + j, 'классе -', l[0], l[1])
            if max_a == int(l[3]):
                print('Абсолютный победитель по алгебре учится в', l[2], 'классе - ', l[0], l[1])