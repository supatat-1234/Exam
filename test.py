def check(arr):
    ans = ''
    cross_1, cross_2 = 0, 0
    # cross_1 => บนซ้าย ล่างขวา
    # cross_2 => ล่างซ้าย บนขวา
    for i in range(3):
        verx, vero = 0, 0
        # verx => แนวตั้งเช็คตัวแปร x
        # vero => แนวตั้งเช็คตัวแปร o
        horx, horo = 0, 0
        # horx => แนวนอนเช็คตัวแปร x
        # horo => แนวนอนเช็คตัวแปร o
        for j in range(3):
            if (arr[i][j] == 1):
                horx += 1
            if (arr[i][j] == 2):
                horo += 1
            if (arr[j][i] == 1):
                verx += 1
            if (arr[j][i] == 2):
                vero += 1
        if (arr[i][i] == 1):
            cross_1 += 1
        if (arr[i][i] == 2):
            cross_2 += 1
        if (verx == 3 or horx == 3 or cross_1 == 3):
            ans = "X Win"
        if (vero == 3 or horo == 3 or cross_2 == 3):
            ans = "Y Win"
            
    cross_1, cross_2 = 0, 0
    for i in range(0,3,1):
        if (arr[i][j-i] == 1):
            cross_1 += 1
        if (arr[i][j-i] == 2):
            cross_2 += 1
    if (cross_1 == 3):
        ans = "X Win"
    if (cross_2 == 3):
        ans = "Y Win"
    if len(ans) == 0:
        return "null"
    return ans



ans = check(
    [[1,2,1],
    [1,2,2],
    [1,0,2]])
print(ans)
