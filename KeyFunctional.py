from array import array
from tkinter import simpledialog

from OperatorsFunctionality import operatorsFunction

def var_reveal(Input, index, var_arr):
    #check for var in var_arr
    for index in range(len(var_arr)):
        if(Input == var_arr[index][0]):
            return var_arr[index][1]

def line_compile(Input, Token, var_arr, varTable, finalTokenArr):
    #print(Input)
    # print(Token)

    #take the 2 lines, read each word from token
    for index in range(len(Token)):
        inword = Input[index]       #important when handling idents, str, ints, and int_lit
        tkword = Token[index]       #compare each word with the token
        print(inword)
        print(f"line{index}: {Input}")
                
        match tkword:
            case "IOL":
                #do nothing
                print("IOL")
                
            case "LOI":
                #write end of code
                print("End of Code")

            case "IS":
                #assign value from the next to previous
                var_arr.append(IS_func(Input, varTable, index, Token, var_arr))
                print("Assigned value to " + Input[index-1])

            case "BEG":
                #stop the program and ask the user for value
                var_arr.append(BEG_func(Input, Token, var_arr, varTable, index))
                
            
            case "PRINT":
                PRINT_func(Input, Token, varTable, index, var_arr)
                
            # case "NEWLN":
            #     #add new line
            #     return
            
            # case "MULT":
            # #save the next 3 words and perform multiplication
            #     MULT_func(Input, Token, index, var_arr)


    for i in range(len(var_arr)) :
        if (len(var_arr[i])) != 2:
            var_arr.pop(i) 
            break
    
    return var_arr

def BEG_func(Input, Token, var_arr, varTable, index):
    
    begarr = []
    print("nadakpan si beg")
    rightword = Input[index+1]
    for j in range(len(varTable)):
        if rightword == varTable[j][1]:
            print(rightword)
            print(varTable[j][1])
            if varTable[j][0] == "STR":
                holder = (varTable[j], simpledialog.askstring(title="Input", prompt="Input for " + rightword))
                begarr.append(holder)
                print("string siya")
            elif varTable[j][0] == "INT":
                holder = (varTable[j], simpledialog.askinteger(title="Input", prompt="Input for " + rightword))
                begarr.append(holder)
                print("int sya")

    return holder
                
                

def PRINT_func(Input, Token, varTable, index, var_arr):
    literals = ["ADD", "SUB", "MULT", "DIV", "MOD"]
    # print("wow")
    # print("nisulod sa PRINT")
    # print(Input[index])
    value = -1
    rightword = Input[index+1]
    tokenrightword = Token[index+1]
    evaluationArray = []
    
    def append_values(Input):
        tempArray = []
        isFound = False
        for item in Input:
            if isFound:
                tempArray.append(item)
            elif item in literals:
                isFound = True
                tempArray.append(item)
        return tempArray
        
    evaluationArray = append_values(Input)
    
    # print(var_arr)
    # print("----")
    # print(rightword)
    if tokenrightword == "IDENT":
        for i in range(len(var_arr)):
            # print("=====")
            # print(var_arr[i][0][1] + "vs" + rightword)
            temp = var_arr[i][0][1]
            if rightword == temp:
                #print("nakasulod diri" + rightword)
                value = var_arr[i][1]
                print("the value of "+ rightword + " is " + str(value))
    elif tokenrightword in literals:
        print(f"PRINT_FUNC:: test [{operatorsFunction(evaluationArray, var_arr)}]")

    # elif tokenrightword == "MULT":
    #     print("operator iyang tapad.")
    #     #iinsert ang operation na rule
    # elif tokenrightword == "MOD":
    #     print("operator iyang tapad.")
    #     #iinsert ang operation na rule
    # elif tokenrightword == "DIV":
    #     print("operator iyang tapad.")
    #     #iinsert ang operation na rule
    # elif tokenrightword == "ADD":
    #     print("operator iyang tapad.")
    #     #iinsert ang operation na rule
    # elif tokenrightword == "SUB":
    #     print("operator iyang tapad.")
        #iinsert ang operation na rule
    else:
        value = rightword
        print("the value of "+ rightword + " is " + value)
    #print("++++")
    
    
def IS_func(Input, varTable, index, Token, var_arr):
    literals = ["ADD", "SUB", "MULT", "DIV", "MOD"]
    evaluationArray = []
    holder =  ""
    # print("-----")
    # print(Token)
    # print("nisulod sa IS")
    # print("nadakpan si is")
    # print(Input[index])

    print(f"ENTERED IS:: Input [{Input}]")
    print(f"IS_FUNC:: VarTable [{varTable}]")
    print(f"IS_FUNC:: Token [{Token}]")
    print(f"IS_FUNC:: var_arr [{var_arr}]")

    #get only the values for operation

    def append_values(Input):
        tempArray = []
        isFound = False
        for item in Input:
            if isFound:
                tempArray.append(item)
            elif item in literals:
                isFound = True
                tempArray.append(item)
        return tempArray

        
    evaluationArray = append_values(Input)
    print(f"IS_FUNC:: evaluationArray [{evaluationArray}]")



    leftword = Input[index-1]                             #get lefword ni is 
    inputrightword = Input[index+1]                       #get rightword ni is
    tokenizedrightword = Token[index+1]
    print("========")
    print(tokenizedrightword)
    # print("left ni is")
    # print(leftword)
    # print("right ni is")
    # print(inputrightword)
    # print("right ni is pero tokenized version")
    # print( finalTokenArrrightword)


    for i in range(len(varTable)):                      
        if leftword == varTable[i][1]:                    #if leftword naga exist sa vartable
            if tokenizedrightword == "INT_LIT": #if rightword kay INT_LIT iyang tokenized version
                holder = (varTable[i], inputrightword)    #hold ang Datatype, varname, and rightword ni is
            elif tokenizedrightword in literals:
                inputrightword = operatorsFunction(evaluationArray, var_arr)
                print(f"IS_FUNC:: test [{inputrightword}]")
                holder = (varTable[i], inputrightword)
            # elif tokenizedrightword == "MULT":
            #     #insert mult operation
            #     print("mult iyang tapad.")
            # elif tokenizedrightword == "ADD":
            #     print("ADD iyang tapad.")
            #     #insert add operation
            # elif tokenizedrightword == "MOD":
            #     print("MOD iyang tapad.")
            #     #insert mod operation
            # elif tokenizedrightword == "SUB":
            #     print("SUB iyang tapad.")
            #     #insert SUB operation
            # elif tokenizedrightword == "DIV": 
            #     print("DIV iyang tapad.")
                #insert DIV operation  
            else:
                for i in range(len(var_arr)):
                    if inputrightword == var_arr[i][0][1]:
                        inputrightword = int(var_arr[i][1])
                        break
                # return variable, counter
                holder = (varTable[i], inputrightword)
                print("diri tung pag ang variable ang right side ni IS")

    
                #iconvert ang variable to iyahang data  
    #call the table, assign var and its value as tuple to the table\\
    #assuming IS is the index, the index-1 should be the variable, index+1 should be value
    #check if operator, a variable, or none
    #keyword = Input[index+1]     


    #check if varname already exist in var_arr
    for i in range(len(var_arr)):
        if leftword == var_arr[i][1]:
            var_arr.pop(i)
            break

    var_arr.append(holder)
    return var_arr

# def MULT_func(Input, Token, index, var_arr):
#     #check the next 2 words, convert if var
#     if(Token[index+1] == "IDENT"):
#         num1 = var_reveal(Input, index+1, var_arr)
#     else:
#         num1 = Input[index+1]
    
#     if(Token[index+2] == "IDENT"):
#         num2 = var_reveal(Input, index+2, var_arr)
#     else:
#         num2 = Input[index+2]
    
#     return num1 * num2