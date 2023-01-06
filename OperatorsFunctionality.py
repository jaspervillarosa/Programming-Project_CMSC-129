def operatorsFunction(array,var_arr):
    # print(f"Array:: [{array}]")
    # print(f"OPERATORSFUNCTION:: var_arr[{var_arr}]")
    literals = ["ADD", "SUB", "MULT", "DIV", "MOD"]
    counter = 0
    def evaluate(array, counter):
        token = array[counter]
        if token not in literals and token.isdigit() and token.isnumeric():
            return int(token), counter
        elif token in literals:
            operator1, counter = evaluate(array, counter+1)
            # print(f"Operator 1:: {operator1}")
            operator2, counter = evaluate(array, counter+1)
            # print(f"Operator 2:: {operator2}")


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
        else:
            for i in range(len(var_arr)):
                if token == var_arr[i][0][1]:
                    variable = int(var_arr[i][1])
                    break
            return variable, counter

    evaluationOutput = evaluate(array, counter)
    # print(f"EVALUATION OUTPUT:: {evaluationOutput[0]}")
    return evaluationOutput[0]