import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM users')
students = cursor.fetchall()

print(students)

print("Hello pleas enter your fistname...")

firstname = input()

print("Hello pleas enter your surname...")

surname = input()

userinput = "Select UserID FROM users WHERE firstName = '" + firstname + "' AND surname = '" + surname + "';"

cursor = connection.cursor()
cursor.execute(userinput)
userID = [row[0] for row in cursor.fetchall()]
 
print(userID)


print("Enter your first number for the calculation")

#cursor = connection.cursor()
#cursor.execute('INSERT INTO users (FirstName, Surname) VALUES("Bill", "Test");')
#connection.commit()

connection.close()