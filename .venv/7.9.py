for S in range(1, 10):
    for E in range(0, 10):
        if E == S:
            continue
        for N in range(0, 10):
            if N in [E, S]:
                continue
            for D in range(0, 10):
                if D in [N, E, S]:
                    continue
                for M in range(1, 10):
                    if M in [D, N, E, S]:
                        continue
                    for O in range(0, 10):
                        if O in [M, D, N, E, S]:
                            continue
                        for R in range(0, 10):
                            if R in [O, M, D, N, E, S]:
                                continue
                            SEND = S*1000 + E*100 + N*10 + D
                            MORE = M*1000 + O*100 + R*10 + E
                            if 1000 <= SEND <= 9999 and 1000 <= MORE <= 9999:
                                MONEY = SEND + MORE
                                Y = MONEY % 10
                                M_1 = MONEY // 10000
                                O_1 = MONEY // 1000 % 10
                                N_1 = MONEY // 100 % 10
                                E_1 = MONEY // 10 % 10
                                if M_1 == M and O_1 == O and N_1 == N and E_1 == E:
                                    if len(set(str(MONEY))) == 5:
                                        print(f'SEND = {SEND}')
                                        print(f'MORE = {MORE}')
                                        print(f'MONEY = {MONEY}')
                                        





