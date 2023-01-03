#function to convert the input file to array
def convertTextToArray(textFile):
    Arr = []                                    #array initialization
    content = textFile.split("\n")              #splits the content of the input file by line
    
    #for loop to iterate the array that contains the elements of the input file by line
    for i in range(len(content)): 
        content2 = content[i].split(" ")        #individualizes the words per elements from the lines 
        Arr.append(content2)                    #stores into another array
                                                    
    return Arr                                  #returns the Arr that will be used for tokenization
#function to save the Arr into .tkn file
def saveTokenToFile(Arr):
    outputFile = open("Tokens.tkn", "w")
    for i in range(len(Arr)):
        for j in range(len(Arr[i])):

            if j != (len(Arr[i])-1):
                outputFile.write(Arr[i][j] + " ")
            else:
                outputFile.write(Arr[i][j])
        
        if i != (len(Arr)-1):
            outputFile.write("\n")

    outputFile.close()
