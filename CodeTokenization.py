import re
#function for the lexical analysis of each element in the array 
def sourceCodeTokenizer(Arr):
    #lines 5-22 are the Regular Expressions initialization to identify if the lexemes are valid combination of characters for this custom programming language
    iol_pattern = re.compile("^IOL$")
    loi_pattern = re.compile("^LOI$")
    checkStrUp_pattern = re.compile("^IOL|LOI|INT|IS|BEG|PRINT|ADD|SUB|MULT|DIV|MOD|STR|NEWLN$")
    checkStrLow_pattern = re.compile("^iol|loi|int|is|beg|print|add|sub|mult|div|mod|str|newln$")
    intLit_pattern = re.compile("^[-+]?[0-9]+$")
    var_pattern = re.compile("^[A-Za-z][A-Za-z0-9]*$")
    str_pattern = re.compile("^STR$")
    int_pattern =re.compile("^INT$")
    into_pattern = re.compile("^INTO$")
    is_pattern = re.compile("^IS$")
    beg_pattern = re.compile("^BEG$")
    print_pattern = re.compile("^PRINT$")
    add_pattern = re.compile("^ADD$")
    sub_pattern = re.compile("^SUB$")
    mult_pattern = re.compile("^MULT$")
    div_pattern = re.compile("^DIV$")
    mod_pattern = re.compile("^MOD$")
    newln_pattern = re.compile("^NEWLN$")
    #lines 24-26 array initializations
    identifiedVariables = []
    finalTokenArr = []
    varctr = ("", "")
    varTable = []
    #nested for loop that iterates through the individualized contents of the input file
    for i in range(len(Arr)):

        errorEncountered = False#flag
        errorLine = None
        unknownWord = None

        tokenizeArray = []
        #inner for loop to iterate through words per line of the array
        for j in range(len(Arr[i])):
            #lines 35-90 are control statements for manipulating the words of the array.
            if iol_pattern.match(Arr[i][j]) !=None:                                                                                                     #if condition if the current word matches IOL
                tokenizeArray.append("IOL")                                                                                                             #appends "IOL" into the tokenizeArray variable
            elif loi_pattern.match(Arr[i][j]) !=None:                                                                                                   #if condition if the current word matches LOI
                tokenizeArray.append("LOI")                                                                                                             #appends "LOI" into the tokenizeArray variable
            elif intLit_pattern.match(Arr[i][j]) !=None:                                                                                                #if condition if the current word matches for INT_LIT
                tokenizeArray.append("INT_LIT")                                                                                                         #appends "INT_LIT" into the tokenizeArray variable
            elif checkStrUp_pattern.match(Arr[i][j]) == None and checkStrLow_pattern.match(Arr[i][j]) == None and var_pattern.match(Arr[i][j]) != None: #if condition if the current word matches does not match any keywords, but match for variable
                tokenizeArray.append("IDENT")                                                                                                           #appends "IDENT" into the tokenizeArray variable since the current word is matches for the regular expression for variable or identifier
                if str_pattern.match(Arr[i][j-1]) != None:
                    varctr = "STR", "%s" %Arr[i][j]                                                                                     #if current word is identifier and word before it is STR
                    varTable.append(varctr)                                                                                               #appends "STR" and the current word into the varTable variable
                    identifiedVariables.append(Arr[i][j])                                                                                               #appends the current word into the identifiedVariables variable
                elif int_pattern.match(Arr[i][j-1]) != None:                                                                                            #if current word is identifier and word before it is INT
                    varctr = "INT", "%s" %Arr[i][j]                                                                                      #if current word is identifier and word before it is STR
                    varTable.append(varctr)                                                                                                #appends "INT" and the current word into the varTable variable
                    identifiedVariables.append(Arr[i][j])                                                                                               #appends "IOL" into the tokenizeArray variable
                else:                                                                                                                                   #if current word is an ident but was not initialize
                    if Arr[i][j] in identifiedVariables:                                                                                                #if current word is an ident but was not initialize but exists 
                        continue                                                                                                                        #in the identifiedVariable meaning it was initialized so continue to next iteration
                    else:                                                                                                                               #else, if not found this means current word is not initialized
                        print('Unknown words found in the program code | Error encountered in line %s : %s' %((i+1), Arr[i][j]))                        #notifies that it does not exist
                        tokenizeArray.append("ERR_LEX")                                                                                                 #append ERR_LEX
                        errorEncountered = True
                        errorLine = i+1
                        unknownWord = Arr[i][j]                                                                                          #sets flag to true
                        break                                                                                                                           #breaks from the statement block
            elif str_pattern.match(Arr[i][j]) != None:                                                                                                  #if current word matches STR
                tokenizeArray.append("STR")                                                                                                             #append STR to tokenizeArray    
            elif int_pattern.match(Arr[i][j]) != None:                                                                                                  #if current word matches INT
                tokenizeArray.append("INT")                                                                                                             #append INT to tokenizeArray
            elif into_pattern.match(Arr[i][j]) != None:                                                                                                 #if current word matches INTO
                tokenizeArray.append("INTO")                                                                                                            #append INTO to tokenizeArray
            elif is_pattern.match(Arr[i][j]) != None:                                                                                                   #if current word matches IS
                tokenizeArray.append("IS")                                                                                                              #append IS to tokenizeArray
            elif beg_pattern.match(Arr[i][j]) != None:                                                                                                  #if current word matches BEG
                tokenizeArray.append("BEG")                                                                                                             #append BEG to tokenizeArray
            elif print_pattern.match(Arr[i][j]) != None:                                                                                                #if current word matches PRINT
                tokenizeArray.append("PRINT")                                                                                                           #append PRINT to tokenizeArray
            elif add_pattern.match(Arr[i][j]) != None:                                                                                                  #if current word matches ADD
                tokenizeArray.append("ADD")                                                                                                             #append ADD to tokenizeArray
            elif sub_pattern.match(Arr[i][j]) != None:                                                                                                  #if current word matches SUB
                tokenizeArray.append("SUB")                                                                                                             #append SUB to tokenizeArray
            elif mult_pattern.match(Arr[i][j]) != None:                                                                                                 #if current word matches MULT
                tokenizeArray.append("MULT")                                                                                                            #append MULT to tokenizeArray                                                                                                            #append STR to tokenizeArray
            elif div_pattern.match(Arr[i][j]) != None:                                                                                                  #if current word matches DIV
                tokenizeArray.append("DIV")                                                                                                             #append DIV to tokenizeArray
            elif mod_pattern.match(Arr[i][j]) != None:                                                                                                  #if current word matches MOD
                tokenizeArray.append("MOD")                                                                                                             #append MOD to tokenizeArray
            elif newln_pattern.match(Arr[i][j]) != None:                                                                                                #if current word matches NEWLN
                tokenizeArray.append("NEWLN")                                                                                                           #append NEWLN to tokenizeArray
            elif Arr[i][j] == '':                                                                                                                       #if the program encounters an empty line
                tokenizeArray.append("")                                                                                                                #append whitespace into tokenizeArray
                continue                                                                                                                                #continue to next iteration
            else:                                                                                                                                       #if current word does not match any of the regular expressions, it is an unknown word
                print('Unknown words found in the program code |Error encountered in line %s : %s' %((i+1), Arr[i][j]))                                 #notify that an unknmown word exists
                tokenizeArray.append("ERR_LEX")                                                                                                         #current word is treated as ERR_LEX
                errorEncountered = True
                errorLine = i+1
                unknownWord = Arr[i][j]                                                                                                                  #sets flag to true
                break                                                                                                                                   #breaks from the statement block

        finalTokenArr.append(tokenizeArray)                                                                                                             #appends the tokenizeArray to finalTokenArr

        if errorEncountered == True:                                                                                                                    #sets flag to true
            break                                                                                                                                       #breaks out of inner for loop

    return finalTokenArr, varTable , errorEncountered, errorLine, unknownWord                                                                                                   #returns the finalTokenArr and varTable back to maininterface for display purposes