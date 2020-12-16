def solve(k):
    a, b = 1, 2
    la, lb = 1, 2
    i = 1

    while True:
        # print(a, b)
        if abs(k-la) < abs(k-a):
            print("ciąg A nr", i-1)
            return 

        if abs(k-lb) < abs(k-b):
            print("ciąg B nr", i-1)
            return 


        la, lb = a, b
        b = b+a
        a = a + b/3
        i += 1


solve(int(input()))