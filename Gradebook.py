def ocena(teorija, prakticno, lab):  # funkcija za presmetka na ocenka na studentot spored br na poeni
    poeni = int(teorija) + int(prakticno) + int(lab)
    if poeni <= 50:
        return 5
    if poeni > 50 and poeni <= 60:
        return 6
    if poeni > 60 and poeni <= 70:
        return 7
    if poeni > 70 and poeni <= 80:
        return 8
    if poeni > 80 and poeni <= 90:
        return 9
    if poeni > 90 and poeni <= 100:
        return 10


if __name__ == '__main__':
    students = {}  # recnik
    informacii = input()  # chitanje na podatoci
    j = 1
    lista1 = {}
    lista = {}
    pom = []
    list = []
    while informacii != "end":  # uslov:se dodeka ne se vnese end chitaj

        students["ime"], students["prezime"], students["index"], students["predmet"], students["poeniteorija"], \
        students["poeniprakticno"], students["poenilabs"] = informacii.split(",")
        # print("pred da gi dodelam ",students)
        t1 = (students["ime"], students["prezime"], students["index"])
        # print("Torka eden: ",t1)
        t2 = (students["predmet"], ocena(students["poeniteorija"], students["poeniprakticno"], students["poenilabs"]))
        # print("Torka dva: ",t2)
        students = {}
        # print(students)
        # print(lista[t1])
        # print(lista.values())
        # print("Listata e: ",lista)

        if j == 1:
            if t1 not in students.keys():
                list = []
                list.append(t2)
                # print("aj listov kolku e:",list)
                lista[t1] = list
                # print(lista)
                j = 0
        else:
            if t1 not in lista.keys():
                list = []
                list.append(t2)
                lista[t1] = list
                # print(lista)
            else:
                pom = lista[t1]
                pom.append(t2)
                lista[t1] = pom
                # print(lista)

        # print(students)

        informacii = input()
    # print(students)
    # print("konecnata lista",lista)
    for i in lista:
        # print("ito e",i)
        print("Student: " + i[0] + ' ' + i[1])
        for j in lista[i]:
            print("	" + j[0] + ": " + str(j[1]))
        print("")