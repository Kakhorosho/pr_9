for A in range(1, 10):
    for B in range(0, 10):
        for C in range(1, 10):
            for D in range(1, 10):
                ABCDCB = A*10**5 + B*10**4 + C*10**3 + D*100 + C*10 + B
                ABCDCB_1 = ABCDCB + 1
                B_1_ABCDB_1 = ABCDCB_1 % 10
                B_2_ABCDB_1 = ABCDCB_1 // 10000 % 10
                if B_1_ABCDB_1 == B_2_ABCDB_1:
                    ABCDCB_2 = ABCDCB_1 + 1
                    E_1_ABCDCB_2 = ABCDCB_2 // 10000 % 10
                    E_2_ABCDCB_2 = ABCDCB_2 // 10 % 10
                    F_1_ABCDCB_2 = ABCDCB_2 // 1000 % 10
                    F_2_ABCDCB_2 = ABCDCB_2 // 100 % 10
                    if E_1_ABCDCB_2 == E_2_ABCDCB_2 and F_1_ABCDCB_2 == F_2_ABCDCB_2:
                        ABCDCB_3 = ABCDCB_2 + 1
                        B_1 = ABCDCB_3 % 10
                        B_2 = ABCDCB_3 // 100000
                        E_1 = ABCDCB_3 // 10000 % 10
                        E_2 = ABCDCB_3 // 10 % 10
                        F_1 = ABCDCB_3 // 1000 % 10
                        F_2 = ABCDCB_3 // 100 % 10
                        if B_1 == B_2 and E_1 == E_2 and F_1 == F_2:
                            print(f'Мой первый пробег был = {ABCDCB}')
