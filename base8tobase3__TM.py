
def check_ans(s, inx):
    w = s[:inx]
    for i in range(len(w)):
        if w[i] != '0':
            return False
    return True

def assign_str(str1, val, inx):
    str1 = list(str1)
    str1[inx] = val

    str1 = "".join(str1)
    return str1


def max_(sn):
    max = sn[0]
    for i in range(1, len(sn)):
        if sn[i] > max:
            max = sn[i]
    
    return int(max)



s = input("Enter your number (in base 8) : ")
s += "#"

if max_(s) > 8:
    print("Please Enter a number in base 8")
else:
    index_sharp = 0
    is_sharp_find = False

    adder = 0
    subtra = 0

    flag_left = 0 # flag_left --> undone left side
    flag = 0

    i = 0

    # program second
    while ( True ):

        if (s[i]) == '#':
            index_sharp = i
            flag = 1
            is_sharp_find = True
        elif is_sharp_find == False:
            i = i + 1            

        if flag == 1 and flag_left == 0: # flag_left --> undone left side
            i = i - 1
            flag = 0

            
            while s[i] == '0':
                s = assign_str(s, '7', i)
                i = i - 1
            subtra = str(int(s[i]) - 1) # 3# -- -1 --> 2#
            s = assign_str(s, subtra, i)
            flag_left = 1

        
        elif flag == 1 and flag_left == 1:
            
            # for go to the end of string.
            while (i < len(s)-1):
                i += 1
            
            
            flag = 0

            while (s[i]) == '2':
                s = assign_str(s, '0', i)
                i = i - 1
                
                flag = 1
        
            if s[i] == '#':
                s = assign_str(s, "#0", i)
                i = i + 1
            adder = str( int(s[i]) + 1 ) # 3# -- +1 --> 4#
            flag = 0

            s = assign_str(s, adder, i)
            flag_left = 0

        if is_sharp_find == True :
            if flag_left == 0 :
                i -= 1
            else:
                i += 1
        
        # Identify the answer
        if (is_sharp_find==True and flag_left==0):
            if(check_ans(s, index_sharp) == True):
                break

print("your ans ( in base 3 ) : ", s[index_sharp+1:])
