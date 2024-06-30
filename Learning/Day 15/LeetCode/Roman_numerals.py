sym = ["M", "D", "C", "L","X", "V", "I"]
val = [1000, 500, 100, 50, 10, 5,1]

def rom_to_int(num):
    i=0
    roman_num = ""
    while num>0:
        for _ in range(num//val[i]):      
            roman_num+=sym[i]
            num-=val[i]
        i+=1
    return roman_num
        
print(rom_to_int(1453))
