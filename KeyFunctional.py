from array import array
from tkinter import simpledialog #a pop up dialog box library that will be use for the user input

from OperatorsFunctionality import operatorsFunction

def var_reveal(Input, index, var_arr):
    #check for var in var_arr
    for index in range(len(var_arr)):
        if(Input == var_arr[index][0]):
            return var_arr[index][1]

def line_compile(Input, Token, var_arr, varTable, finalTokenArr, output_arr):

    #take the 2 lines, read each word from token
    for index in range(len(Token)):
        inword = Input[index]       #important when handling idents, str, ints, and int_lit
        tkword = Token[index]       #compare each word with the token
                
        match tkword:
            case "IOL":
                #do nothing
                output_arr.append("IOL Execution: \n")
                
            case "LOI":
                #write end of code
                output_arr.append("\nEnd of Execution")
            case "IS":
                #assign value from the next to previous
                var_arr.append(IS_func(Input, varTable, index, Token, var_arr))
                #output_arr.append("Assigned value to " + Input[index-1])

            case "BEG":
                #stop the program and ask the user for value
                var_line, output_arr = BEG_func(Input, Token, var_arr, varTable, index, output_arr)
                var_arr.append(var_line)
                
            
            case "PRINT":
                #if PRINT is encounter and proceed of printing the message and result
                output_arr.append(PRINT_func(Input, Token, varTable, index, var_arr))
                
            case "NEWLN":
                 #add new line
                 output_arr.append("\n")


    for i in range(len(var_arr)) :
        if (len(var_arr[i])) != 2:
            var_arr.pop(i) 
            break
    
    return (var_arr, output_arr)

#function that checks the line if BEG is present and append a string or integer from user input
def BEG_func(Input, Token, var_arr, varTable, index, output_arr):
    
    begarr = []
    rightword = Input[index+1]
    for j in range(len(varTable)):
        if rightword == varTable[j][1]:
            if varTable[j][0] == "STR":
                holder = (varTable[j], simpledialog.askstring(title="Input", prompt="Input for " + rightword))
                begarr.append(holder) #ask the user for string input
            elif varTable[j][0] == "INT":
                holder = (varTable[j], simpledialog.askinteger(title="Input", prompt="Input for " + rightword))
                begarr.append(holder) #ask the user for integer input

    input = holder[1]
    output_arr.append("Input for " + rightword + ": " + input + "\n")
    return (holder, output_arr)
                
                
# a PRINT function that return the str and the evaluation str
def PRINT_func(Input, Token, varTable, index, var_arr):
    literals = ["ADD", "SUB", "MULT", "DIV", "MOD"]

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
    
    if tokenrightword == "IDENT":
        for i in range(len(var_arr)):
            # print(var_arr[i][0][1] + "vs" + rightword)
            temp = var_arr[i][0][1]
            if rightword == temp:
                value = var_arr[i][1]
                string = str(value)
                return " "+string
    elif tokenrightword in literals:
        return " "+str(operatorsFunction(evaluationArray, var_arr))

    else:
        value = rightword
        string =value
        return " "+str(string)
    
# a function that check if IS is present in the array and check the right side and left side to avoid errors
# append the values on the right side of IS which is a literal value  
def IS_func(Input, varTable, index, Token, var_arr):
    literals = ["ADD", "SUB", "MULT", "DIV", "MOD"]
    evaluationArray = []
    holder =  ""

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

        
    evaluationArray = append_values(Input) #place the values inside the evaluation array



    leftword = Input[index-1]                             #get lefword of IS
    inputrightword = Input[index+1]                       #get rightword of IS
    tokenizedrightword = Token[index+1]
    print("========")
    print(tokenizedrightword)


    for i in range(len(varTable)):                      
        if leftword == varTable[i][1]:                    # check if leftword exist in the vartable
            if tokenizedrightword == "INT_LIT":          #if rightword kay INT_LIT iyang tokenized version
                holder = (varTable[i], inputrightword)    #hold the Datatype, varname, and rightword of IS
            elif tokenizedrightword in literals:
                inputrightword = operatorsFunction(evaluationArray, var_arr)
                holder = (varTable[i], inputrightword)

            else:
                for i in range(len(var_arr)):
                    if inputrightword == var_arr[i][0][1]:
                        inputrightword = int(var_arr[i][1])
                        break
                holder = (varTable[i], inputrightword)  #holder of the right side variable of IS


    #check if varname already exist in var_arr
    for i in range(len(var_arr)):
        if leftword == var_arr[i][1]:
            var_arr.pop(i)
            break

    var_arr.append(holder)
    return var_arr