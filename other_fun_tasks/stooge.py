"""
Fun task for Auriga New Year challenge :)
"""


def check_string(item):
    if item.count("O") != item.count("="):
        raise Exception("There are one or more halved children in you input")


def my_split(str):
    inds = [i for i in range(len(str)+1) if i % 2 == 0]
    result = []
    for i in inds:
        x = i
        y = i+2
        if y <= len(str):
            r = str[x:y]
            result.append(r)
    return result


def check_children(test_string):
    ice_hill = "=O"  # to the ice_hill
    pedo = "O="  # to a pedophile

    children = {"ice_hill": 0, "pedo": 0}

    vector = test_string.split("D")

    if len(vector) > 2:
        raise Exception("Should be only one DEAD MOROSE")

    if len(vector[0]) > 0:
        check_string(vector[0])
        sub_ = my_split(vector[0])
        children["ice_hill"] += sub_.count(ice_hill)
        children["pedo"] += sub_.count(pedo)

    if len(vector[1]) > 0:
        check_string(vector[1])
        sub_ = my_split(vector[1])
        children["ice_hill"] += sub_.count(ice_hill)
        children["pedo"] += sub_.count(pedo)

    return children


def main():

    tested_string = input("Enter your string: ")

    result = check_children(tested_string)
    print(result["ice_hill"])


if __name__ == '__main__':
    main()
