from array import array

def line_compile(Input, Token, var_arr):
    print(Input)
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
                print("End of Cde")

            case "IS":
                #assign value from the next to previous
                var_arr.append(IS_func(Input, index))
                print("Assigned value to " + Input[index-1])

            case "BEG":
                #stop the program and ask the user for value
                return 

            case "NEWLN":
                #add new line
                return
            
            case "MULT":
            #save the next 3 words and perform multiplication
            case "DIV":
            case "ADD":
            case "SUB":
            case "MOD":
            

    return var_arr


def IS_func(Input, index):
    #call the table, assign var and its value as tuple to the table\\
    #assuming IS is the index, the index-1 should be the variable, index+1 should be value
    #check if operator, a variable, or none
    keyword = Input[index+1]

    match keyword:
       


    return (Input[index-1], Input[index+1])