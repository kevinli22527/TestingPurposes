import random
"""
number1 = input("Enter the first number:\n")
number2 = input("Enter the second number:\n")
number3 = input("Enter the third number:\n")
result = int(number1) + int(number2) + int(number3)
result2 = int(number1) + int(number2) - int(number3)
print("result 1 is: " + str(result))
print("result 2 is: " + str(result2))
"""
"""
operator = input("Enter the operator: \n")
operand1 = input("Enter the first operand: \n")
operand2 = input("Enter the second operand: \n")
if operator == "*":
    result = int(operand1) * int(operand2)
elif operator == "/":
    result = int(operand1) / int(operand2)
elif operator == "+":
    result = int(operand1) + int(operand2)
else:
    result = int(operand1) - int(operand2)
print("result is: " + str(result))
print("Yay!!!")
"""
theNumber = random.randrange(0, 1001)
guess = input("Enter your guess here: \n")
while int(guess) != theNumber:
    pettyremark = ""
    if int(guess) > theNumber:
        pettyremark = "Guess again. You were too high \n"
    else:
        pettyremark = "Guess again. You were too low \n"
    guess = input(pettyremark)
print("You got it!")
