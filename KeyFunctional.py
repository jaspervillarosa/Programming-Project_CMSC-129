from array import array
from tkinter import simpledialog

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
        
        match tkword:
            case "IOL":
                #do nothing
                print("IOL")
                
            case "LOI":
                #write end of code
                print("End of Code")

            case "IS":
                #assign value from the next to previous
                var_arr.append(IS_func(Input, varTable, index, Token))
                print("Assigned value to " + Input[index-1])

            case "BEG":
                #stop the program and ask the user for value
                var_arr.append(BEG_func(Input, Token, var_arr, varTable, index))
                
            


            # case "NEWLN":
            #     #add new line
            #     return
            
            # case "MULT":
            # #save the next 3 words and perform multiplication
            #     MULT_func(Input, Token, index, var_arr)


            

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
                
                



def IS_func(Input, varTable, index, Token):
    holder =  ""
    print("-----")
    print(Token)
    print("nisulod sa IS")
    print("nadakpan si is")
    print(Input[index])
    
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
            elif tokenizedrightword == "MULT":
                #insert mult operation
                print("mult iyang tapad.")
            elif tokenizedrightword == "ADD":
                print("ADD iyang tapad.")
                #insert add operation
            elif tokenizedrightword == "MOD":
                print("MOD iyang tapad.")
                #insert mod operation
            elif tokenizedrightword == "SUB":
                print("SUB iyang tapad.")
                #insert SUB operation
            elif tokenizedrightword == "DIV": 
                print("DIV iyang tapad.")
                #insert DIV operation  
            else:
                print("diri tung pag ang variable ang right side ni IS")
                #iconvert ang variable to iyahang data  
    #call the table, assign var and its value as tuple to the table\\
    #assuming IS is the index, the index-1 should be the variable, index+1 should be value
    #check if operator, a variable, or none
    #keyword = Input[index+1]     

    return holder

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
