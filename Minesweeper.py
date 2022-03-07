def igra(lista):
    for indexi in range(0, len(lista)):
        for indexj in range(0, len(lista[indexi])):
            brojac = 0
            if lista[indexi][indexj] == '-':
                if indexi - 1 >= 0:
                    if indexj - 1 >= 0 and lista[indexi - 1][indexj - 1] == '#':
                        brojac += 1
                if indexi - 1 >= 0 and lista[indexi - 1][indexj] == '#':
                    brojac += 1
                if indexi - 1 >= 0:
                    if indexj + 1 < len(lista) and lista[indexi - 1][indexj + 1] == '#':
                        brojac += 1
                if indexj + 1 < len(lista) and lista[indexi][indexj + 1] == '#':
                    brojac += 1
                if indexi + 1 < len(lista):
                    if indexj + 1 < len(lista) and lista[indexi + 1][indexj + 1] == '#':
                        brojac += 1
                if indexi + 1 < len(lista) and lista[indexi + 1][indexj] == '#':
                    brojac += 1
                if indexi + 1 < len(lista):
                    if indexj - 1 >= 0 and lista[indexi + 1][indexj - 1] == '#':
                        brojac += 1
                if indexj - 1 >= 0 and lista[indexi][indexj - 1] == '#':
                    brojac += 1

                lista[indexi][indexj] = brojac

    for i in lista:
        vrednosti = '   '.join(str(vred) for vred in i)
        print(vrednosti)

    return lista


if __name__ == "__main__":
    br = int(input())
    lista = []
    for x in range(0, br):
        informacii = input().split("   ")
        pom = []

        for y in informacii:
            pom.append(y)
        lista.append(pom)
    igra(lista)
