 # Calculator 

num = int(input("Enter a number :"))
operator = input("Enter an operator  (+ , - , * , /): ")
num2 = int(input("Enter a number :"))

if operator == "+":
    print(num + num2)
elif operator == "-":
    print (num - num2)    
elif operator == "*":
    print(num * num2)
elif operator == "/":
        print(num / num2)

else :
     print("Invalid operator")