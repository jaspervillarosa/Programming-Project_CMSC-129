#A simple lexical analyzer for a custom programming language
#Program UI including User Inputs and Program Outputs by Ferdinand Gador, Van Joseph P. Cabuga, and Jasper Villarosa
#Tokenization Process by Ferdinand Gador and Mark Christian Valderama

import os
import pathlib
from tkinter import *
from tkinter import filedialog
import tkinter
from turtle import left
from CodeTokenization import sourceCodeTokenizer
from HelperFunctions import convertTextToArray, saveTokenToFile
from Syntaxcheck import checksyntax


#----------------------------------------------------
#overwrites the existing loaded file with changes appended using the text editor, if there is no file path, i.e. no opened file, calls saveAs()
def save():
    if path != '':
        with open(path, 'w') as overwriteFile:
            content = textEditor.get(1.0, END)
            overwriteFile.write(content)

            consoleLabel.configure(text="Current File is Saved Sucessfully")
            consoleLabel.pack()
            
    else:
        saveAs()
#generates a new .iol file – asks the user for a filename and directory which it will be stored
def saveAs():
    saveAsFile = filedialog.asksaveasfile(mode='w', filetypes=[("String files","*.iol"),('Transitions','*.dfa')])
    if saveAsFile is None:
        return
    
    inputData = textEditor.get(1.0, END)
    saveAsFile.write(inputData)


    consoleLabel.configure(text="New Input File is Saved Sucessfully")
    consoleLabel.pack()

    saveAsFile.close()

# opens the file directory and allows the user to open a .iol file, said file will be printed and displayed on the UI textbox.
def openFile(): 
    global inputData, path
    path = filedialog.askopenfilename(filetypes=[("String files","*.iol"),('Transitions','*.dfa')])
    inputFile = open(path)
    inputData = inputFile.read()
    inputFile.close()

    textEditor.delete(1.0, tkinter.END)
    textEditor.insert(1.0, inputData)

    return path

#reads the .iol file, processes and performs lexical analysis through the sourceCodeTokenizer()
def compileCode():
    global finalTokenArr, varTable, errorEncountered, errorLine, unknownWord
    file = textEditor.get(1.0, tkinter.END)
    inputStringName = os.path.basename(path)
    array = []
    Arr = convertTextToArray(file)
    finalTokenArr, varTable, errorEncountered, errorLine, unknownWord= sourceCodeTokenizer(Arr)

    saveTokenToFile(finalTokenArr)
    
    if errorEncountered == True:
        consoleLabel.configure(text="Unknown word [ %s ] found in the program code | Error encountered in line [ %s ] !" %(unknownWord, errorLine))
        consoleLabel.pack()
    else:
        consoleLabel.configure(text="Tokenized Code for file name %s Compiled Sucessfully " %inputStringName)
        consoleLabel.pack()


    array, errorFlag = syntax()
    

    if (errorFlag == 1):
        consoleLabel.configure(text='')
        consoleLabel.pack()
        
        message = []
        for i in range(len(array)):
            for j in range(len(array[i])):
                if(array[i][j][0] == "2"):
                    message.append("Error in line %s, Error Found: %s\n" %(i+1, array[i][j][1]))

        displayMsg.delete('1.0', END)            
        for x in message:
            displayMsg.insert(END, x + '\n')
            displayMsg.pack()

    else:
        displayMsg.delete('1.0', END)
        res = "Syntax Analysis Successful without problems found."
        displayMsg.insert(END, res)
        displayMsg.pack()

    #proceed to functionality
    #split the string into line and individually check the functionality of each keyword in line
    code_function()

def code_function():
    #needs array of the original codes before tokenized
    #split code into line
    #send each line to another function
    #check each word on each line
    #assuming the code was created correctly(checked both lexical and syntax), assume functionality of keyword
    #create a match() for each keyword, if not keyword, assume either variable or constant
    #create an empty array to store output
    
    #idea, prepare var table to hold
     #for int/num/str, prepare variable with no content
    #for Beg, pause the program to ask user for input, check table for var name and save content to said var
    # for NEWLN, switch to next element of output array
    #for operators, take the next 2 element and apply the correct operation
    #for print, print the current var or constant
    
    #if IOL, start the program
    #if LOI, print Program terminated successfuly and end the code_function()
    
    return 0

    
def syntax():
    testArray = []
    errorFlag=0
    presytaxToken = finalTokenArr

    #flag = ("0", "")
    if(presytaxToken[0][0] == "IOL"):
        for i in range(len(presytaxToken)):
            #if there is an error in checksyntaxx, flag becomes more than 1, stop the program and print the problem
            syntaxArray = checksyntax(presytaxToken[i])

            for j in range(len(syntaxArray)):
                if(syntaxArray[j][0] == "2"):
                    errorFlag = 1
                    break
            testArray.append(syntaxArray)

    return testArray, errorFlag


# displays the tokenized version of the source code and its table of variables in the UI
def showTokenizeCode():
    
    fileExtension = pathlib.Path(path).suffix
    
    if(fileExtension=='.iol'):
        textFile = open(path)
        textFile.close()

        inputStringName = os.path.basename(path)

        if errorEncountered == TRUE:

            consoleLabel.configure(text="Cannot display tokenized version of the source code!" %(unknownWord, errorLine))
            consoleLabel.pack()

        else:
            consoleLabel.configure(text='')
            consoleLabel.pack()

            finalTokenstr = ""
            finalTokenstr += "Variable Used:\n" + "    ".join(map(str, varTable ))+ "\n" +"\n" + "Tokenized Code:" + "\n"
            for string in finalTokenArr:
                finalTokenstr += " ".join(map(str, string))
                finalTokenstr += "\n"

            finalTokenstr = finalTokenstr + "\n" 
            tokenAndVariablesLabel.create_text(210,245, text=finalTokenstr, fill='black')
            tokenAndVariablesLabel.pack()

            displayMsg.delete('1.0', END)
            res = "Tokenized Code for file name %s Compiled Sucessfully " %inputStringName
            displayMsg.insert(END, res)
            displayMsg.pack()


#----------------------------------------------------
mainWindow = Tk()
mainWindow.title('CMSC 129 - Programming Exercise 4 | Syntactic Analysis')

width= mainWindow.winfo_screenwidth()
height= mainWindow.winfo_screenheight()
mainWindow.geometry("%dx%d" % (width, height))
mainWindow.config(bg='lightgreen')

#----------------------------------------------------
mainMenuBar = Menu(mainWindow)
mainWindow.config(menu = mainMenuBar)

fileMenu = Menu(mainMenuBar, tearoff=0)
fileMenu.add_command(label='Open File', command=openFile)
fileMenu.add_command(label='Save as', command=saveAs)
fileMenu.add_command(label='Save', command=save)
mainMenuBar.add_cascade(label='File', menu=fileMenu)

functionalitiesMenu = Menu(mainMenuBar, tearoff=0)
functionalitiesMenu.add_command(label= 'Compile Code', command=compileCode)
functionalitiesMenu.add_command(label= 'Show Tokenize Code', command=showTokenizeCode)
functionalitiesMenu.add_command(label= 'Execute Code', command='')
#execute code button exist but there is no function connected to it
mainMenuBar.add_cascade(label='Functionalities', menu=functionalitiesMenu)

#----------------------------------------------------

encapsulatingFrame = LabelFrame(mainWindow, padx=10, pady=10)
encapsulatingFrame.pack()

editorAndCanvasFrame = LabelFrame(encapsulatingFrame, text='Built-in Editor', width=1000, height=900, padx=10, pady=10)
editorAndCanvasFrame.grid(row=0, column=0, padx=10, pady=10)

tokenAndVariablesFrame = LabelFrame(encapsulatingFrame, text='Table of Variables', width=500, height=900, padx=10, pady=10)
tokenAndVariablesFrame.grid(row=0,column=1)
tokenAndVariablesFrame.pack_propagate(False)


textEditor = Text(editorAndCanvasFrame, width=125, height=35)
textEditor.pack()

consoleFrame = LabelFrame(editorAndCanvasFrame,text='Console Log', width=1000, height=200)
consoleFrame.pack_propagate(False)
consoleFrame.pack()

consoleLabel = Label(consoleFrame, text='')
consoleLabel.pack(side='top')

tokenAndVariablesLabel = Canvas(tokenAndVariablesFrame, width=450, height= 850)
tokenAndVariablesLabel.pack(side='top')

displayMsg = Text(consoleLabel)
displayMsg.pack()

mainWindow.mainloop()