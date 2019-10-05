
def system_check(system, number):
    alphabet = ['0','1','2','3','4','5','6','7','8','9',
                'a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t',
                'u','v','w','x','y','z']
    number = number.lower()
    failure = 0
    dots = 0
    sign = 0
    dot_location = 0
    for i in range (len(number)):
        if(number[i] != '.'):
            if(number[i] != '-' and number[i] != '+'):
                if(alphabet.index(number[i]) >= system):
                    failure = 1
                    break
            else:
                sign += 1
        else:
            dots += 1
            dots_indexes.append(i - sign)
    if(dots > 1 or sign > 1):
        failure = 1
    elif(dots == 0):
        dots_indexes.append(-1)

    return failure            ###CHECKED###

def format(input):
    dots_indexes.clear()
    for i in range(len(input)):
        failed = system_check(base, input[i])
    negativity = []

    for i in range (len(input)):
        if(input[i][0] == '-'):
            negativity.append(1)
        else:
            negativity.append(0)

    iterations = abs(max(dots_indexes))
    for i in range (len(input)):
        tmp0 = list(input[i])

        if(dots_indexes[i] == -1):
            sign = 0
            if(tmp0[0] == '+' or tmp0[0] == '-'):
                sign = 1
            dots_indexes[i] = len(tmp0) - sign
            tmp0.append('.') 
            tmp0.append('0')
        if(tmp0[0] == '-' or tmp0[0] == '+'):
            del tmp0[0];

        for x in range (iterations - dots_indexes[i]):
            tmp0.insert(0, '0')

        if(negativity[i] == 1):
            input[i] = '-' + ''.join(tmp0)
        else:
            input[i] = '+' + ''.join(tmp0)          
            
    max_len = 0
    for i in range(len(input)):
        if (len(input[i]) > max_len): 
            max_len = len(input[i])

    for i in range(len(input)):
        length = len(input[i])
        for x in range(max_len - length):
            input[i] = input[i] + '0'                           ###CHECKED###

def value_comparison(operand_0, operand_1):

    alphabet = ['0','1','2','3','4','5','6','7','8','9',
             'a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z']
    output = -1

    for i in range(1, len(operand_0)):
        if(operand_0[i] != '.'):
            if(alphabet.index(operand_0[i]) > alphabet.index(operand_1[i])):
                output = 0
                break
            elif(alphabet.index(operand_0[i]) < alphabet.index(operand_1[i])):
                output = 1
                break
 
    return output  ###CHECKED###

def sum(operand_0, operand_1):
    sum_1 = [char for char in operand_0.lower()]
    sum_2 = [char for char in operand_1.lower()]
    result = []
    increment = 0 
    
    for i in range(len(sum_1) - 1, -1, -1):
        a = 0
        b = 0
        if(sum_1[i] != '.'):
            if(ord(sum_1[i]) <= ord('9')):
               a = int(sum_1[i])
            elif(ord(sum_1[i]) <= (ord('a') + base - 11)): 
               a = ord(sum_1[i]) - ord('a') + 10
    
                
    
            if(ord(sum_2[i]) <= ord('9')):
               b = int(sum_2[i])
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
    
    output = ''
    if(increment):
        result.insert(0, '1')
    return output.join(str(x) for x in result)

def sub(operand_0, operand_1):
    sub_0 = [char for char in operand_0.lower()]
    sub_1 = [char for char in operand_1.lower()]
    result = []

    decrement = 0    
  
    for i in range(len(sub_0) - 1, -1, -1):
        a = 0
        b = 0
        if(sub_0[i] != '.'):
            if(ord(sub_0[i]) <= ord('9')):
               a = int(sub_0[i])
            elif(ord(sub_0[i]) <= (ord('a') + base - 11)): 
               a = ord(sub_0[i]) - ord('a') + 10

                

            if(ord(sub_1[i]) <= ord('9')):
               b = int(sub_1[i])
            elif(ord(sub_1[i]) <= (ord('a') + base - 11)): 
               b = ord(sub_1[i]) - ord('a') + 10

            if((a - b - decrement) < 10):
                #result.insert(0, (a+b))
                a = a - b - decrement            
            else:
                #result.insert(0, chr(87 + a + b))
                a = a - b - decrement
            decrement = 0

            if(a < 0):
                a = a + base
                decrement = 1

            if(a < 10):
                result.insert(0, a)
            else:
                result.insert(0, chr(87 + a))
        else:
            result.insert(0, '.')

    output = ''
    return output.join(str(x) for x in result)

def sum_operation(operand_0, operand_1):
    max_abs_val = value_comparison(operand_0, operand_1)
    operand_0_is_negative = 0
    operand_1_is_negative = 0
    result_is_positive = 0
    result = ''

    if(operand_0[0] == '-'):
        operand_0_is_negative = 1
    if(operand_1[0] == '-'):
        operand_1_is_negative = 1
    
    tmp0 = list(operand_0)
    del tmp0[0]
    operand_0 = ''.join(tmp0)

    tmp0 = list(operand_1)
    del tmp0[0]
    operand_1 = ''.join(tmp0)

    if(max_abs_val == 0):
        if(operand_0_is_negative):
            if(operand_1_is_negative):
                result = sum(operand_0, operand_1)    # -2 - 1
                # RESULT IS NEGATIVE
                result_is_positive = 0
            elif(not operand_1_is_negative):
                tmp = 0
                result = sub(operand_0, operand_1)    # -2 + 1
                # RESULT IS NEGATIVE
                result_is_positive = 0
        elif(not operand_0_is_negative):
            if(operand_1_is_negative):
                result = sub(operand_0, operand_1)    # 2 - 1
                # RESULT IS POSITIVE
                result_is_positive = 1
            elif(not operand_1_is_negative):
                result = sum(operand_0, operand_1)    # 2 + 1
                # RESULT IS POSITIVE
                result_is_positive = 1
    elif(max_abs_val == 1 or max_abs_val == -1):
        if(operand_1_is_negative):
            if(operand_0_is_negative):
                result = sum(operand_0, operand_1)    # -1 - 2
                # RESULT IS NEGATIVE
                result_is_positive = 0
            elif(not operand_0_is_negative):
                result = sub(operand_1, operand_0)    # 1 - 2
                # RESULT IS NEGATIVE
                result_is_positive = 0
        elif(not operand_1_is_negative):
            if(operand_0_is_negative):
                result = sub(operand_1, operand_0)    # -1 + 2
                # RESULT IS POSITIVE
                result_is_positive = 1
            elif(not operand_0_is_negative):
                result = sum(operand_0, operand_1)    # 1 + 2
                # RESULT IS POSITIVE
                result_is_positive = 1
    
    if(result_is_positive):
        result = '+' + result
    else:
        result = '-' + result
    return result

def sub_operation(operand_0, operand_1):
    max_abs_val = value_comparison(operand_0, operand_1)
    operand_0_is_negative = 0
    operand_1_is_negative = 0
    result_is_positive = 0
    result = ''

    if(operand_0[0] == '-'):
        operand_0_is_negative = 1
    if(operand_1[0] == '-'):
        operand_1_is_negative = 1
    
    tmp0 = list(operand_0)
    del tmp0[0]
    operand_0 = ''.join(tmp0)

    tmp0 = list(operand_1)
    del tmp0[0]
    operand_1 = ''.join(tmp0)

    if(max_abs_val == 0):
        if(operand_0_is_negative):          
            if(operand_1_is_negative):
                result = sub(operand_0, operand_1)  #-2+1
                #RESULT IS NEGATIVE
                result_is_positive = 0
            elif(not operand_1_is_negative):
                result = sum(operand_0, operand_1)  #-2-1
                #RESULT IS NEGATIVE
                result_is_positive = 0
        elif(not operand_0_is_negative):
            if(operand_1_is_negative):
                result = sum(operand_0, operand_1)  #2+1
                #RESULT IS POSITIVE
                result_is_positive = 1
            elif(not operand_1_is_negative):
                result = sub(operand_0, operand_1)  #2-1
                #RESULT IS POSITIVE
                result_is_positive = 1
    elif(max_abs_val == 1):
        if(operand_1_is_negative):
            if(operand_0_is_negative):
                result = sub(operand_1, operand_0)   #-1+2
                #RESULT IS POSITIVE
                result_is_positive = 1
            elif(not operand_0_is_negative):
                result = sum(operand_0, operand_1)  #1+2
                #RESULT IS POSITIVE
                result_is_positive = 1
        elif(not operand_1_is_negative):
            if(operand_0_is_negative):
                result = sum(operand_0, operand_1)  #-1-2
                #RESULT IS NEGATIVE
                result_is_positive = 0
            elif(not operand_0_is_negative):
                result = sub(operand_1, operand_0)  #1-2
                #RESULT IS NEGATIVE
                result_is_positive = 0

    if(result_is_positive):
        result = '+' + result
    else:
        result = '-' + result
    return result

def side_zeros_check(argument):
    result_left = []
    result_right = []
    negative_output = 0
    only_zeros = 1

    for i in range (len(argument)):
        if(argument[i] != '0' or only_zeros != 1 or argument[i+1] == '.'):
            if(argument[i] == '-'):
                negative_output = 1
            elif(argument[i] != '+'):
                only_zeros = 0
                result_left.insert(len(argument), argument[i])

    only_zeros = 1
    for i in range (len(result_left)):
        if(result_left[len(result_left) - i - 1] != '0' or only_zeros != 1 or result_left[len(result_left) - i - 1] == '.'):
            only_zeros = 0
            result_right.insert(0, result_left[len(result_left) - i - 1])
    if(negative_output):
        result_right.insert(0, '-')
    output = '' 
    return(output.join(str(x) for x in result_right))


##################################################################################################################################
base         = int(input())
input        = [input(), input(), input()]
dots_indexes        = []

failed = 0
dots_indexes.clear()
for i in range(len(input)):
    failed = system_check(base, input[i])
    if(failed):
        print("ERROR")
        break

if(not failed):
    format(input)

    #print(input[0])
    #print(input[1])
    #print(input[2])
    #print("==============")
    input[0] = sum_operation(input[0], input[1])
    format(input)
    input[0] = sub_operation(input[0], input[2])
    input[0] = side_zeros_check(input[0])
    print(input[0])
    #value_comparison(input[0], input[1])
    