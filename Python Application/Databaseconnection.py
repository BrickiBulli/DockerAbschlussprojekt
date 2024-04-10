import mysql.connector
import os

os.system('clear')

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")



id = ""

while id == "":
    print("Pleas enter your fistname...")

    firstname = input()

    print("Pleas enter your surname...")

    surname = input()

    userinput = "Select UserID FROM users WHERE firstName = '" + firstname + "' AND surname = '" + surname + "';"

    cursor = connection.cursor()
    cursor.execute(userinput)
    userID = [row[0] for row in cursor.fetchall()]

    if not userID:
        id = ""
    else :
        id = userID[0]

    print("Invalid Login please try again")

os.system('clear')

print("Welcome back " + firstname + " " + surname)

print("Do you want to make a calculation (y) / (n)")

repeat = input()

while repeat != "n":

    print("Enter your first number for the calculation")

    firstNumber = input()

    while type(firstNumber) == int or type(firstNumber) == float:
        firstNumber = input()

    print("Enter your second number for the calculation")

    secondNumber = input()

    while type(secondNumber) == int or type(secondNumber) == float:
        secondNumber = input()

    print("Enter the kind of opperation you would like to do (+|-|*|/)")

    opperation = input()

    while opperation != "+" and opperation != "-" and opperation != "*" and opperation != "/":
        opperation = input()

    if opperation == "+":
        result = float(firstNumber) + float(secondNumber)
    if opperation == "-":
        result = float(firstNumber) - float(secondNumber)
    if opperation == "*":
        result = float(firstNumber) * float(secondNumber)
    if opperation == "/":
        result = float(firstNumber) / float(secondNumber)

    print("Your result is: " + str(result))

    insertCommand = "INSERT INTO calculatorHistory (Result, FirstNumber, SecondNumber, Operation, UserID) VALUES (" +str(result)+ ", " +firstNumber+", "+secondNumber +", '"+opperation+"', '"+str(id)+"');"
    cursor.execute(insertCommand)
    connection.commit()

    print("Do you want to make another calculation (y) / (n)")

    repeat = input()

print("Do you want to see your Calculator history if yes Type how many you would like to see (as a Number) if you dont want to see them press (n)")

historyInput = input()

if historyInput != "n" and type(int(historyInput)) == int:  
    sqlCommand = "Select * FROM calculatorHistory WHERE UserID = "+str(id)+" ORDER BY ID DESC LIMIT " +str(historyInput)+ ";"
    cursor.execute(sqlCommand)
    calculatorHistorys = cursor.fetchall()
    for calculatorHistory in calculatorHistorys:
        print("First number: " +str(calculatorHistory[2])+ " Second number: " + str(calculatorHistory[3])+ " Operation: " + str(calculatorHistory[4])+ " Result: " + str(calculatorHistory[1]))
    
connection.close()