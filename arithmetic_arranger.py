import re

def arithmetic_arranger(problems, work = False):
    
    first_line = ""
    second_line = ""
    dotted_line = ""
    answers = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if len(firstNumber) > 4 or len(secondNumber) > 4 :
            return "Error: Numbers cannot be more than four digits."

        if(re.search("[*]",problem) or re.search("[/]",problem)):
            return "Error: Operator must be '+' or '-'"
            if(re.search("[^\s0-9.+-]",problem)):
                return "Error: Numbers must only contain digits."
        


    
print(arithmetic_arranger(["32 + 8", "1 - 3801", "999x + 9999", "523 - 49"]))