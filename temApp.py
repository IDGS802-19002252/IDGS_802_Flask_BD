from db import get_connection

# try:
#   connection = get_connection()
#   with connection.cursor() as cursor:
#     cursor.execute('call getAll()')
#     resultset = cursor.fetchall()
#     for row in resultset:
#       print(row)
# except Exception as e:
#   print('ERROR WE: ', e)

# try:
#   connection = get_connection()
#   with connection.cursor() as cursor:
#     cursor.execute('call getOne(4)')
#     resultset = cursor.fetchall()
#     for row in resultset:
#       print(row)
# except Exception as e:
#   print('ERROR WE: ', e)

try:
  connection = get_connection()
  with connection.cursor() as cursor:
    cursor.execute('call insertAlumno(%s, %s, %s)', ('Fernanda', 'Perez', 'fernandaperez@gmail.com'))
  connection.commit()
  connection.close()
except Exception as e:
  print('ERROR WE: ', e)