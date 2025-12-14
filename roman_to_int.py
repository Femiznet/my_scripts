def rom(roman:str):
    roman = roman.upper()
    roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
    length_roman = len(roman)
    idx = 0
    result = 0

    while idx < length_roman:
        init = roman_dict[roman[idx]]
        idx_2 = idx+1
        next = 0
        if idx_2 <= length_roman-1:
            next = roman_dict[roman[idx_2]]

        if init < next:
            result += (next - init)
            idx+=2
        else:
            result+=init
            idx+=1

    return result




        
