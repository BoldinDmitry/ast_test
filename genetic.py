def fitness(code):
    score = 40
    try:
        exec(code)
    except:
        score -= 40
    if "=" not in code:
        return 0
    lines_of_code = code.split("\n")
    variables_from_code = ""
    for i in range(len(lines_of_code)):
        if "=" in lines_of_code[i] and lines_of_code[i].split("=")[0].replace(" ", "") not in variables_from_code:
            variables_from_code += lines_of_code[i].split("=")[0].replace(" ", "")
            score -= i
    for i in range(len(lines_of_code)):
        if "print" in lines_of_code[i]:
            score += i
    return score

