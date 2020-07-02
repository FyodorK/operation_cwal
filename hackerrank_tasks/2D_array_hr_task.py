"""
Solution for https://www.hackerrank.com/challenges/2d-array/problem
"""


def hg_pat(i, j, arr):
    try:
        hg = [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j+1], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
    except:
        return "Flag"
    return sum(hg)


def main():
    arr = []
    with open("test_input_2D_array_task.txt", "r") as f:
        for line in f.readlines():
            arr.append(list(map(int, line.rstrip().split())))
    hg_sums = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if hg_pat(i, j, arr) != "Flag":
                hg_sums.append(hg_pat(i, j, arr))
    print((hg_sums))


if __name__ == '__main__':
    main()
