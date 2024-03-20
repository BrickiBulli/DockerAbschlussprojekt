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

cursor = connection.cursor()
cursor.execute('Select ID FROM users WHERE FirstName = ' + firstname +' Surname = ' + surname)
userID = cursor.fetchall()

print(userID)


#cursor = connection.cursor()
#cursor.execute('INSERT INTO users (FirstName, Surname) VALUES("Bill", "Test");')
#connection.commit()

connection.close()