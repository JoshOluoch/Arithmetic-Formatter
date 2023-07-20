def arithmetic_arranger(problems, work = False):
    
    first_line = []
    second_line = []
    third_line = []
    answers = []
        
    for item in problems:
        a, op, c = item.split()
        padding = max(len(a), len(c)) + 2
        a = a.rjust(padding)
        first_line.append(a)
        
        b = op + c.rjust(padding - 1)
        second_line.append(b)
        
        dotted = "-" * padding
        third_line.append(dotted)
                
        if op == "+":
            result = int(a) + int(c)
            result = str(result).rjust(padding)
            answers.append(result)
        elif op == "-":
            result = int(a) - int(c)
            result = str(result).rjust(padding)
            answers.append(result)
        else:
            return "Error:"
    spaces = "    "    
    for item in first_line:
        print(item, end='\n')
    for item in second_line:
        print(item, end="\n")
    for item in third_line:
        print(item, end="\n")
    
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))