def mul(P, Q):             # Янголь -- h)

    if P == [0] or Q == [0] or P == 0 or Q == 0:
        return [0]
    else:
        n0_P = len(P) - 1
        n0_Q = len(Q) - 1
        n0_R = n0_P + n0_Q

        R = list()
        for k in range(n0_R + 1):
            R.append(0)

        for i in range(n0_P + 1):
            for j in range(n0_Q + 1):
                R[i + j] += (P[n0_P - i] * Q[n0_Q - j])

        return _delzeroes(R)
