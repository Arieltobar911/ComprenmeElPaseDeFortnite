import mysql.connector
import sys
from mysql.connector import Error

sys.stdout.reconfigure(encoding='utf-8') # codificacion UTF8

conexion = None
verify = False
cursor = None

try:
  conexion = mysql.connector.connect(
    host="localhost",          
    user="root",               
    password="Ingresa tu contraseña profe",  
    database="empresa"         
  )
  if conexion.is_connected():
    cursor = conexion.cursor()
    verify = True
    print("✅ Conexión exitosa a la Base de Datos")

except Error as e:
  print("❌ Error al conectar con la Base de Datos", e)
  conexion = None
  verify = False
  cursor = None

