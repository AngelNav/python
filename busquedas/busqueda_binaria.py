import random


def binary_search(list_numbers, start, end, target):
    print(
        f'buscando {target} entre {list_numbers[start]} y {list_numbers[end -1]}')
    if start > end:
        return False

    center = (start + end) // 2

    if list_numbers[center] == target:
        return True
    elif list_numbers[center] < target:
        return binary_search(list_numbers, center + 1, end, target)
    else:
        return binary_search(list_numbers, start, center - 1, target)


def run():
    list_range = int(input("Tamaño de la lista: "))
    target = int(input("Objetivo: "))

    list_numbers = sorted([random.randint(0, 100) for i in range(list_range)])

    found = binary_search(list_numbers, 0, len(list_numbers), target)

    print(list_numbers)
    print(
        f'El elemento {target} {"está" if found else "no está"} en la lista')


if __name__ == "__main__":
    run()
