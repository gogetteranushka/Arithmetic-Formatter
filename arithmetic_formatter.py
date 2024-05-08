def arithmetic_arranger(problems, show_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    separator_line = ""
    result_line = ""

    for problem in problems:
        operands = problem.split()
        operand1, operator, operand2 = operands

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        top_line += operand1.rjust(width) + "    "
        bottom_line += operator + operand2.rjust(width - 1) + "    "
        separator_line += "-" * width + "    "

        if show_result:
            if operator == "+":
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            result_line += result.rjust(width) + "    "

    arranged_problems += top_line.rstrip() + "\n"
    arranged_problems += bottom_line.rstrip() + "\n"
    arranged_problems += separator_line.rstrip()

    if show_result:
        arranged_problems += "\n" + result_line.rstrip()

    return arranged_problems
arithmetic_arranger(["3801 - 2", "123 + 49"])
