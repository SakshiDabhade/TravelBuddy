import mysql.connector
from itertools import zip_longest

# create a connection to the MySQL database
cnx = mysql.connector.connect(user='Manasi', password='Mysql@Manasi2',
                              host='localhost', database='TravelBuddy')

# create a cursor object to execute SQL statements
cursor = cnx.cursor()

# execute an SQL query
query = 'SELECT PID FROM packages'
cursor.execute(query)
results = {
    'pid': [1001,1002],
    "From_City" : ["ABC","xyz"]  

}
# fetch the results of the query
resultss = cursor.fetchall()

# results['pid'] = resultss
# # print(dict(zip(l1, resultss[0])))
# # row = dict(zip(l1, resultss[0]))
# for row in results['pid']:
#     print(row)


# do something with the results

# close the cursor and connection
cursor.close()
cnx.close()