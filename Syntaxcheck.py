#Check syntax function takes each line from the tokenized version of the input as an argument which it processes to check for proper grammar and language construction
#each case switches are attached to specific rules which determines what are the valid/invalid word constructions that make a grammar true.

from array import array
def checksyntax(Arr):
    iolctr = ("0", "")
    iolctrArray = []

    for index in range(len(Arr)):
        word = Arr[index]

        match word:
            case "IOL":
                iolctr = ("1", "")
                iolctrArray.append(iolctr)
                print(iolctr)
            case "LOI":
                iolctr = ("0", "")
                iolctrArray.append(iolctr)
                print(iolctr)
            case "INT_LIT":
                iolctr = intLit_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "INT":
                iolctr = int_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "IDENT":
                iolctr = ident_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "IS":
                iolctr = is_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "STR":
                iolctr = str_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "NEWLN":
                iolctr = newln_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "BEG":
                iolctr = beg_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "PRINT":
                iolctr = print_syntax(Arr)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "ADD":
                iolctr = op_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "SUB":
                iolctr = op_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "MULT":
                iolctr = op_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "DIV":
                iolctr = op_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
            case "MOD":
                iolctr = op_syntax(Arr, index)
                iolctrArray.append(iolctr)
                print(iolctr)
    return iolctrArray

#each function from lines 77 - 170 designate every rules and conditions that must be follow to make the grammar of the language true

def op_syntax(Arr, index):
    op_next = Arr[index+1]
    if(op_next != "IDENT" and op_next != "INT_LIT"):
        return ("2", "Next element is not IDENT: " + op_next)
        
    op_nextnext = Arr[index+2]
    if(op_nextnext != "IDENT" and op_nextnext != "INT_LIT"):
        return ("2", "Next next element is not IDENT:" + Arr[index+2])

    return ("1", "")

def beg_syntax(Arr, index):
    begnext = Arr[index+1]

    if(begnext != "IDENT"):
        return ("2", "IDENT is not NEXT")
    
    return ("1", "")


def print_syntax(Arr):
    if(Arr.count("PRINT") > 1):
        return  ("2", "More than 2 prints in a line")

    return ("1", "")

def int_syntax(Arr, index):
    if index != (len(Arr)-1):
        if Arr[index+1] != "IDENT":
            return("2", "no variable attached to INT")
        else:
            return("1", "")
    else:
        return("2", "INT initialised at the end of line")

def intLit_syntax(Arr, index): #INT IDENT IS INT_LIT
    literals = ["IS", "IDENT"]
    if Arr[index-1] not in literals:
        return("2", "not assigned to a variable or used in an expression")
    else:
        return("1","")

def ident_syntax(Arr, index):
    literals = ["INT", "STR", "BEG", "PRINT", "IDENT"]
    operatorLiterals = ["ADD", "SUB", "MULT", "DIV", "MOD"]
    operatorRightSide = ["IDENT", "INT_LIT"]
    if Arr[index-1] in literals:
        if Arr[index-1] == "INT":
            if Arr[index+1] != "IS":
                return("2", "no IS to designate a value with")
            else:
                return("1", "")
        else:
            return("1", "")
    elif Arr[index-1] in operatorLiterals:
        if index != (len(Arr)-1):
            if Arr[index+1] not in operatorRightSide:
                return("2", "another IDENT or INT_LIT not found")
            else:
                return("1", "")
        else:
            return("2", "Missing another IDENT or INT_LIT to complete expression")

def is_syntax(Arr, index):
    literals = ["INT_LIT", "IDENT", "ADD", "SUB", "MULT", "DIV", "MOD"]
    if index != (len(Arr)-1):
        if Arr[index-1] == "IDENT":
            if Arr[index+1] not in literals:
                return("2", "token after IS is an violates syntactic rule")
            else:
                return("1", "")            
        else:
            return("2", "no variable to assign value with")
    else:
        return("2", "IS initialised at the end of line")

def str_syntax(Arr, index):
    if index != (len(Arr)-1):
        if Arr[index+1] != "IDENT":
            return("2", "no variable next to STR found")
        else:
            return("1", "")
    else:
        return("2", "STR initiated at the end of line")

def newln_syntax(Arr, index):
    specificLiterals = ["LOI", "IOL"]
    if index != 0:
        if Arr[index-1] in specificLiterals:
            return("2", "literal before a NEWLN")
        else:
            return ("1", "")
    else:
        return("1", "")