import pygame
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="projekt",
  port='3306',
 database='pokedex'
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pokedex1")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)




