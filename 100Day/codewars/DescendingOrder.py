def descending_order(num):
    num1 = str(num)
    list1 = list(num1)
    list2 = sorted(list1, reverse=True)
    string_1 = ''.join(list2)
    final_integer = int(string_1)

    return final_integer
num = 2345678
print(descending_order(num))


def Descending_Order2(num2):
    return int("".join(sorted(str(num2), reverse=True)))
