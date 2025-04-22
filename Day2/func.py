# Function is a block of code that perform a specific task

# Syntax

# Simple function : function koi simple kam kree tu yeh use krege
def full_name():
    print("Alishba Majeed")

full_name()

# Parameter Function : jab humay kisi ko parameter pass krege tu yeh use krege
def numberAdd(a,b):
    print("Sum:" , a+b)
numberAdd(2 , 6)   

def student(name , age ):
    print("Student Name:" , name)
    print("Student Age:" , age)

student("Alishba" , 20)    


# Default Parameter Function : jab humay koi parameter ko default value de denay hain tu yeh use krege

def greet(name = "Mariyam"):
    print("Asalam o Alikum:" , name)
greet()
greet("Alishba")    


def sum(a , b = 20):
    print("Sum:", a+b)

sum(10)
sum(6)

# *args : jab humay unknown number of values pass krege tu yeh use krege

def add (*args):
    print("sum:" ,(args))
add(2, 3 , 4 , 5)    


def full_name (*args):
    print("fullname" ,(args))
add("Alisba" ," Manahil")   


# **kwargs : jab humay unknown number of key value pass krege tu yeh use krege

def info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

info(name = "Alishba" , age = 19 , course = "python")        

# lamda function : jab humay koi function ko ek line mein likhna ho tu yeh use krege

sum = lambda a,b : a+b
print(sum(2,3))

square = lambda x : "alishba" + "Shahmeer"
print(square(1))


# recursive function : bar bar khud ko  call krna jab tak kam poora na hu 

def facterical(n):
    if n == 0:
        return
    print(n)
    facterical(n - 1)
facterical(5)


# high order function : jab humay function ko function mein pass krege tu yeh use krege

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# 👇 Higher-order function
def speak(func):
    result = func("Hello Alishba!")
    return result

print(speak(shout))   # HELLO ALISHBA!
print(speak(whisper)) # hello alishba!


