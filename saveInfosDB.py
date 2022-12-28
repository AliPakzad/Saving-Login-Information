import mysql.connector

import re

my_username = input()

regex = r'[a-zA-Z]+[\w]*@[a-zA-Z]+\.[a-zA-Z]{2,4}'


result = re.search(regex, my_username)


while result == None:
    print("Email address is not valid. Please enter an email with this format:")
    print("expression@string.string")
    username = input()
    result = re.search(regex, my_username)

print("Your email is accepted")

print("Enter your password")

my_password = input()

print(f'your pass is :{my_password}')

cnx = mysql.connector.connect(user='root', password='@lexander8891',
                              host='127.0.0.1',
                              database='infoDB')
print("connected to DB")
cursor = cnx.cursor(buffered=True)

#cursor.execute("CREATE TABLE information(username varchar(255), password varchar(255))")

cursor.execute("INSERT INTO information VALUES(\'%s\', \'%s\')" %(my_username, my_password))

cnx.commit()

cursor.execute("SELECT * From information;")
cnx.commit()

results = cursor.fetchall()

for row in results:
  print(row)

cnx.close()
