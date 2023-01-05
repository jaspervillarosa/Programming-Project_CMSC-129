def operatorsFunction(array):
    literals = ["ADD", "SUB", "MULT", "DIV", "MOD"]
    counter = 0
    def evaluate(array, counter):
        token = array[counter]
        if token not in literals:
            return token, counter
        else:
            operator1, counter = evaluate(array, counter+1)
            operator2, counter = evaluate(array, counter+1)

            if token == "ADD":
                return operator1+operator2, counter
            elif token == "SUB":
                return operator1-operator2, counter
            elif token == "MULT":
                return operator1*operator2, counter
            elif token == "DIV":
                return operator1//operator2, counter
            elif token == "MOD":
                return operator1%operator2, counter

    evaluationOutput = evaluate(array, counter)
    return evaluationOutput[0]