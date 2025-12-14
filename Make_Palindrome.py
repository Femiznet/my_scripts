
def solve (N, S):
    # Write your code here
    if N != len(S):
        return

    if N <= 1:
        return 0
    
    if S == S[::-1]:
        return 0
    
    freq = 0
    freq_list = []
    for s in S:
        if s not in freq_list:
            f = S.count(s)
            if f > 1:
                if f % 2 != 0:
                    f = f - 1
                freq+=f
        freq_list.append(s)        

    odd_s = N - freq
    if odd_s <=1:
        return 0

    return odd_s - 1

