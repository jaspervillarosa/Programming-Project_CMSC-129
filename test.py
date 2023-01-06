testArray = ['IOL Execution: \n', 'Input for msg1: qweqw \n', 'Input for msg2: weqweqweqwer \n', 'Input for msg3: qzdfad \n', '\n', 'weqweqweqwer', 0, '\n', 'qzdfad', '0', '\nEnd of Execution']

print(testArray)
finalString = ""

for i in range(len(testArray)):
    
    
    if isinstance(testArray[i], str):
        finalString = finalString+testArray[i]
        print(f"if:: {finalString}")
    else:
        finalString = finalString+str(testArray[i])
        print(f"else:: {finalString}")


print(finalString)