for A in range(1, 10):
    for B in range(0, 10):
        AB = A*10 + B
        double_AB = AB**2
        if 100 <= double_AB <= 999:
            C = double_AB // 100
            remain = double_AB % 100
            A_1 = remain // 10
            B_1 = remain % 10
            if A_1 == A and B_1 == B:
                print(A, B, C)
print(4560 // 100)