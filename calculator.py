def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def division(a,b):
  return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}
def calculator():
    number1=int(input("enter the first number:"))
    for symbol in operations_dict:
      print(symbol)
    continue_flag=True
    while continue_flag:
       op_symbol=input("pick an operation:")
       number2=int(input("enter the second number:"))
       calculator_function=operations_dict[op_symbol]
       output=calculator_function(number1,number2)
       print(f"{number1}{op_symbol}{number2}={output}")

       should_continue=input(f"enter 'y' to continue calculation with {output} or 'n' to exit:").lower()
       if should_continue=='y':
         number1=output
       elif should_continue=='n':
         continue_flag=False
         calculator()
       else:
         continue_flag=False
         print("Bye")
calculator()
