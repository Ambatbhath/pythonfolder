print("Hello, World")

print("Python has three numeric types: int, float, and complex")

myValue=1
print(myValue)
print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))


myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))


myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) +  " is of the data type "  + str(type(myValue)))


myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))


myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print("{}, you like a {} {}!".format(name,color,animal))
print("{}{}{}".format(color,animal,name))


"""Collections"""
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"

print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
