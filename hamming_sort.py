
def solve (N:int, K:int, A:list):
    # Write your code here


    h_d = [(bin(num^K).count("1"), num) for num in A]

    out = sorted(h_d, key=lambda x: (x[0],x[1]))


    return [num for (_,num) in out]
        




            





