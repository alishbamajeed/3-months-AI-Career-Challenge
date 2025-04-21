# Variable  & Data Types 

name = "Alishba" # ismayee aik string store hua ha
age = 20 # ismayee aik integer store hua ha


# what is Data Types

fullName = "Alishba Majeed"
age = 20
height = 5.3
isStudent = True
focus = "Python"

# string : string is a sequence of characters iska mtlb ha koi bhi character
# yani Alphabets , words yeh Sentence jo Quotes mein likha ho (" " '')

words = "A"

# String Concatenation : is means jo bhi string ha wo ek dusre string ke saath jorta ha

firstName = "Alishba"
lastName = "Majeed"

fullName = firstName + " " + lastName
print(fullName)

# String Usefull Method 

# 1) Upper Case : is method ko use kar ka hum string ko upper case
    # mein convert kar sakte ha

student = "Iqra"
print(student.upper())
   
# 2) Lower case : is method ko use kar ka hum string ko lower case
    # mein convert kar sakte ha
    
student2 = "Amna"
print (student2.lower())

# 3) Tittle Case : har words ka 1st letter ko capital main liktye ha

student3 = "Fiza"
print(student3.title())

# 4) Stripe : dono side ki extra space ko remove kar deta ha

student4 = "     Zaniab"
print(student4.strip())

# 5) Replace : is method ko use kar ka hum string mein jo bhi word ha wo replace kar sakte ha

student5 = "mariyam"
print(student5.replace("mariyam", "ayesha"))

# 6) length : is method ko use kar ka hum string ki length ko dekh sakte ha

student6 = "Mariyam"
print(len(student6))


# F- String : is method ko use kar ka hum string mein variable ko use kar sakte ha

today = "Monday"
print(f"Today is {today}")


# f-string vs concatenation: is method ko use kar ka hum string mein variable
#  ko use kar sakte ha


tommorow = "Tuesday"
print("tommorow is " + tommorow)


#list : list ka ek order of collection ha jo bhi data type ka ho sakta ha yeh
       # mutable ha jo bhi change kar sakte ha

fruits = ["Apple" , " Mango" , " Grapes" , "Strawbarry"] 
print (fruits)      


# list usefull method
# 1) append : is method ko use kar ka hum list mein jo bhi element ha wo add kar sakte ha

color = ["Red" , "Blue" , "Green"]
color.append("Yellow")
print(color)

# 2) insert : is method ko use kar ka hum list mein jo bhi element ha wo add kar sakte ha

food = ["Biryani" , "Pizza" , "Burger"]
food.insert(0, "Chicken")
print(food)

# 3) remove : is method ko use kar ka hum list mein jo bhi element ha wo remove kar sakte ha

drinks = ["Coke" , "Pepsi" , "Sprite"]
drinks.remove("Pepsi")
print(drinks)

# 4) pop : is method ko use kar ka hum list mein jo bhi element ha wo remove kar sakte ha

isStudent = ["Alishba" , "Mariyam" , "Ayesha"]
isStudent.pop(2)
print(isStudent)

# 5) sort : is method ko use kar ka hum list mein jo bhi element ha wo sort kar sakte ha

number = [6 , 8 , 5, 3 , 2, 7]
number.sort()
print(number)

# 6) reverse : is method ko use kar ka hum list mein jo bhi element ha wo reverse kar sakte ha

alphabet = ["A" , "B" , "C" , "D" , "E"]
alphabet.reverse()
print(alphabet)


# 4) Tuple : tuple ka ek order of collection ha jo bhi data type ka ho sakta ha yeh 
# immutable ha jo bhi change nhi kar sakte ha
 
character = (" cinderalla" , "snow white" , "bella")
print(character)


#1) Count : is method ko use kar ka hum tuple mein jo bhi element ha wo count kar sakte ha

weather = ("sunny" , "rainy" , "cloudy" , "sunny")
print(weather.count("cloudy"))

#2) index : is method ko use kar ka hum tuple mein jo bhi element ha wo index kar sakte ha

weather = ("sunny" , "rainy" , "cloudy" , "sunny")
print(weather.index("cloudy"))


# 5) Dictionary : dictionary ka ek order of collection ha jo bhi data type ka ho sakta ha yeh
# mutable ha jo bhi change kar sakte ha

student = {
    "name" : "Alishba" ,
    "age" : 20 ,
    "isStudent" : True
}
print(student)

# Dictionary usefull method
# 1) get : is method ko use kar ka hum dictionary mein jo bhi element ha wo get kar sakte ha


student = {
    "name" : "Alishba" ,
    "age" : 20 ,
    "isStudent" : True
}
print(student.get("name"))

# 2) keys : is method ko use kar ka hum dictionary mein jo bhi element ha wo keys kar sakte ha

student = {
    "name" : "Alishba" ,
    "age" : 20 ,
    "isStudent" : True
}   
print(student.keys())

# 3) values : is method ko use kar ka hum dictionary mein jo bhi element ha wo values kar sakte ha

student = {
    "name" : "Alishba" ,
    "age" : 20 ,
    "isStudent" : True
}
print(student.values())

# 4) items : is method ko use kar ka hum dictionary mein jo bhi element ha wo items kar sakte ha

student = {
    "name" : "Alishba" ,
    "age" : 20 ,
    "isStudent" : True
}
print(student.items())

# 5) update : is method ko use kar ka hum dictionary mein jo bhi element ha wo update kar sakte ha

student = {
    "name" : "Alishba" ,
    "age" : 20 ,
    "isStudent" : True
}

student.update({"name" : "Mariyam"})
print(student)

# 6) Set : set ka ek order of collection ha jo bhi data type ka ho sakta ha yeh
# mutable ha jo bhi change kar sakte ha

student = {"Alishba" , "Mariyam" , "Ayesha"}
print(student)

# Set usefull method
# 1) add : is method ko use kar ka hum set mein jo bhi element ha wo add kar sakte ha

student = {"Alishba" , "Mariyam" , "Ayesha"}
student.add("Alishba")
print(student)

# 2) remove : is method ko use kar ka hum set mein jo bhi element ha wo remove kar sakte ha

student = {"Alishba" , "Mariyam" , "Ayesha"}
student.remove("Mariyam")
print(student)

# 7) Frozen Set : frozen set ka ek order of collection ha jo bhi data type ka ho sakta ha yeh
# immutable ha jo bhi change

student = frozenset({"Alishba" , "Mariyam" , "Ayesha"})
print(student)

# 8) Range : range ka ek order of collection ha jo bhi data type ka ho sakta ha yeh
# immutable ha jo bhi change

student = range(1, 10)
print(student)


