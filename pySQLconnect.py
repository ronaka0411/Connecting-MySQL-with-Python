import pymysql.cursors
# Connect to the database.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',                             
                             db='compny',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")


'''
#For another database (db):
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
'''

try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT Dept_No, Dept_Name FROM Department "
         
        # Execute query.
        cursor.execute(sql)

        for row in cursor:
            print(row)
            
        print ("cursor.description: ", cursor.description)
 '''
        for row in cursor:
            print(row)
 '''            
finally:
    # Close connection.
    connection.close()
