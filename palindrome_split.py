import time


def solve (S):
    # Write your code here
    # N - length of S
    N = len(S)
    freq = []
    count = 0

    for s in S:
        if s not in freq:
            f = S.count(s)
            freq.append(s)
            
            if f >= 2:            
                count+= (f//2)

    return int(count)

def p(S):
    # Write your code here
    # N - length of S
    N = len(S)
    char_dict = {}
    count = 0

    for s in S:
        if s not in char_dict:
            char_dict[s] = 0
        char_dict[s]+=1

    
    for i in char_dict:
        f = char_dict[i]

        if f >= 2:
            count+= (f//2)

    return int(count)


        




avg = []

for i in range(10):
    start = time.time()
    solve("abbcccddddeeeeffffggghhhiiijkdshgalkfhsdaljhjfdhsauehwjnfbadjhuehfieweuffhhhhhhhhhhhhheeeeeeeeeeeeeeeeeeeeehdbjcksojudcdcvesdffffffffffffffffffffffafdaffffopopofpefijijr")
    end = time.time()

    finish = end - start
    avg.append(round(finish, 10))

print (f"Test 1: {sum(avg)/len(avg)}")


avr = []
for j in range(10):
    st = time.time()
    p("abbcccddddeeeeffffggghhhiiijkdshgalkfhsdaljhjfdhsauehwjnfbadjhuehfieweuffhhhhhhhhhhhhheeeeeeeeeeeeeeeeeeeeehdbjcksojudcdcvesdffffffffffffffffffffffafdaffffopopofpefijijr")
    en = time.time()

    fin = en - st
    avr.append(round(fin, 10))

print (f"Test 2: {sum(avr)/len(avr)}")



print (""*3)
# print (    solve("abbcccddddeeeeffffggghhhiiijkdshgalkfhsdaljhjfdhsauehwjnfbadjhuehfieweuffhhhhhhhhhhhhheeeeeeeeeeeeeeeeeeeeehdbjcksojudcdcvesdffffffffffffffffffffffafdaffffopopofpefijijr")
# )

# print (p("abbcccddddeeeeffffggghhhiiijkdshgalkfhsdaljhjfdhsauehwjnfbadjhuehfieweuffhhhhhhhhhhhhheeeeeeeeeeeeeeeeeeeeehdbjcksojudcdcvesdffffffffffffffffffffffafdaffffopopofpefijijr"))