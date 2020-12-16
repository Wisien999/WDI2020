def solve(board, w):
    szachowane_s = 0
    for x in range(len(w)):
        y = w[x]

        szachowane_s += sum(board[y])

        for k in range(len(board)):
            szachowane_s += board[k][x]

        



    for i in range(len(w)):
        y1 = w[i]
        exist1 = False
        for j in range(len(w)):
            if i != j and y1 == w[j]:
                exist1 = True
                break

        for j in range(len(w)):
            if i == j:
                continue

            y2 = w[j]
            exist2 = False

            for k in range(len(w)):
                if k != j and y2 == w[k]:
                    exist2 = True
                    break
            

            