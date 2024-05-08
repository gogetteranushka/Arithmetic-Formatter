## Arithmetic-Formatter

##Description :

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

<img width="89" alt="a1" src="https://github.com/gogetteranushka/Arithmetic-Formatter/assets/109903993/7b1131bd-a862-41fd-85b5-cc68b8494032">




Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example: 
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:

<img width="280" alt="image" src="https://github.com/gogetteranushka/Arithmetic-Formatter/assets/109903993/73823837-1247-4ddf-b6fb-828aacaaa41c">



Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:



##Rules : 

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

#Situations that will return an error :

1. If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
2. The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
3. Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
4. Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
5. If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
6. Numbers should be right-aligned.
7. There should be four spaces between each problem.
8. There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
