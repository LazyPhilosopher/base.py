input               = {}
dots_indexes        = []

base                = 16                    #int(input())
input[0]            = "0123456.789aBcDef"    #input() #first operand
input[1]            = "12345.acdf"           #input() #summarised operand
input[2]            = "1545.60AcdF"          #input() #subtracted operand

def system_check(system, number):
    failure = 0
    dots = 0
    dot_location = 0
    for i in range (len(number)):
        if( not (0 < system < 36)                                                               or
            not ((ord(number[i]) >= ord('0')) and ((ord(number[i]) <= ord('9'))))               and
            not ((ord('a') <= ord(number[i])) and (ord(number[i]) <= (ord('a') + system - 11))) and
            not ((ord('A') <= ord(number[i])) and (ord(number[i]) <= (ord('A') + system - 11))) and
                (number[i] != '.')):
                failure = 1
                break
        elif(number[i] == '.'):
            dots += 1
            dots_indexes.append(i)
    if(dots > 1):
        failure = 1
    return failure
           
failed = 0

for i in range(len(input)):
    failed = system_check(base, input[i])
    if(failed):
        break


if(failed):
    print("ERROR")

else:
    sum_1 = []
    sum_2 = []
    result= []
    if(dots_indexes[0] > dots_indexes[1]):
        for i in range(dots_indexes[0] - dots_indexes[1]):
            input[1] = '0' + input[1]
    elif(dots_indexes[1]  > dots_indexes[0]):
        for i in range(dots_indexes[1]  - dots_indexes[0]):
            input[0] = '0' + input[0]

    longest_number = max(len(input[0]), len(input[1]))
    for i in range (longest_number):
        try:
            a = input[0][longest_number - i - 1]
        except:
            a = '0'
        try:
            b = input[1][longest_number - i - 1]
        except:
            b = '0'
        sum_1.insert(0, a)
        sum_2.insert(0, b)

        increment = 0    
    for i in range(len(sum_1) - 1, -1, -1):
        a = 0
        b = 0
        if(sum_1[i] != '.'):
            if(ord(sum_1[i]) <= ord('9')):
               a = int(sum_1[i])
            elif(ord(sum_1[i]) <= (ord('A') + base - 11)): 
               a = ord(sum_1[i]) - ord('A') + 10
            elif(ord(sum_1[i]) <= (ord('a') + base - 11)): 
               a = ord(sum_1[i]) - ord('a') + 10

                

            if(ord(sum_2[i]) <= ord('9')):
               b = int(sum_2[i])
            elif(ord(sum_2[i]) <= (ord('A') + base - 11)): 
               b = ord(sum_2[i]) - ord('A') + 10
            elif(ord(sum_2[i]) <= (ord('a') + base - 11)): 
               b = ord(sum_2[i]) - ord('a') + 10

            if((a + b + increment) < 10):
                #result.insert(0, (a+b))
                a = a + b + increment            
            else:
                #result.insert(0, chr(87 + a + b))
                a = a + b + increment
            increment = 0

            if(a >= base):
                a = a - base
                increment = 1

            if(a < 10):
                result.insert(0, a)
            else:
                result.insert(0, chr(87 + a))
        else:
            result.insert(0, '.')

        
    print(sum_1)
    print(sum_2)
    print(result)
    print(dots_indexes)




