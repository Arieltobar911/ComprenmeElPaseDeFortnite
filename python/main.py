from sans import  conexion, cursor, verify

class SCP:
  def __init__(self, nombre=None, cargo=None, sueldo=None):
    self.nombre = nombre
    self.sueldo = sueldo
    self.cargo = cargo

  def sp03(self):
    cursor.callproc("sp_listar_empleados_activos")
    resultados = []
    for result in cursor.stored_results():
      resultados.extend(result.fetchall())
    return resultados

  def sp04(self):
    cursor.callproc("sp_listar_empleados_todos")
    resultados = []
    for result in cursor.stored_results():
      resultados.extend(result.fetchall())
    return resultados

  def sp02(self, nombre, cargo, sueldo):
    cursor.callproc("sp_insertar_empleado", [nombre, cargo, sueldo, None])
    conexion.commit()

  def sp01(self, id_empleado):
    cursor.callproc("sp_borrado_logico_empleado", [id_empleado])
    conexion.commit()

  def sp05(self, id_empleado):
    cursor.callproc("sp_restaurar_empleado", [id_empleado])
    conexion.commit()

s = SCP()

if not verify:
  print("\nDebido a la nula respuesta de la DB, el programa termina aqui.\n¡Gracias!")
  exit()

print("Bienvenido a la base de datos.\nque quieres hacer?\n\n1 - Borrar\n2 - Insertar\n3 - Listar activos\n4 - Listar a todos\n5 - Restaurar")
option = int(input("\nR: "))

if option == 1:
    num = int(input("\nIngresa el id de empleado\nR: "))
    s.sp01(num)
    print("Empleado borrado lógicamente.")

elif option == 2:
    nombre = input("\nIngresa el nombre del empleador\nR: ")
    cargo = input("\nIngresa el cargo del empleador\nR: ")
    sueldo = int(input("\nIngresa el sueldo del empleador\nR: "))
    s.sp02(nombre, cargo, sueldo)
    datos = s.sp04()
    for dato in datos:
       print(dato)
    print("^^^^^^^^^^^^^^^^^^^^\n¡Empleado insertado!")

elif option == 3:
    empleados = s.sp03()
    print("\n--- EMPLEADOS ACTIVOS ---")
    for fila in empleados:
        print(fila)

elif option == 4:
    empleados = s.sp04()
    print("\n--- TODOS LOS EMPLEADOS ---")
    for fila in empleados:
        print(fila)

elif option == 5:
    num = int(input("\nIngresa el id de empleado\nR: "))
    s.sp05(num)
    print("Empleado restaurado correctamente.")
